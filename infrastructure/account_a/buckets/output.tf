output "user_event_bucket_arn" {
  description = "ARN user event bucket"
  value = aws_s3_bucket.user_event_bucket.arn
}

output "user_utm_bucket_arn" {
  description = "ARN user utm bucket"
  value = aws_s3_bucket.user_utm_bucket.arn
}