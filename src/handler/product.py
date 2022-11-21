import boto3

from src.service.dynamo.product import ProductService

dynamodb_client = boto3.client('dynamodb')


def lambda_handler(event, context):
    # set dummy product values
    product = {
        "ID": "prid_0001",
        "name": "test_proeuct"
    }
    service = ProductService()
    response = service.create_product(product)
    print(response)
    return response
