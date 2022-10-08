pipeline {
    agent any

    triggers {
        cron('0 10 * * *') //regular builds at 10 AM Everyday
    }

    stages {
        stage('Checkout') {
            steps { //Checking out the repo
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'a5ffd0e6-dfdd-4204-9513-3c4493055ffd', url: 'https://github.com/gauravmaheshwari2101/Python.git']]])
            }
        }
        stage('Build') {
            steps { //Building the application
               git branch: 'main', credentialsId: 'a5ffd0e6-dfdd-4204-9513-3c4493055ffd', url: 'https://github.com/gauravmaheshwari2101/Python.git'
               bat Script: ‘main.py’
            }
        }           
        stage('Cleanup') {
            steps { // Cleaning up checkout 
                cleanWs()               
            }    
         } 
     }
}

