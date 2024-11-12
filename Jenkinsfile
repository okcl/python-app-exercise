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
                // Alternative Method 2: Using pyenv (if Method 1 doesn't work)
                sh '''
                    # Install pyenv if not already installed
                    curl https://pyenv.run | bash
                    
                    export PATH="$HOME/.pyenv/bin:$PATH"
                    eval "$(pyenv init -)"
                    
                    # Install Python version you want
                    pyenv install 3.9.0
                    pyenv global 3.9.0
                    
                    # Create and activate virtual environment
                    python -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    
                    # Install requirements
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
