provider "aws" {
    region  = "eu-west-1"
}

resource "aws_instance" "palo-1" {
    ami           = "ami-004b0f608ba7894d6"
    instance_type = "t2.micro"
    subnet_id = "subnet-000fe206f7958b8dd"
    }
