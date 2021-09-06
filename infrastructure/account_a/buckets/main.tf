provider "aws" {
  profile = "default"
  region  = var.bucket_region
}

resource "aws_s3_bucket" "user_event_bucket" {
  bucket = var.user_event_bucket_name
  acl    = "private"
  force_destroy = true
}

resource "aws_s3_bucket" "user_utm_bucket" {
  bucket = var.user_atm_account_name
  acl    = "private"
  force_destroy = true
}