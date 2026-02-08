# Use an official Python runtime as a parent image
FROM python:3.14

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file from the host to the container's working directory
COPY requirements.txt .

# Install the Python packages
RUN pip install --no-cache-dir -r requirements.txt

# [Optional] Ensure the container runs as a non-root user for security
# USER vscode