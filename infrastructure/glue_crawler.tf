resource "aws_glue_crawler" "rais_crawler" {
  database_name = "igti_rais"
  name          = "processando_dados_rais"
  role          = aws_iam_role.glue_role.arn

  s3_target {
    path = "s3://datalake-igti-staging-579937625472/consume-zone/rais/"
  }
}