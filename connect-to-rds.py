import boto3
import json
import subprocess
from botocore.exceptions import ClientError

def get_secret():
    secret_name = "rds!db-2539d91f-8536-44f9-93c3-e4d2d07d05d0"
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    return json.loads(secret)

def connect_to_mysql():
    creds = get_secret()
    username = creds['username']
    password = creds['password']
    host = creds.get('host', 'guddy-pub-db.cr8oumgm6psr.us-east-1.rds.amazonaws.com')  # default if not in secret
    port = creds.get('port', 3306)

    cmd = [
        "mysql",
        f"-h{host}",
        f"-P{port}",
        f"-u{username}",
        f"-p{password}"
    ]

    subprocess.run(cmd)

if __name__ == "__main__":
    connect_to_mysql()
