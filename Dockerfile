#base image
FROM ubuntu:latest

#set label for the application
LABEL Description="This image will build the application"

# install packages
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3.6 \
    python3-pip 

#set working directory
WORKDIR /var/www/app

#copy app
COPY . .

#install packages from requirements file. 
RUN pip3 install -r requirements.txt

# expose port 
EXPOSE ${PORT}

#run application
CMD [ "python3", "run.py" ]
