provider "aws" {
  profile = "default"
  region  = var.stream_region
}


resource "aws_kinesis_firehose_delivery_stream" "user_event_stream" {
  name        = "kinesis-firehose-user-event-stream"
  destination = "s3"

  s3_configuration {
    role_arn   = var.kinesis_role
    bucket_arn = var.user_event_bucket_arn
  }
}


resource "aws_kinesis_firehose_delivery_stream" "user_utm_stream" {
  name        = "kinesis-firehose-user-utm-stream"
  destination = "s3"

  s3_configuration {
    role_arn   = var.kinesis_role
    bucket_arn = var.user_utm_bucket_arn
  }
}