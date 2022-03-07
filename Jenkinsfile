pipeline {
    environment {
        DOCKER_LOGIN = credentials('DOCKER_LOGIN')
        DOCKER_REGISTRY = "bishal86/budget_planner"
        DB_LOGIN = credentials('DB_LOGIN')
        DB_USER = "$DB_LOGIN_USR"
        DB_PASSWORD = "$DB_LOGIN_PSW"
        DB_HOST = credentials('DB_HOST')
        DB_PORT = credentials('DB_PORT')
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