resource "aws_instance" "test-instance" {
  ami           = "ami-0551ce4d67096d606"
  instance_type = "t2.micro"
  subnet_id = "subnet-00f37d21ab2137f78"
  key_name = "zero_key_pair"

  tags = {
    Name = "MyFirstInstance"
  }
}