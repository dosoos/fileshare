# Use the official Python image from the Alpine distribution
FROM python:alpine

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["flask", "run"]

EXPOSE 3000