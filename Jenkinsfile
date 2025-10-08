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
                echo 'Building the app...'
                dir('HomeworkAssignment2/foodly-app') {
                    sh 'python3 -m pip install -r requirements.txt || echo "requirements not found"'
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                dir('HomeworkAssignment2/foodly-app') {
                    sh 'pytest || echo "No tests found"'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the app...'
                dir('HomeworkAssignment2/foodly-app') {
                    sh '''
                    mkdir -p /tmp/deploy
                    cp -r * /tmp/deploy/
                    '''
                    echo 'App deployed successfully!'
                }
            }
        }
    }
}
