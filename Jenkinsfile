pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-flask-app'
        //AWS_ECR_REPO = 'your-aws-account-id.dkr.ecr.your-region.amazonaws.com/my-flask-app'
        //AWS_REGION = 'your-region'
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
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run --rm %DOCKER_IMAGE% python -m pytest'
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
