pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m playwright install chromium'
            }
        }

        stage('Run UI tests') {
            steps {
                bat 'echo JENKINSFILE DEBUG VERSION'
                bat 'echo Workspace: %WORKSPACE%'
                bat 'dir'
                bat 'dir /s /b laptop_cart.py'

                bat 'if not exist reports mkdir reports'
                bat 'python -m pytest -v test_laptop_cart.py --junitxml=reports/junit.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
        }
    }
}
