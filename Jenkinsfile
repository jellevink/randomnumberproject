pipeline{
        agent any
        
        stages{
		stage('--Build Docker--'){
			steps{
				sh '''. ~/.bashrc
				      pwd
				      ls
				      docker-compose build
				      docker ps -a
				      docker service ls
				      docker-compose push
				      '''
			}
		}
                stage('--Deploy Docker--'){
                        steps{
                                sh '''ssh qaproject2  << BOB
				      export BUILD_NUMBER="${BUILD_NUMBER}"
                                      #docker service update --image qaproject2jenkins:5000/random1:build-${BUILD_NUMBER} project_random1
				      #docker service update --image qaproject2jenkins:5000/random2:build-${BUILD_NUMBER} project_random2
				      #docker service update --image qaproject2jenkins:5000/combine:build-${BUILD_NUMBER} project_combine
				      docker service update --image qaproject2jenkins:5000/flask:build-${BUILD_NUMBER} project_flask
                                      '''
                        }
                }
        }
}
