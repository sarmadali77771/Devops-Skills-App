# DevOps Skills App

A interactive Flask web application showcasing essential DevOps skills with clickable information bubbles. Perfect for practicing Docker, CI/CD, and other DevOps workflows.

![DevOps Skills App Screenshot](https://raw.githubusercontent.com/sarmadali77771/Devops-Skills-App/refs/heads/main/devops-skills.png)

## Features

- Interactive skill bubbles with hover descriptions
- Modern gradient background
- Responsive design
- Docker-ready configuration
- Simple Flask backend

## Technologies Used

- Python 3.9
- Flask
- HTML5/CSS3
- JavaScript (minimal)
- Docker

## Prerequisites

- Python 3.9+
- Docker (optional)
- Git

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/sarmadali77771/Devops-Skills-App.git
cd devops-skills-app
```

### Build the Docker image

```bash
docker build -t devops-skills-app .
```

### Run the container

```bash
docker run -p 9050:9050 --name devops-app devops-skills-app
```

### On Browser

```bash
http://localhost:9050
```

### Project Structure

```bash
devops-skills-app/
├── app.py                # Main Flask application
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
├── README.md            
├── templates/
│   └── index.html       
└── static/
    ├── css/
    │   └── style.css    
    └── js/
        └── script.js
```

License
MIT License

Author
Sarmad Ali - https://github.com/sarmadali77771/
