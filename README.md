# Flask Weather App

## Features

- Built with Python and Flask
- Simple and clean HTML frontend
- Dockerized for easy deployment
- Cross-platform compatibility via WSL2 or Linux

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Python 3.x](https://www.python.org/) (optional if you want to run locally without Docker)
- [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) (for Windows users)


Build Docker Image:

docker build -t flask-weather-app .

Run the Container:

docker run -p 5000:5000 flask-weather-app

visit http://localhost:5000/home 

----------------------------------------

Run Locally Without Docker (optional)
pip install -r requirements.txt
python app.py