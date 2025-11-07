import boto3, random, json
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('QuotesTable')

def lambda_handler(event, context):
    resp = table.scan(ProjectionExpression="#q, id", ExpressionAttributeNames={"#q":"quote"})
    items = resp.get('Items', [])
    if not items:
        return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps({"quote":"(no quotes yet)"})}
    quote = random.choice(items)
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(quote)
    }
