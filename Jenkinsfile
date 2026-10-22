pipeline {
    agent any
    
    environment {
        AWS_REGION = 'ap-southeast-2'
        ECR_REPO_NAME = 'my-devops-app'
    }
    
    stages {
        stage('Build Image') {
            steps {
                script {
                    echo "Building Docker Image..."
                    dockerImage = docker.build("${ECR_REPO_NAME}:${env.BUILD_ID}")
                }
            }
        }
        
        stage('Push to ECR') {
            steps {
                script {
                    echo "Authenticating with AWS ECR..."
                    sh """
                    # Dynamically get the AWS Account ID
                    AWS_ACCOUNT_ID=\$(aws sts get-caller-identity --query Account --output text)
                    ECR_URI=\$AWS_ACCOUNT_ID.dkr.ecr.${AWS_REGION}.amazonaws.com
                    
                    # Log in to ECR
                    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin \$ECR_URI
                    
                    # Tag and push the image
                    docker tag ${ECR_REPO_NAME}:${env.BUILD_ID} \$ECR_URI/${ECR_REPO_NAME}:${env.BUILD_ID}
                    docker tag ${ECR_REPO_NAME}:${env.BUILD_ID} \$ECR_URI/${ECR_REPO_NAME}:latest
                    
                    docker push \$ECR_URI/${ECR_REPO_NAME}:${env.BUILD_ID}
                    docker push \$ECR_URI/${ECR_REPO_NAME}:latest
                    """
                }
            }
         }

        stage('Deploy to ECS') {
            steps {
                script {
                    echo "Deploying to ECS Fargate..."
                    sh """
                    aws ecs update-service --cluster my-devops-cluster --service my-devops-service --force-new-deployment --region ${AWS_REGION}
                    """
                }
            }
        }   
        
    }
}
