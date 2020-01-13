# Every Docker image is built on top of another image. In this case, we're going
# to build on top of an existing image of Alpine Linux with Python already installed.

FROM python:3.6.5-alpine3.7

# We're going to copy the contects of the project folder into the container.
# This is how our Python files will get into the container.

COPY ./ python_api

# We the use Docker RUN command to run shell commands.
# In this case, we're using Pip to install Flask.

RUN pip install flask

# Containers have their own network that's seperate from localhost on your machine.
# To connect to the server that's going to run inside the container, we'll expose port 5000.
# When we expose a port we'll be abl to connect to it via our own localhost.

EXPOSE 5000

# Change the current directory inside the container to where we copied our files into.

WORKDIR /python_api/

# Start the Python server.

CMD ["python", "-u", "server.py"]