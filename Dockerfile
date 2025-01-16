FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Create and activate virtual environment
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Install the Python dependencies in the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to allow access to the Flask app
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]