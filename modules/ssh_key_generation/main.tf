# Generate a new SSH key pair
resource "tls_private_key" "ssh_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Output the key details as base64 encoded
output "public_key_base64" {
  value     = base64encode(tls_private_key.ssh_key.public_key_openssh)
  sensitive = false
}

output "private_key_base64" {
  value     = base64encode(tls_private_key.ssh_key.private_key_pem)
  sensitive = true
}

# Also provide original format for convenience
output "public_key" {
  value     = tls_private_key.ssh_key.public_key_openssh
  sensitive = false
}

output "private_key" {
  value     = tls_private_key.ssh_key.private_key_pem
  sensitive = true
}
