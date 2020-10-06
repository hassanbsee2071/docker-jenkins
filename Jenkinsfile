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
                sh 'docker build -t python_app:bravo .'
            }
        }
    }
}
