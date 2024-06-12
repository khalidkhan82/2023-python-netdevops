resource "aws_vpc" "first-test-vpc" {
  cidr_block = "10.128.0.0/22"
  tags = {
    name = "test-vpc"
  }
}