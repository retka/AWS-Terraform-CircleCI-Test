resource "aws_dynamodb_table" "compatibility" {
    name         = "${var.env}-compatibility"
    billing_mode = "PAY_PER_REQUEST"
    hash_key     = "PK"

    attribute {
        name = "PK"
        type = "S"
    }
}
