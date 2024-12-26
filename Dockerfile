FROM python:3.9-slim

# Set the working directory
WORKDIR /app

COPY exercise1.py .

# Run the Python script
CMD ["python", "exercise1.py"]
