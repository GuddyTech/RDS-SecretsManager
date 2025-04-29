#!/bin/bash

# Set your secret name
SECRET_NAME="guddy-mysql-secret"

# Fetch secret from AWS Secrets Manager
secret=$(aws secretsmanager get-secret-value --secret-id "$SECRET_NAME" --query 'SecretString' --output text)

# Parse username and password
username=$(echo "$secret" | jq -r .username)
password=$(echo "$secret" | jq -r .password)

# Connect to MySQL
mysql -h guddy-pub-db.cr8oumgm6psr.us-east-1.rds.amazonaws.com -P 3306 -u "$username" -p"$password"
