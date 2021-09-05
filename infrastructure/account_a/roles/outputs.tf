output "kinesis_role" {
  description = "Role created for kinesis"
  value = aws_iam_role.firehose_role.arn
}
