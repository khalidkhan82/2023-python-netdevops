provider "aws" {
  region = "us-west-1"
}

resource "aws_instance" "test-instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "MyFirstInstance"
  }
}

variable "aws_profile" {
    type = string
    default = null
}

variable "aws_region" {
    type = string
    default = null
}