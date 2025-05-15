from config0_publisher.terraform import TFConstructor


def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_optional(key="aws_default_region",
                                 default="us-east-1",
                                 tags="tfvar,db,resource,tf_exec_env",
                                 types="str")
    
    stack.parse.add_optional(key="ssh_key_name",
                                 default="terraform-generated-key",
                                 tags="tfvar,db",
                                 types="str")
    
    stack.parse.add_optional(key="public_key",
                                 default="null",
                                 tags="tfvar,db",
                                 types="str")
    
    stack.parse.add_optional(key="public_key_base64",
                                 default="null",
                                 tags="tfvar,db",
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
