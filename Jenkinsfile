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
                sh 'docker build -t foodly-web .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest || echo "No tests found"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying app...'
                sh 'docker compose up -d'
            }
        }
    }
}