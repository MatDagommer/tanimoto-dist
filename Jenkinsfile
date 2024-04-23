pipeline {
    agent {
        docker { image 'continuumio/miniconda3' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'conda env create -f environment.yml'
            }
        }
        stage('Test') {
            steps {
                sh 'conda activate myenv'
                sh 'python -m pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Deployed!'
            }
        }
    }
}
