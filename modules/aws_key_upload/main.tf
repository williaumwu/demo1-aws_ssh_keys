# Upload the public key to AWS
resource "aws_key_pair" "generated_key" {
  key_name   = var.key_name
  public_key = var.public_key_base64 != "" ? base64decode(var.public_key_base64) : var.public_key
}

# Output the key pair name
output "key_pair_name" {
  value = aws_key_pair.generated_key.key_name
}
