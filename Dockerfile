# Use official Python image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy local code to the container image
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on (Flask default: 5000)
EXPOSE 5001

# Start the app
CMD ["python", "app.py"]