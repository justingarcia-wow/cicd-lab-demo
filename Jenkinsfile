pipeline {
    agent any

    environment {
        APP_VERSION = "v${BUILD_NUMBER}"
        IMAGE_NAME  = "demo-app"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build imagen Docker') {
            steps {
                dir('demo-app') {
                    sh "sudo docker build -t ${IMAGE_NAME}:${APP_VERSION} ."
                }
            }
        }

        stage('Exportar imagen') {
            steps {
                dir('demo-app') {
                    sh "sudo docker save ${IMAGE_NAME}:${APP_VERSION} -o ${IMAGE_NAME}-${APP_VERSION}.tar"
                    sh "sudo chown jenkins:jenkins ${IMAGE_NAME}-${APP_VERSION}.tar"
                }
            }
        }

        stage('Deploy con Ansible') {
            steps {
                sh """
                ansible-playbook -i /etc/cicd-lab/hosts.ini playbooks/deploy.yml \
                  --extra-vars "app_version=${APP_VERSION} imagen_local_tar=${WORKSPACE}/demo-app/${IMAGE_NAME}-${APP_VERSION}.tar"
                """
            }
        }
    }

    post {
        success {
            echo "Deploy exitoso: ${IMAGE_NAME}:${APP_VERSION} en nodo1 y nodo2"
        }
        failure {
            echo "Algo falló, revisa el log del pipeline"
        }
        always {
            sh "sudo rm -f demo-app/${IMAGE_NAME}-${APP_VERSION}.tar || true"
        }
    }
}
