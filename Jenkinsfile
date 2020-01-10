pipeline{
        agent any
        
        stages{
		stage('--Build Docker--'){
			steps{
				sh '''. ~/.bashrc
				      docker-compose build
				      docker-compose push
				      '''
			}
		}
                stage('--Deploy Docker--'){
                        steps{
                                sh '''ssh 34.89.127.153  << BOB
				      export BUILD_NUMBER="${BUILD_NUMBER}"
                                      cd project_changed/
                      docker service update --image 34.89.85.60:5000/random1:build-${BUILD_NUMBER} projectchanged_random1
				      docker service update --image 34.89.85.60:5000/random2:build-${BUILD_NUMBER} projectchanged_random2
				      docker service update --image 34.89.85.60:5000/combine:build-${BUILD_NUMBER} projectchanged_combine
				      docker service update --image 34.89.85.60:5000/flask:build-${BUILD_NUMBER} projectchanged_flask
                                      '''
                        }
                }
        }
}
