import json
import boto3
from boto3.dynamodb.conditions import Attr
from decimal import Decimal

# DynamoDB Resource
dynamodb = boto3.resource("dynamodb")

# DynamoDB Table Name
TABLE_NAME = "Employees"

table = dynamodb.Table(TABLE_NAME)


# Convert Decimal to int/float for JSON
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            if obj % 1 == 0:
                return int(obj)
            return float(obj)
        return super().default(obj)


def lambda_handler(event, context):

    try:

        response = table.scan()

        items = response.get("Items", [])

        # Sort by Employee ID
        items = sorted(items, key=lambda x: int(x["id"]))

        return {

            "statusCode": 200,

            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "*"
            },

            "body": json.dumps(items, cls=DecimalEncoder)

        }

    except Exception as e:

        return {

            "statusCode": 500,

            "headers": {
                "Access-Control-Allow-Origin": "*"
            },

            "body": json.dumps({

                "message": "Failed to fetch records",

                "error": str(e)

            })

        }
