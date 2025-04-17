terraform {
  required_version = ">= 1.0.0" # Ensure that the Terraform version is 1.0.0 or higher

  required_providers {
    aws = {
      source = "hashicorp/aws" # Specify the source of the AWS provider
      version = "~> 4.0"        # Use a version of the AWS provider that is compatible with version
    }
  }
}

provider "aws" {
  profile = "personal"   # specify the name of the profile to use from .aws/profiles
}

resource "aws_organizations_account" "test-dev" {
  name = "test-dev"
  email = "khalid.dev24+2@gmail.com"
  iam_user_access_to_billing = "ALLOW"
  tags = {"account": "test-dev"}
}

output "account_id" {
  value = aws_organizations_account.test-dev.id
}