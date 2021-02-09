pipeline {
    agent {
        node {
            label 'build'
        }
    }
    environment {
        BRANCH = 'main'
    }
    options {
        timeout(time: 1, unit: 'HOURS')
        buildDiscarder(logRotator(numToKeepStr: '20'))
        disableConcurrentBuilds()
        skipDefaultCheckout()
    }
    stages {
        stage('getcode') {
            steps {
                deleteDir()
                git credentialsId: '4c952718-7af6-4703-8b98-1e7d9d413272', url: 'https://github.com/adevarapally/wdsimpleapi.git', branch: env.BRANCH
            }
        }
        stage ('DockerImageBuild') {
            steps {
                sh '''#!/bin/sh -l
                cd $WORKSPACE_MAIN
                sudo docker pull ubuntu
                sudo docker build  -f Dockerfile . -t ${BRANCH}/${BUILD_NUMBER}
                ret=$?
                if [ $ret -ne 0 ]
                then 
                    exit 1
                fi
                '''
            }
        }
        stage('testdockerimage') {
            steps {
                sh '''#!/bin/sh
                set -euo pipefail
                IFS=$'\n\t'
                echo "Running docker image to test"
                sudo docker run --rm --cmd="python3 run.py" "${BRANCH}/${BUILD_NUMBER}:latest"
                '''
            }
        }
        stage('pushtodockerhub') {
            steps {
                sh '''#!/bin/sh
                set -euo pipefail
                IFS=$'\n\t'
                echo "Pushing to dockerhub"
                sudo docker push adevarapally/wdsimpleapi:${BRANCH}/${BUILD_NUMBER}
                '''
            }
        }
    }
}