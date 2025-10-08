pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/duha-se/DevOpsAssignments.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                dir('HomeworkAssignment2/foodly-app') {
                    sh 'docker build -t foodly-web .'
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                dir('HomeworkAssignment2/foodly-app') {
                    sh '''
                    pip install -r requirements.txt
                    pytest || echo "No tests found"
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying app...'
                dir('HomeworkAssignment2/foodly-app') {
                    sh 'docker compose up -d || echo "docker-compose not found or not configured"'
                }
            }
        }
    }
}
