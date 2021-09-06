provider "aws" {
  profile = "buildyourjazz"
  region  = var.region
}


resource "aws_security_group_rule" "example" {
  type              = "ingress"
  from_port         = 0
  to_port           = 65535
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = "sg-fe2e7089"
}