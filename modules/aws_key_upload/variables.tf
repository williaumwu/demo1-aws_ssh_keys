variable "aws_default_region" {
  description = "AWS region where the key pair will be created"
  type        = string
  default     = "us-east-1"
}

variable "ssh_key_name" {
  description = "Name of the SSH key pair in AWS"
  type        = string
  default     = "terraform-generated-key"
}

variable "public_key" {
  description = "Public key content to upload to AWS"
  type        = string
  default     = ""
}

variable "public_key_base64" {
  description = "Base64 encoded public key content to upload to AWS"
  type        = string
  default     = ""
}
