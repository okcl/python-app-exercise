pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/okcl/python-app-exercise'
            }
        }
        stage('Setup') {
            steps {
                sh 'python3 -m pip install pytest'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest test_app.py'
            }
        }
    }
}
