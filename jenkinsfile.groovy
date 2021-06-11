pipeline {
    agent any

    stages {
        stage('configure repository and checkout') {
            steps {
                git 'https://github.com/netashiloh/WorldOfGames.git'
                bat 'git checkout'

            }}
        stage('Build and run docker for MainScores app') {
            steps {
                bat 'docker build -t wog .'
                bat 'docker run -d -p 8777:8777 --name wog_container --mount source=myvol,target=/app wog'
            }}
        stage('test') {
            steps {
                mystepppps
            }}
        }
    }
}
