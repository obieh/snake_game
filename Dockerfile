FROM python:3.9-slim

WORKDIR /code

COPY . .

ADD snakev1.py .


# Expose the VNC port (5901 by default)
EXPOSE 5901

RUN apt-get update && \
apt-get install -y python3-dev libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libsm6 libxext6 libxrender-dev && \
pip install --no-cache-dir pygame

# Add these lines to the original Dockerfile to set up VNC
RUN apt-get update && apt-get install -y \
    xfce4 \
    xfce4-goodies \
    tightvncserver
    

CMD ["python3", "/snakev1.py", "tightvncserver", "1"]

