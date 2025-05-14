# Output the key details as base64 encoded
output "public_key_base64" {
  value     = base64encode(tls_private_key.ssh_key.public_key_openssh)
  sensitive = false
}

output "private_key_base64" {
  value     = base64encode(tls_private_key.ssh_key.private_key_pem)
  sensitive = true
}
