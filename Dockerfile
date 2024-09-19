# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    postgresql \
    postgresql-contrib \
    python3-pip \
    python3-venv \
    build-essential \
    supervisor \
    nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install virtualenv
RUN pip install virtualenv

# Create a directory for the application
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Create a virtual environment and install Python packages
RUN virtualenv venv
RUN . venv/bin/activate && pip install -r requirements.txt

# Set up PostgreSQL (you might want to use a more secure approach for passwords)
RUN service postgresql start && \
    sudo -u postgres psql -c "CREATE USER myuser WITH PASSWORD 'mypassword';" && \
    sudo -u postgres createdb mydatabase -O myuser

# Install Gunicorn
RUN . venv/bin/activate && pip install gunicorn

# Install Supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80 8000

# Start Supervisor
CMD ["/usr/bin/supervisord"]
