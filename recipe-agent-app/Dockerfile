# Use a slim Python base image
#FROM python:3.11-slim
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Cloud Run injects the PORT environment variable.
# We run the uvicorn server with main:app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]