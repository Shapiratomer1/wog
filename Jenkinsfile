pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                powershell 'docker-compose build'
            }
        }
        stage('Run') {
            steps {
                powershell 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                powershell 'python tests/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                powershell 'docker-compose down'
                powershell 'docker tag flask-scores-app shapiratomer/flask-scores-app:latest'
                powershell 'docker push shapiratomer/flask-scores-app:latest'
            }
        }
    }
}
