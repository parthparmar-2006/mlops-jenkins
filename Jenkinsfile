// Scenario 3: project is on GitHub
// Jenkins job -> Pipeline -> Definition: "Pipeline script from SCM"
//   Repository URL: https://github.com/parthparmar-2006/mlops-jenkins.git   Branch: */main
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/parthparmar-2006/mlops-jenkins.git'
            }
        }

        stage('Show Workspace') {
            steps {
                bat 'cd'
            }
        }

        stage('Build Images') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker compose run --rm --no-deps webapp pytest'
            }
        }

        stage('Deploy Containers') {
            steps {
                bat 'docker compose up -d'
            }
        }
    }
}
