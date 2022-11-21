import boto3


class ProductService:

    def __int__(self):
        self.dynamo = boto3.client('dynamodb')

    def create_product(self, product: dict):
        self.dynamo.put_item(TableName='Product', Item=product)
        return {
          'statusCode': 200,
          'body': 'Successfully Created Product'
        }