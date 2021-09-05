output "s3_access_policy_arn" {
  description = "ARN of s3 policy"
  value = aws_iam_policy.s3_full_access.arn
}
