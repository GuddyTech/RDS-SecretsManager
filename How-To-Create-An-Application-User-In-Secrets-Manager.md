# How To Create An Application User in DB and Authenticate with Secrets Manager
After creating the `RDS` e.g `MySQL` database in a `Private Subnet`, create a `Bastion Host` to be able to access it

1. Connect to bastion host
2. Use the bastion host to connect to RDS as `dbadmin`
   - To show databases(If you're unsure of the DB name)
     ```
     SHOW DATABASES;
     ```
     e.g:
     ```
     mysql> SHOW DATABASES;
     ```
   - To connect to database(Switch to the target database)
     ```
     USE your_database_name;
     ```
3. Issue an `SQL Statement` to Create the application user with a strong password
   ```
   CREATE USER 'myapp_user'@'%' IDENTIFIED BY 'YourStrongPassword123!';
   ```
4. Grant necessary privileges to the new user (adjust as needed)
   ```
   GRANT ALL PRIVILEGES ON your_database_name.* TO 'myapp_user'@'%';
   ```
5. Apply the changes
   ```
   FLUSH PRIVILEGES;
   ```

# 🔐 Notes:
Replace `your_database_name` with the actual DB name.

Replace `myapp_user` and `YourStrongPassword123!` with your desired username and password.

`%` means the user can connect from any host (ok if you're using VPC/SG restrictions).

Use least privilege if `ALL PRIVILEGES` is too broad (e.g., use `SELECT, INSERT` instead).

6. Add new `DB user` to `AWS Secrets Manager` manually
     ```
     {
      "username": "myapp_user",
      "password": "YourStrongPassword123!",
      "engine": "mysql",
      "host": "<your-rds-endpoint>",
      "port": 3306,
      "dbname": "your_database_name"
     }
    ```
     - Credentials for Amazon RDS database
     - Username
     - Password
     - Encryption Key
     - Database
     - Secret Name (This will be used in the script)
     - Description
     - Configure Rotation
     - Store
7. Have the application connect to Secrets Manager to retrieve our new application user credentials
   - Make sure your app is referencing the correct secret name/ARN.
8. Test the Application
    - Test Manually from Bastion
      ```
      mysql -h <rds-endpoint> -u myapp_user -p
      ```
      This confirms the user was created and has correct access.

9. Use script to connect easily to the `db` with the Secrets Manager Credential.

    See: <a href=./connect-to-rds.py> connect-to-rds using python3 </a> or <a href=./connect-to-rds.sh> connect-to-rds using bash </a>
