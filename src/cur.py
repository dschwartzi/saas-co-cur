import os
import boto3
import botocore

import pandas as pd
import awswrangler as wr

from functools import partial, reduce

MAX_WORKERS = int(os.environ.get('MAX_WORKERS', '32'))
client_config = botocore.config.Config(max_pool_connections=MAX_WORKERS)

#####################

def assume_role(**params):
    account_id = params.get('accountId')
    role_name = params.get('roleName')
    session_name = params.get('sessionName')
    role_arn = f'arn:aws:iam::{account_id}:role/{role_name}'
    try:
        sts = boto3.client('sts', config=client_config)
        assumed_role = sts.assume_role(RoleArn=role_arn, RoleSessionName=session_name)
        credentials = assumed_role.get('Credentials')
    except:
        print(account_id, 'Assume error')
        credentials = None
    if credentials:
        region = params.get('region','us-east-1')
        return boto3.session.Session(
            region_name=region,
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"]
        )

#####################

def athena(session, db, query):
    return partial(wr.athena.read_sql_query,
                   database=db,
                   boto3_session=session)(query)
