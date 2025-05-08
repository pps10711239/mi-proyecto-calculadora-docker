pipeline {
    agent any

    stages {
        stage('Clonar código') {
            steps {
                git branch: 'main', url: 'https://github.com/pps10711239/mi-proyecto-calculadora.git'
            }
        }
        stage('Ejecutar test') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }
    }
}
