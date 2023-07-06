from __future__ import print_function

import json
import urllib
import boto3
import datetime

print('Loading function...')

def process_refund(message, context):

    print("Recieved message from step Functions:")
    print(message)

    response = {}
    response['TransactionType'] = message['TransactionType']
    response['Message'] = 'Hello from lambda land inside the ProcessRefund function'

    return response