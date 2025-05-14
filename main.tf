module "ssh_key_generation" {
  source = "./modules/ssh_key_generation"
}

module "aws_key_upload" {
  source             = "./modules/aws_key_upload"
  ssh_key_name       = var.ssh_key_name
  aws_default_region = var.aws_default_region
  public_key_base64  = module.ssh_key_generation.public_key_base64
}

output "key_pair_name" {
  value = module.aws_key_upload.key_pair_name
}

provider "aws" {
  region = var.aws_default_region
}

terraform {
  required_version = ">= 1.0.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0.0"
    }
    tls = {
      source  = "hashicorp/tls"
      version = ">= 3.1.0"
    }
  }
}

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
