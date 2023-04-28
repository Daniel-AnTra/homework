pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python -m pip install argparse'
            }
        }
        stage('Test') {
            steps {
                sh 'python your_script.py'
            }
        }
    }
}
