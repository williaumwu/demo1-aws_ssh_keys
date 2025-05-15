def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    stack.parse.add_required(key="ssh_key_name",
                             types="str")

    stack.parse.add_required(key="public_key_base64",
                             types="str")

    stack.parse.add_optional(key="aws_default_region",
                                 default="us-east-1",
                                 types="str")

    stack.add_substack("williaumwu:::ssh_key_generation")
    stack.add_substack("williaumwu:::aws_key_upload")

    # Initialize
    stack.init_variables()
    stack.init_substacks()

    human_description = f"Create ssh key name {stack.ssh_key_name}"
    inputargs = {
        "arguments": {"ssh_key_name": stack.ssh_key_name},
        "automation_phase": "infrastructure",
        "human_description": human_description
    }

    stack.ssh_key_generation.insert(display=True, **inputargs)

    human_description = f"Upload ssh key name {stack.ssh_key_name}"
    inputargs = {
        "arguments": {
            "ssh_key_name": stack.ssh_key_name,
            "public_key_base64": stack.public_key_base64,
            "aws_default_region": stack.aws_default_region
            },
        "automation_phase": "infrastructure",
        "human_description": human_description
    }

    stack.aws_key_upload.insert(display=True, **inputargs)

    return stack.get_results()
