output "kinesis_role_arn" {
  description = "Role created for kinesis"
  value = aws_iam_role.firehose_role.arn
}


output "kinesis_role_name" {
  description = "Role created for kinesis"
  value = aws_iam_role.firehose_role.name
}
