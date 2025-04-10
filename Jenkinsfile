pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-flask-app'
        //AWS_ECR_REPO = 'your-aws-account-id.dkr.ecr.your-region.amazonaws.com/my-flask-app'
        //AWS_REGION = 'your-region'
        DOCKER_HOST = 'npipe:////./pipe/docker_engine'
    }

    stages {
        stage('Checkout Repo') {
            steps {
                git branch: 'main', credentialsId: 'Github', url: 'https://github.com/Kshitija0110/End-to-end-CICD-pipeline.git'
                bat 'echo Listing files in the repo:'
                bat 'dir /s'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Use --no-cache option for the build
              bat 'docker build --no-cache -t my-flask-app .'
        
             // Use -f or --force flag to bypass the confirmation prompt
              bat 'docker system prune -a --volumes -f'
            }
        }

        // stage('Test') {
        //     steps {
        //         bat 'docker run --rm %DOCKER_IMAGE% python -m pytest'
        //     }
        // }

        stage('Run Locally') {
            steps {
                // Stop any existing container with the same name
                // bat 'docker stop my-flask-app || true'
                // bat 'docker rm my-flask-app || true'
                
                // Run the container locally on port 5000
                bat 'docker run -d -p 5000:5000 --name my-flask-app %DOCKER_IMAGE%'
                
                // Print a message to the console
                echo 'Application is now running locally at http://localhost:5000'
            }
        }

        // stage('Push to ECR') {
        //     steps {
        //         withCredentials([aws(credentialsId: 'aws-credentials', region: env.AWS_REGION)]) {
        //             bat 'aws ecr get-login-password --region %AWS_REGION% | docker login --username AWS --password-stdin %AWS_ECR_REPO%'
        //             bat 'docker tag %DOCKER_IMAGE% %AWS_ECR_REPO%:latest'
        //             bat 'docker push %AWS_ECR_REPO%:latest'
        //         }
        //     }
        // }

        // stage('Deploy to EC2') {
        //     steps {
        //         withCredentials([aws(credentialsId: 'aws-credentials', region: env.AWS_REGION)]) {
        //             // Deploy to EC2 using AWS CLI
        //             bat 'aws ec2 describe-instances --filters "Name=tag:Name,Values=flask-app-server" --query "Reservations[].Instances[].InstanceId" --output text > instance.txt'
        //             bat 'aws ssm send-command --document-name "AWS-RunShellScript" --targets "Key=instanceids,Values=$(type instance.txt)" --parameters "commands=[\"docker pull %AWS_ECR_REPO%:latest\", \"docker stop flask-app || true\", \"docker rm flask-app || true\", \"docker run -d -p 80:5000 --name flask-app %AWS_ECR_REPO%:latest\"]"'
        //         }
        //     }
        // }
    }
}
