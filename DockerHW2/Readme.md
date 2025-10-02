## Basic Running of Docker

# First, install and open Docker

# Build!
docker build --no-cache -t myfastapi -f Docker/Dockerfile .

# Run
docker run -d -p 5002:5000 myfastapi  

# See your local
http://localhost:5002/docs


