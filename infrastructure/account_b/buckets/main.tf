provider "aws" {
  profile = "default"
  region  = var.bucket_region
}

resource "aws_s3_bucket" "jimdo_lambda_bucket" {
  bucket = var.lambda_package_bucket_name
  acl = "private"
  force_destroy = true
}