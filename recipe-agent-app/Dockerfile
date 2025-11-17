# Use the standard Python image
FROM python:3.11 

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file and install them
COPY requirements.txt .
# CHANGE THIS LINE: Use --verbose to get detailed logs
RUN pip install --no-cache-dir --verbose -r requirements.txt 

# Copy the rest of the application code
COPY . .

# Cloud Run injects the PORT environment variable.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]