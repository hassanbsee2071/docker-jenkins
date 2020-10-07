pipeline {
    agent none
    stages {
        stage('Instantiate Docker Agent') {
            agent {
                docker { image 'python:3' }
            }
            steps {
                sh 'python --version'
            }
        }
        stage('Build Docker Image from Dockerfile') {
            agent {
                label {label 'master'}
            }
            steps {
                sh 'docker build -t python_app:$BUILD_NUMBER .'
                sh 'echo "Build Number Is  $BUILD_NUMBER."'
            }
        }

        stage('Killing Previous Running Docker Container') {
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


        always {

          node('master') {
               sh 'docker run -dit --name python-server -p 5000:5000 python_app:$BUILD_NUMBER'

              }
 
        }

 
   }

}

