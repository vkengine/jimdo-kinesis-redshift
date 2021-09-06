variable "s3_bucket" {
  default = "jimdo-lambda-package-bucket"
}

variable "lambda_role" {
  default = "arn:aws:iam::151495987564:role/lambda_role"
}

variable "aws_region" {
  default = "eu-central-1"
}