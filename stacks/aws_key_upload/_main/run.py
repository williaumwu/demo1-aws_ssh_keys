from config0_publisher.terraform import TFConstructor

def _get_public_key_base64(stack):
    return stack.get_resource(
        name=stack.ssh_key_name,
        must_be_one=True,
        use_labels="project",
        resource_type=stack.resource_type_ssh_key,
    )[0]["public_key_base64"]

def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_optional(key="aws_default_region",
                             default="us-east-1",
                             tags="tfvar,db,resource,tf_exec_env",
                             types="str")
    
    stack.parse.add_required(key="ssh_key_name",
                             tags="tfvar,db",
                             types="str")
    
    stack.parse.add_optional(key="public_key_base64",
                             default="null",
                             tags="tfvar,db",
                             types="str")

    stack.parse.add_optional(key="resource_type_ssh_key",
                             default="ssh_key_pair",
                             types="str")
    
    # Add execgroup
    stack.add_execgroup("williaumwu:::demo1-aws_ssh_keys::aws_key_upload",
                        "tf_execgroup")

    # Add substack
    stack.add_substack('config0-publish:::tf_executor')

    # Initialize
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    if not stack.public_key_base64:
        stack.set_variable("public_key_base64", _get_public_key_base64(stack))

    stack.set_variable("timeout", 300)

    # use the terraform constructor (helper)
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       provider="aws",
                       tf_runtime="tofu:1.9.1",
                       resource_name=stack.ssh_key_name,
                       resource_type="aws_ssh_key")

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()
