pipeline {
    agent any

    environment {
        REMOTE_DIR = 'jenkins-flask-backend'
        APP_NAME   = 'flask-backend'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Syntax check') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Deploy to EC2') {
            steps {
                withCredentials([string(credentialsId: 'ec2-host', variable: 'EC2_HOST')]) {
                    sshagent(credentials: ['ec2-ssh-key']) {
                        sh '''
                            ssh -o StrictHostKeyChecking=no ec2-user@$EC2_HOST "
                                cd ~/${REMOTE_DIR} &&
                                git pull origin main &&
                                pip3 install --user -r requirements.txt &&
                                pm2 restart ${APP_NAME}
                            "
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Flask backend deployed successfully."
        }
        failure {
            echo "Flask backend deployment failed."
        }
    }
}
