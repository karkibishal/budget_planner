pipeline {
    environment {
        DOCKER_LOGIN = credentials('DOCKER_LOGIN')
        DB_LOGIN = credentials('DB_LOGIN')
        DB_USER = "$DB_LOGIN_USR"
        DB_PASSWORD = "$DB_LOGIN_PSW"
        DB_HOST = credentials('DB_HOST')
        DB_PORT = credentials('DB_PORT')
        SECRET_KEY = credentials('SECRET_KEY')
    }

    agent any
    stages {

//        stage('Build') {
 //           steps {
 //               sh 'docker-compose build'
 //           }
 //       }

        stage('Push') {
			steps {
				sh 'echo $DOCKER_LOGIN_PSW | docker login -u $DOCKER_LOGIN_USR --password-stdin'
                sh 'docker-compose push'
			}
		}
    }
    
	post {
		always {
			sh 'docker logout'
		}   
	}
}