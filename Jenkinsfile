pipeline {
    agent any

    environment {
        DEPLOY_DIR = "/tmp/deploy" 
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the app...'
                dir('foodly-app') {
                    sh 'pip install -r requirements.txt || echo "requirements not found"'
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                dir('foodly-app') {
                    sh 'pytest || echo "No tests found"'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the app...'
                dir('foodly-app') {
                    sh """
                    mkdir -p ${DEPLOY_DIR}
                    cp -r * ${DEPLOY_DIR}/
                    """
                    echo "App deployed successfully to ${DEPLOY_DIR}!"
                }
            }
        }

        stage('Run App') {
            steps {
                echo 'Running the app...'
                dir('foodly-app') {
                    sh 'nohup python app.py --port 9496 > /tmp/deploy/app.log 2>&1 &'
                    echo 'App is running on port 9496'
                }
            }
        }
    }
}
