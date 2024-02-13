# Use an official lightweight Python image.
FROM python:3.8-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY . /app

# Install any needed packages specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Uvicorn will run on.
EXPOSE 80

# Run the Uvicorn server.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
