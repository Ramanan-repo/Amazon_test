pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m playwright install chromium'
            }
        }

        stage('Find test file') {
            steps {
                bat 'echo JENKINSFILE DEBUG VERSION'
                bat 'echo Workspace: %WORKSPACE%'
                bat 'dir'
                bat 'where /r "%WORKSPACE%" laptop_cart.py'
            }
        }

        stage('Run UI tests') {
            steps {
                bat 'if not exist reports mkdir reports'

                // Change this path if the search finds the file in a subfolder.
                bat 'python -m pytest -v laptop_cart.py --junitxml=reports/junit.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
        }
    }
}