# Use a lightweight Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
