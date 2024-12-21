FROM python:3.12.3-alpine3.20

# Install packages
RUN apk add --update --no-cache supervisor texmf-dist texlive-full gcc musl-dev

# Upgrade pip
RUN python -m pip install --upgrade pip

# Setup app
RUN mkdir -p /app

# Switch working environment
WORKDIR /app

# Add application
COPY challenge .

# Install dependencies
RUN pip install flask

# Copy configs
COPY config/supervisord.conf /etc/supervisord.conf

# Expose port the server is reachable on
EXPOSE 1337

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]