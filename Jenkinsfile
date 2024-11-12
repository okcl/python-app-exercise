pipeline {
    agent any
    
    // Add environment variables for Python
    environment {
        PATH = "/usr/local/bin:/usr/bin:/bin:${env.PATH}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                // This will check out your repository
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                // Create and activate virtual environment
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install virtualenv
                    python3 -m virtualenv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run tests inside virtual environment
                sh '''
                    . venv/bin/activate
                    python -m pytest test_app.py -v
                '''
            }
        }
    }
    
    post {
        always {
            // Clean up virtual environment
            cleanWs()
        }
    }
}
