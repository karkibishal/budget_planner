pipeline {
    agent any
    environment {
        SECRET_KEY = credentials('SECRET_KEY')
//        DATABASE_URI = credentials('DATABASE_URI')
        DOCKER_LOGIN = credentials('DOCKER_LOGIN')
        DB_LOGIN = credentials('DB_LOGIN')
        APP_RUN = 'True'
    }

// This stage creates virtual environment for the python container
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

// This stage runs unit tests and saves them to files to be picked up post build 
//        stage('Test') {
//            steps {
//                sh """ . ./venv/bin/activate
//                python3 -m pytest --junitxml unittests.xml
//                python3 -m pytest --cov-report xml:coverage.xml --cov=tests/""" 
//            }
//        }

// This stage builds the two containers and pushes to docker hub
        stage('build and push') {
            steps {
                withCredentials([string(credentialsId: 'SQLPWD', variable: 'password')]) {

                sh """echo $DOCKER_LOGIN_PSW | docker login -u $DOCKER_LOGIN_USR --password-stdin
                docker build -t bishal86/budget_planner .
                docker push bishal86/budget_planner
                """
                }
            }
        }

// This stage copies a compose file into the manager node sshs into manager node of swarm and sets up the docker stack
//        stage('deploy') {
 //           steps {
 //               sh """scp scripts/docker-compose.yml jenkins@10.0.0.13:
 //               ssh jenkins@10.0.0.13 'docker stack deploy --compose-file docker-compose.yml webapp'
 //               """
 //           }
 //       }
// This stage copies a conf file into the vm, sshs into the vm and sets up a load balancer with a nginx server
        // stage('create nginx load balancer'){
        //     steps{
        //         sh """cps  scripts/nginx.conf jenkins@GETAVMWITHIPADDRESS!
        //         ssh jenkins@GETANIP!  'docker run -d -p 80:80 --name nginx --mount type=bind,source=${pwd}/nginx.conf,target=/etc/nginx/nginx.conf nginx'
        //         """
        //     }
        // }
    
//        stage('post build - test results') {
//            steps{
//                junit 'unittests.xml'
//                cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
//archiveArtifacts artifacts: '*.xml', followSymlinks: false
                
//            }
//        }
    }   
}