# Upload the public key to AWS
resource "aws_key_pair" "default" {
  key_name   = var.ssh_key_name
  public_key = var.public_key_base64 != "" ? base64decode(var.public_key_base64) : var.public_key
}
