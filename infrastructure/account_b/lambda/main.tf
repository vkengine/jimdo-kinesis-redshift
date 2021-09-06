provider "aws" {
  profile    = "default"
  region     = var.aws_region
}


module "lambda_function_with_vpc" {
  source = "terraform-aws-modules/lambda/aws"

  create_role   = false
  attach_cloudwatch_logs_policy = false
  attach_policy = false
  attach_network_policy = false
  store_on_s3 = true

  function_name = "trigger_realtime_email_dag"
  description   = "deployed by terraform"
  handler       = "trigger_realtime_successful_sync.lambda_handler"
  runtime       = "python3.8"

  source_path = "sync_lambda"
  lambda_role = var.lambda_role
  s3_bucket   = var.s3_bucket
  timeout = 900


  tags = {
    Name = "trigger_realtime_email_dag"
  }
}