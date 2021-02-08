FROM ubuntu:latest
# Get Arguments
ARG APP
ARG PORT

# Set Environment Variables
ENV APP ${APP}
ENV PORT ${PORT}


LABEL Description="This image will build the application"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3.6 \
    python3-pip \
    python3.6-venv \
    python3.6-dev
WORKDIR /var/www/{APP}
COPY . .


EXPOSE ${PORT}

ENTRYPOINT [ "./entrypoint.sh" ]
