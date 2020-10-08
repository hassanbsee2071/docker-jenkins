pipeline {
    agent none
    stages {
        stage('Instantiate Docker Agent') {
            agent {
                docker { image 'python:3' }
            }
            steps {
                    sh 'python --version'
                    sh 'docker build -t python_app:$BUILD_NUMBER .'
                    sh 'echo "Build Number Is  $BUILD_NUMBER."'
                    sh 'docker save -o python_app_$BUILD_NUMBER.tar python_app:$BUILD_NUMBER'
                    fingerprint 'python_app_$BUILD_NUMBER.tar'
                    archiveArtifacts '**/*.tar'
                    stash allowEmpty: true, includes: '**/*.tar', name: 'buildArtifacts'

                  }


        }
        stage('Build Docker Image from Dockerfile') {
            agent {
                label {label 'master'}
            }
            steps {
                dir(images){
                unstash 'buildArtifacts'
                           }
            }
        }




    }



    post {


        always {

          node('master') {
               sh 'echo Hassan'

              }
 
        }

 
   }

}

