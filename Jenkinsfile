pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
	    	sh 'sudo apt-get update'
		sh 'sudo apt-get install -y python3-pip'
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
