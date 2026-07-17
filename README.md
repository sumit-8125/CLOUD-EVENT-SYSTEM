# Cloud Event Driven Data Processing System

## Overview

This project demonstrates an event-driven cloud architecture using AWS services.

Whenever a new JSON file is uploaded to Amazon S3, an event automatically triggers an AWS Lambda function. The Lambda function processes the uploaded data and stores the transformed records inside Amazon DynamoDB.

A web application hosted on an EC2 instance fetches the processed records through API Gateway and displays them dynamically.

---

## AWS Services Used

- Amazon EC2
- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon API Gateway
- IAM

---

## Workflow

User Uploads JSON

↓

Amazon S3

↓

S3 Event Trigger

↓

AWS Lambda

↓

Amazon DynamoDB

↓

API Gateway

↓

EC2 Hosted Website

---

## Features

- Fully Automated Workflow
- Event Driven Architecture
- Serverless Processing
- Responsive Dashboard
- Dynamic Data Loading
- Cloud Native Services Only

---

## Folder Structure

cloud-event-system

lambda/

website/

sample-data/

architecture/

docs/

README.md

deployment-guide.md

---

## Technologies

- HTML
- CSS
- JavaScript
- Python
- AWS Cloud

---

