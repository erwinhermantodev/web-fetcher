# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set main.py executable
RUN chmod +x /app/main.py

# Specify the command to run when the container starts
CMD ["python", "/app/main.py"]
