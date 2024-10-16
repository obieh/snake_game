# Linux
xhost +local:root
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw snake-game

# For macOS or Windows:
You'll need to use an X server (like XQuartz on macOS or VcXsrv on Windows) to forward the graphical display from the container to your host. Here’s how you can do that:

1.Install an X11 Server:
 .For macOS: Install XQuartz.
 .For Windows: Install VcXsrv.

2.Run the X11 Server:
.For macOS: Open XQuartz and go to Preferences > Security and check "Allow connections from network clients".

  .Run the following command to allow Docker containers to connect to XQuartz:
  xhost + 127.0.0.1

Run the Docker Container:
# For MacOS
  docker run -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix:rw snake-game

# For Windows
  docker run -e DISPLAY=host.docker.internal:0 snake-game

# Build the Docker Image
  docker build -t snake-game .

# Tag the Image: If you're pushing to Docker Hub
  docker tag snake-game <your-dockerhub-username>/snake-game:latest

# Push the Image to Docker Hub:
  docker push <your-dockerhub-username>/snake-game:latest

# Explanation of the Dockerfile
Base Image: We're using python:3.9-slim as the base image because it's lightweight and provides the Python runtime.
Working Directory: The WORKDIR /app command sets /app as the working directory inside the container.
Copy Files: COPY . . copies the current directory (your project files, including the snake.py) into the /app directory in the container.
Install Dependencies: The RUN apt-get install ... command installs necessary libraries and dependencies for pygame to work. This includes SDL libraries and other graphical libraries.
Command to Run the Game: The CMD directive specifies the command that will be run when the container starts (python snake.py).

# To configure VNC, you need to update Dockerfile to include a lightweight VNC server
# Add these lines to the original Dockerfile to set up VNC
RUN apt-get update && apt-get install -y \
    xfce4 \
    xfce4-goodies \
    tightvncserver

# Expose the VNC port (5901 by default)
EXPOSE 5901

# Start the VNC server in the CMD
CMD ["tightvncserver", ":1"]

