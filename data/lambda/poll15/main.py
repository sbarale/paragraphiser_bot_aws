import os
import pprint as pp
import boto3
from boto3.dynamodb.conditions import Key, Attr
import time
import json
import common
import scheduling

def lambda_handler(event,contex):
    if ('unitTest' in event) and event['unitTest']:
        print('Running unit tests')
        return(common.unit_tests())
    else:
        print('Running main (non-test) handler')
        return(check_latest_batch(event))

def check_latest_batch(event):
    scheduling.fetch_15()
    print('Finished moving the latest batch of checks from dynamo to SQS')