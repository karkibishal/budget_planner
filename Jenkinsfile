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
//            steps {
//                sh 'docker-compose build'
//            }
//        }

//        stage('Push') {
//			steps {
//				sh 'echo $DOCKER_LOGIN_PSW | docker login -u $DOCKER_LOGIN_USR --password-stdin'
//                sh 'docker-compose push'
//			}
//		}
    
        stage('Ssh to manager') {
            steps {
                script {
                    def remote = [:]
                    remote.name = 'master'
                    remote.host = '10.0.1.5'
                    remote.knownHosts = '.ssh/known_hosts'

                    withCredentials([sshUserPrivateKey(credentialsId: 'SSH_USER', keyFileVariable: 'identity', passphraseVariable: '', usernameVariable: 'userName')]) {
                        remote.user = userName
                        remote.identityFile = identity
                        
                        sshCommand remote: remote, command: "ls -l"
                        sshPut remote: remote, from: 'docker-stack.yml', into: '.'
                        sshCommand remote: remote, command: "docker stack rm webapp"
                        sshCommand remote: remote, command: "docker stack deploy --compose-file docker-stack.yml webapp"
                    }
                }
            }
        }
    }
    
//	post {
//		always {
//			sh 'docker logout'
//		}   
//	}
}