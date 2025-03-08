import json
import boto3


client = boto3.client('lambda')

def mapped_func(i):
    msg = 'writing user nrow:{}'.format(i)
        
    response = client.invoke(
        FunctionName='datafaker3-DataFaker3Function-htLUDYPjNi2X',
        InvocationType='Event')
     
    return response

def lambda_handler(event, context):

    nrows=int(event["nrows"])

    result = list(map(mapped_func, range(nrows)))
    msg = f'{len(result)} objects added'
    return msg
