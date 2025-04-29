# RDS-SecretsManager
Connecting to MySql Database with Secrets Manager

To run the script that retrieves credentials from AWS Secrets Manager and uses them to log in to your MySQL RDS instance, follow these steps:
✅ Pre-requisites
Make sure these tools are installed and configured:
1. AWS CLI (with credentials/config set up)
2. jq (to parse JSON)
3. MySQL client

You can install them with:
```
# AWS CLI
sudo apt install awscli -y

# jq
sudo apt install jq -y

# MySQL client
sudo apt install mysql-client -y
```
4. Check the status of the MySQL service:
```
sudo systemctl status mysql
```
You should see something like `active (running)`.
Also, ensure you're authenticated (e.g., aws configure or using an EC2 IAM role or environment variables).

# Option 1: Run it directly in the terminal
Just paste each line one-by-one into your terminal:
```
# 1. Get the secret JSON
secret=$(aws secretsmanager get-secret-value --secret-id <your-secret-name> --query 'SecretString' --output text)

# 2. Extract username and password
username=$(echo "$secret" | jq -r .username)
password=$(echo "$secret" | jq -r .password)

# 3. Connect to MySQL
mysql -h guddy-pub-db.cr8oumgm6psr.us-east-1.rds.amazonaws.com -P 3306 -u "$username" -p"$password"

```
Replace <your-secret-name> with your actual AWS Secrets Manager secret name (e.g., guddy-mysql-secret).

# Option 2: Save it as a script file
1. Create a file:
   ```
   nano connect-to-rds.sh
   ```
2. Paste this content into the file:
   ```
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
   ```

3. Save and exit (Ctrl + O, Enter, Ctrl + X)
4. Make it executable:
   ```
   chmod +x connect-to-rds.sh
   ```
5. Run it:
   ```
   ./connect-to-rds.sh
   ```
# How To Retrieve Secrets using AWS CLI, then connect
```
# 1. Get the secret from Secrets Manager (replace <secret-name> with your actual secret name)
aws secretsmanager get-secret-value --secret-id <secret-name> --query 'SecretString' --output text
```
This will return a JSON string like:
```
{"username":"admin","password":"yourpassword"}
```

# For a normal connection with username and Password:
```
mysql -h your-rds-endpoint.amazonaws.com -P 3306 -u your_username -p
```

## For the python file `connect-to-rds.py`, you can run it with
```
python3 connect-to-rds.py
```
This was gotten from Secrets Manager `Sameple Code` in AWS

