provider "aws" {
  profile    = "buildyourjazz"
  region     = var.aws_region
}


module "lambda_function_with_vpc" {
  source = "terraform-aws-modules/lambda/aws"

  create_role   = true
  attach_cloudwatch_logs_policy = true
  attach_policy = false
  attach_network_policy = false
  store_on_s3 = true

  function_name = "s3-redshift-copy"
  description   = "deployed by terraform"
  handler       = "copy_to_redshift.lambda_handler"
  runtime       = "python3.7"

  source_path = "s3_redshift_lambda"
  lambda_role = var.lambda_role
  s3_bucket   = var.s3_bucket
  timeout = 900


  tags = {
    Name = "s3-redshift-copy"
  }
}