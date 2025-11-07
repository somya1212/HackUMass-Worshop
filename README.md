# HackUMass-Worshop
Build and deploy your first project on the AWS Free Tier
# Quote of the Day — Serverless on AWS (Free Tier)

A minimal, beginner-friendly **serverless** app:
- **DynamoDB** stores quotes
- **Lambda** picks a random quote
- **API Gateway** exposes a `/quote` endpoint
- **S3** hosts a tiny web page

Perfect for hackathons and workshops.

## Architecture
S3 (front-end) → API Gateway (waiter) → Lambda (chef) → DynamoDB (kitchen)



## 1) DynamoDB (create table)
- Table name: `QuotesTable`
- Partition key: `id` (String)
- Add items (example):
  - `{ "id": "1", "quote": "Stay curious." }`
  - `{ "id": "2", "quote": "Build, break, learn, repeat." }`
  - `{ "id": "3", "quote": "Sleep is for after the demo." }`

## 2) Lambda (Python)
Create function `GetRandomQuote` (Python 3.x). Paste `lambda/get_random_quote.py` and deploy.

### IAM permissions
Attach either **AmazonDynamoDBReadOnlyAccess** to the Lambda role,
or use `infra/iam-QuotesTableReadOnly.json` as an inline policy (update region/account if needed).

## 3) API Gateway (HTTP API)
- Create HTTP API
- Integration: Lambda → `GetRandomQuote`
- Route: `GET /quote`
- Enable CORS (Allowed origin `*`, methods `GET`)

Note your **Invoke URL** (e.g. `https://abc123.execute-api.us-east-1.amazonaws.com/quote`)

## 4) S3 Static Website
- Create S3 bucket (unique name). Uncheck “Block all public access”
- Enable **Static website hosting** → index `index.html`
- Add a bucket policy to allow public read of objects
- Edit `frontend/index.html` → set `const API = "<your api>/quote"`

Open your bucket **Website endpoint** to view the app.

## Troubleshooting
- **403 on S3**: public access blocked or bucket policy missing
- **CORS error**: enable CORS in API Gateway
- **Empty quote**: ensure items in DynamoDB have `quote` attribute (string)

## Credits
Built for HackUMass workshop by **Somya Bharti**. MIT licensed.
