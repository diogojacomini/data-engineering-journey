resource "aws_s3_bucket" "coinmarket" {
  bucket = local.bucker_name
}
resource "aws_s3_bucket" "coinmarket_raw" {
  bucket = "coin-market-raw"
}