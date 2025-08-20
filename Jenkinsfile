pipeline{
    
    agent any;
    
    stages{
        
        stage("code"){
            steps{
                
                git url: 'https://github.com/sarmadali77771/Devops-Skills-App.git', branch: 'main'
            }
        }
        
        stage("build"){
            steps{
                
                sh "docker build -t skills:latest ."
                sh "docker image prune -f"
                sh "docker image ls"
            }
        }
        
        stage ("push") {
                steps {
                    withCredentials([usernamePassword (
                        credentialsId: 'dhl',
                        usernameVariable: 'DHL_USER',
                        passwordVariable: 'DHL_PASS'
                    
                    )]){
                        sh 'docker login -u ${DHL_USER} -p ${DHL_PASS}'
                        sh 'docker tag skills:latest ${DHL_USER}/skills:latest'
                        sh 'docker push ${DHL_USER}/skills:latest'
                        
                      }
                    }            
        }
        
        
        stage("deploy"){
            steps{
                sh "docker stop skills && docker rm skills"
                sh "docker run --name skills -d -p 9050:9050 skills:latest"
                //sh "docker image prune -f"
                
            }
        }
        
        
    }
    
}
