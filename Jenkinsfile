pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh 'git checkout main'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t flask-scores-app .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:8777 --name flask-scores-app -v $(pwd)/Scores.txt:/Scores.txt flask-scores-app'
            }
        }
        stage('Test') {
            steps {
                sh 'python tests/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker stop flask-scores-app'
                sh 'docker rm flask-scores-app'
                sh 'docker tag flask-scores-app shapiratomer/flask-scores-app:latest'
                sh 'docker push shapiratomer/flask-scores-app:latest'
            }
        }
    }
}
