## Basic Running of Docker

# First, install and open Docker

# Build!
docker build -t myapp -f Docker/Dockerfile .

# Run
docker run -d -p 5001:5000 myapp

# See your local
http://localhost:5001

