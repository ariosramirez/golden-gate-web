# Use the official Python image from the Docker Hub
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy requirements into the container at /app
COPY ./requirements.txt /app/requirements.txt

# Copy the environment file
COPY .env .env

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app


# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=run.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]