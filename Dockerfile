FROM python:3.9

# Install system dependencies
RUN apt-get update && \
    apt-get install -y postgresql-client redis-server

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install Python dependencies
RUN  pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=lead_ultimate_user
ENV POSTGRES_PASSWORD=Balkot11@
ENV POSTGRES_DB=lead_ultimate_db

# Start Redis and PostgreSQL services
CMD service redis-server start && \
    service postgresql start && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    celery -A mainsite worker --loglevel=info --concurrency=10 & \
    python manage.py runserver 0.0.0.0:8080
