pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m playwright install chromium'
            }
        }

        stage('Debug workspace') {
            steps {
                bat 'echo Workspace: %WORKSPACE%'
                bat 'cd'
                bat 'dir'
                bat 'dir /s /b laptop_cart.py'
            }
        }

        stage('Run UI tests') {
            steps {
                bat 'if not exist reports mkdir reports'
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
