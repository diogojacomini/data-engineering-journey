terraform {
  required_version = ">= 1.3.9"
}

provider "aws" {
  region = "us-east-2"

  default_tags {
    tags = local.tags_projec
  }
}

