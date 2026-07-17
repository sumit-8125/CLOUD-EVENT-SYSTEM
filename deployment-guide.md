# Cloud Event-Driven Data Processing System

## AWS Services Used

- Amazon EC2
- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon API Gateway

---

## Deployment Steps

### 1. Create DynamoDB Table

Table Name:
Employees

Partition Key:
id (String)

---

### 2. Create S3 Bucket

Bucket Name:
cloud-event-system-sumit-8125

Upload employees.json

---

### 3. Create Lambda Function

Function Name:
ProcessEmployeeData

Configure an S3 Trigger.

---

### 4. Create Second Lambda

Function Name:
get_employees

Attach DynamoDB permissions.

---

### 5. Create API Gateway

HTTP API

Route:
GET /employees

Integration:
get_employees

---

### 6. Launch EC2

Install Apache.

Copy:

- index.html
- style.css
- script.js

to

/var/www/html

Restart Apache.

---

### 7. Update script.js

Replace API_URL with your API Gateway Invoke URL.

---

### 8. Test

Upload employees.json to S3.

Verify:

- Lambda executes automatically.
- Data appears in DynamoDB.
- API returns JSON.
- Website displays employee data.
