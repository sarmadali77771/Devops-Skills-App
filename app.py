from flask import Flask, render_template
import os

app = Flask(__name__)

# Skill data
skills = [
    {"name": "Linux", "description": "Linux is an open source os and the foundation of most DevOps workflows..."},
    {"name": "Docker", "description": "Docker is a platform for developing app, and shipping in isolated environment.."},
    {"name": "Git", "description": "Git is a distributed version control system..."},
    {"name": "Python", "description": "Python is a versatile programming language..."},
    {"name": "Bash", "description": "Bash is a Unix shell and command language for automation"},
    {"name": "Kubernetes", "description": "Kubernetes is an open-source container orchestration tool"},
    {"name": "Ansible", "description": "Ansible is an open-source automation tool.."},
    {"name": "Jenkins", "description": "Jenkins is an open-source automation server for CI/CD"},
    {"name": "Terraform", "description": "Terraform is an infrastructure as code tool..."},
    {"name": "Grafana", "description": "Grafana is an open-source analytics and monitoring..."},
    {"name": "Prometheus", "description": "Prometheus is an open-source monitoring system..."},
    {"name": "AWS", "description": "Amazon Web Services is a cloud computing platform..."},
    {"name": "Azure", "description": "Microsoft Azure is a cloud computing service provider..."},
]

@app.route('/')
def index():
    return render_template('index.html', skills=skills)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9050, debug=True)
