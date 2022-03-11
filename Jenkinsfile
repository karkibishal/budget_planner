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

        stage('Setup') {
            steps {
                sh """sudo apt install python3-venv -y 
                python3 -m venv venv
                . ./venv/bin/activate
                pip3 install -r requirements.txt
                """
                }
        }

        stage('Test') {
            steps {
                sh """ . ./venv/bin/activate
                coverage run tests.py
                coverage xml
                deactivate
                rm -rf /venv""" 
            }
        }

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

        stage('Test results') {
            steps{
                cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
                archiveArtifacts artifacts: '*.xml', followSymlinks: false
            }
        }

    }
    
	post {
		always {
			sh 'docker logout'
		}   
	}
}