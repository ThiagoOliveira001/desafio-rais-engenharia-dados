resource "aws_s3_bucket" "datalake" {
  bucket = "${var.base_datalake_bucket_name}-${var.environment}-${var.account}"

  tags = {
    IES   = "IGTI",
    CURSO = "EDC"
  }
}

resource "aws_s3_bucket_acl" "acl_datalake" {
  bucket = aws_s3_bucket.datalake.bucket
  acl    = "private"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "encrypt_datalake" {
  bucket = aws_s3_bucket.datalake.bucket

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "block_public_datalake" {
  bucket = aws_s3_bucket.datalake.bucket

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}