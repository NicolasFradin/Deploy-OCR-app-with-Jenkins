pipeline {
    agent  any
   
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh("pwd")
                sh("docker build . -t img/totxt")
               
                

            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh("docker rm -f img-to-txt && docker run --name img-to-txt -p 3001:3001 -d  img/totxt")
            }
        }
    }
}
