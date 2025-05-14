from config0_publisher.terraform import TFConstructor


def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    stack.parse.add_required(key="ssh_key_name",
                             default="terraform-generated-key",
                             tags="db",
                             types="str")

    # Add execgroup
    stack.add_execgroup("williaumwu:::demo1-aws_ssh_keys::ssh_key_generation",
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
                       provider="terraform",
                       tf_runtime="tofu:1.9.1",
                       resource_name=stack.ssh_key_name,
                       resource_type="ssh_key_pair")

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()
