pipeline {
    agent none
    stages {
        stage('Docker-build') {
            agent {
                docker { image 'python:3' }
            }
            steps {
                sh 'python --version'
            }
        }
        stage('Running commands on Master Server Trial') {
            agent {
                label {label 'master'}
            }
            steps {
                sh 'docker build -t python_app:$BUILD_NUMBER .'
                sh 'echo "Build Number Is  $BUILD_NUMBER."'
            }
        }

        stage('Running commands on Master Server to run Docker Image') {
            agent {
                label {label 'master'}
            }
            steps {
                sh 'docker kill python-server'
                sh 'docker rm python-server'

            }
        }



    }



    post {

      agent {
                label {label 'master'}
            }

        always {
            sh 'docker run -dit --name python-server -p 5000:5000 python_app:$BUILD_NUMBER'
        }

 
   }

}

