# Output the key pair name
output "key_pair_name" {
  value = aws_key_pair.default.key_name
}
