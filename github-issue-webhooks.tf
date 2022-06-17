resource "aws_api_gateway_rest_api" "webhooks" {
    name = "${var.env}-Ryujinx-Compatibility-List-Webhooks"
    
    endpoint_configuration {
      types = ["REGIONAL"]
    }
}
