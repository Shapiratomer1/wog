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
                powershell 'docker build -t flask-scores-app .'
            }
        }
        stage('Run') {
            steps {
                powershell 'docker run -d -p 8777:8777 --name flask-scores-app -v $(pwd)/scores.txt:/scores.txt flask-scores-app'
            }
        }
        stage('Test') {
            steps {
                powershell 'python tests/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                powershell 'docker stop flask-scores-app'
                powershell 'docker rm flask-scores-app'
                powershell 'docker tag flask-scores-app shapiratomer/flask-scores-app:latest'
                powershell 'docker push shapiratomer/flask-scores-app:latest'
            }
        }
    }
}
