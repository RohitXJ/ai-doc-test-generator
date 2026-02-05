# Use an official Python runtime as a parent image
FROM python:3.11-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY src ./src
COPY prompts ./prompts

# Define the entrypoint for the container. 
# This command will be executed when the container starts.
ENTRYPOINT ["python", "/app/src/main.py"]
