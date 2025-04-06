TRN Jenkins CI/CD Setup Guide

Prerequisites
Before you start, ensure the following:

1. Install Docker

2. Ensure TRN Database is set up and SQL Server is installed and running

3. Run Docker with provided file
docker build -t trn-jenkins .
docker run -d -p 8080:8080 trn-jenkins

4. Verify Docker Image is Running
Ensure that your Docker container is running and accessible. You can check this by opening your browser and navigating to http://localhost:8080.

5. Login to Jenkins
Open Jenkins in your browser (http://localhost:8080).

6. Set Up Jenkins Environment Variables
In Jenkins, make sure the following environment variables are configured for use in your pipelines:

DB_SERVER: The server address of your SQL Server instance
DB_USER: The username for the database 
DB_PASSWORD: The password for the database 

7. Get and add credentials to the git repo to be able to post. 

8. Follow branching strategy while adding changess:

main: Stable production releases.
develop: Ongoing development (features are merged here).
feature/: For developing new features.
bugfix/: For minor fixes or patches (merged into develop).
release/: For stabilizing pre-production builds (before merging into main).
hotfix/: For urgent production fixes.
support/: For long-term support branches if needed.
