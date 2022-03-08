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

        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Push') {
			steps {
				sh 'echo $DOCKER_LOGIN_PSW | docker login -u $DOCKER_LOGIN_USR --password-stdin'
                sh 'docker-compose push'
			}
		}
    
        stage('Deploy') {
            steps {
                sh 'scp docker-stack.yml bishal@10.0.1.5:'
                sh """ssh -tt bishal@10.0.1.5 << ENDSSH
                    docker stack deploy --compose-file docker-stack.yml webapp
                    exit
                    ENDSSH"""
            }
        }

        stage('Nginx load balancer') {
            steps{
                sh """scp nginx.conf bishal@10.0.1.8:
                ssh bishal@10.0.1.8 'docker rm -f nginx'
                ssh bishal@10.0.1.8  'docker run -d -p 80:80 --name nginx --mount type=bind,source=/home/bishal/nginx.conf,target=/etc/nginx/nginx.conf nginx'
                """
            }
        }

    }
    
	post {
		always {
			sh 'docker logout'
		}   
	}
}