provider "aws" {
  profile = "default"
  region = var.policy_region
}

resource "aws_iam_policy" "s3_full_access" {
  name        = "s3_full_access"
  description = "created by terraform"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "s3-firehose-permission-attach" {
  role       = var.kinesis_role_name
  policy_arn = aws_iam_policy.s3_full_access.arn
}