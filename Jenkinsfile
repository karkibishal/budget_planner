pipeline {
    environment {
        DOCKER_LOGIN = credentials('DOCKER_LOGIN')
        DOCKER_REGISTRY = "bishal86/budget_planner"
        DB_LOGIN = credentials('DB_LOGIN')
        SECRET_KEY = credentials('SECRET_KEY')
    }

    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}