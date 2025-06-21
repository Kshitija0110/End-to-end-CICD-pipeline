pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-flask-app'
        DOCKER_HUB_REPO = 'kshitu/ci_cd-pipeline'
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
                bat 'docker build --no-cache -t my-flask-app .'
        
            
            }
        }

        // stage('Test') {
        //     steps {
        //         bat 'docker run --rm %DOCKER_IMAGE% python -m pytest'
        //     }
        // }
    //     stage('Test') {
    // steps {
    //     // Update Dockerfile CMD temporarily for testing
    //     bat 'echo FROM python:3.9-slim > Dockerfile.test'
    //     bat 'echo WORKDIR /app >> Dockerfile.test'
    //     bat 'echo COPY requirements.txt . >> Dockerfile.test'
    //     bat 'echo RUN pip install --no-cache-dir -r requirements.txt >> Dockerfile.test'
    //     bat 'echo COPY . . >> Dockerfile.test'
    //     bat 'echo EXPOSE 5000 >> Dockerfile.test'
    //     bat 'echo CMD ["python", "app.py"] >> Dockerfile.test'

    //     //remove if exists
    //     //bat 'docker stop my-flask-app-test || true'
    //     // bat 'docker rm my-flask-app-test || true'
        
    //     // Build test image
    //     bat 'docker build -f Dockerfile.test -t my-flask-app-test .'

       //  //remove if exists
       // // bat 'docker rm my-flask-app-test || true'
        
       //  // Run the container in detached mode
       //  bat 'docker run -d -p 5001:5000 --name flask-app-test my-flask-app-test'
        
       //  // Wait a moment for the application to start
       //  // bat 'timeout /t 5'
        
       //  // Test 1: Check if the health endpoint returns correct response
       //  bat 'curl -s http://localhost:5001/ | findstr "LLaMA QA API is running!" || exit 1'
        
       //  // Test 2: Send a simple message to the chat API and verify response format
       //  bat 'curl -s -X POST -H "Content-Type: application/json" -d "{\"message\":\"Hello\"}" http://localhost:5001/api/chat | findstr "response" || exit 1'
        
       //  // Test 3: Check if the main page loads correctly
       //  bat 'curl -s http://localhost:5001/ | findstr "Llama 3 AI Chatbot" || exit 1'
        
       //  // Clean up after tests
//         bat 'docker stop flask-app-test'
//         bat 'docker rm flask-app-test'
//         bat 'docker rmi my-flask-app-test'
//         bat 'del Dockerfile.test'
//     }
// }

        stage('Run Locally') {
            steps {
                // Stop any existing container with the same name
                bat 'docker stop my-flask-app || true'
               bat 'docker rm my-flask-app || true'
                
                // Run the container locally on port 5000
                bat 'docker run -d -p 5000:5000 --name my-flask-app %DOCKER_IMAGE%'
                
                // Print a message to the console
                echo 'Application is now running locally at http://localhost:5000'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                    bat 'docker tag %DOCKER_IMAGE% %DOCKER_HUB_REPO%:latest'
                    bat 'docker push %DOCKER_HUB_REPO%:latest'
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                
       bat '"C:\\Program Files\\Kubernetes\\Minikube\\minikube.exe" start'
            
                bat 'kubectl config use-context minikube'
                bat 'kubectl apply -f deployment.yml'
                
                bat '"C:\\Program Files\\Kubernetes\\Minikube\\minikube.exe" service flask-app-service'
                
                echo 'Application is now deployed to Minikube Kubernetes'
            }
        }

    }
}
