# How To Install AWS CLI In A New Server
## Using the AWS CLI version 2 installer:
1. Update the Server
   ```
   sudo apt update
   ```
2. Download the installer: Use the `curl` command to download the AWS CLI v2 installer
    ```
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    ```
3. Unzip the package:
    ```
    unzip awscliv2.zip
    ```
    - If Unzip is not found:
      ```
      Sudo apt install unzip
      ```
4. Run the install script:
    ```
    sudo ./aws/install
    ```
5. Verify the installation:
    ```
    aws --version
    ```
    
## Using Snap package manager (AWS CLI version 2):
1. Install Snap: If you don't have Snap, install it using:
   ```
   sudo apt update
   sudo apt install snapd
   ```
2. Install the AWS CLI:
   ```
   sudo snap install aws-cli
   ```
   
## Using apt package manager (AWS CLI version 1):
1. Update the package list:
   ```
   sudo apt update
   ```
2. Install the AWS CLI:
   ```
   sudo apt install awscli
   ```
3. Verify the installation:
   ```
   aws --version
   ```
