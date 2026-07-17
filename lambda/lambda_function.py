import json
import boto3
from datetime import datetime

# AWS Clients
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

# Change this after creating DynamoDB table
TABLE_NAME = "Employees"

table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):

    print("Received Event:")
    print(json.dumps(event))

    try:

        # S3 Event Details
        bucket = event["Records"][0]["s3"]["bucket"]["name"]
        key = event["Records"][0]["s3"]["object"]["key"]

        print(f"Bucket : {bucket}")
        print(f"File   : {key}")

        # Read uploaded file
        response = s3.get_object(
            Bucket=bucket,
            Key=key
        )

        content = response["Body"].read().decode("utf-8")

        employees = json.loads(content)

        processed = []

        for emp in employees:

            item = {

                "id": str(emp["id"]),

                "name": emp["name"].title(),

                "department": emp["department"].upper(),

                "salary": int(emp["salary"]),

                "processed_at": datetime.utcnow().isoformat()

            }

            table.put_item(Item=item)

            processed.append(item)

        return {

            "statusCode": 200,

            "body": json.dumps({

                "message": "Processing Completed",

                "records_processed": len(processed)

            })

        }

    except Exception as e:

        print("ERROR :", str(e))

        return {

            "statusCode": 500,

            "body": json.dumps({

                "error": str(e)

            })

        }
