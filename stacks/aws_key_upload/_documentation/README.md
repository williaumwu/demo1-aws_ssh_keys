# aws_key_upload

A stack that creates aws_ssh_key

## Stack Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| aws_default_region | string | No | "us-east-1" | AWS region where the key pair will be created |
| ssh_key_name | string | No | "terraform-generated-key" | Name of the SSH key pair in AWS |
| public_key | string | No | "" | Public key content to upload to AWS |
| public_key_base64 | string | No | "" | Base64 encoded public key content to upload to AWS |
