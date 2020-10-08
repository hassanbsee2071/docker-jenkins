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
                    sh 'docker save -o python_app:$BUILD_NUMBER.tar python_app:$BUILD_NUMBER'
                    stash allowEmpty: true, includes: 'python_app:$BUILD_NUMBER.tar', name: 'buildArtifacts'

                  }


        }
        stage('Build Docker Image from Dockerfile') {
            agent {
                label {label 'master'}
            }
            steps {
                unstash 'buildArtifacts'
                sh 'yes | sudo cp -R python_app:$BUILD_NUMBER.tar .'
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

