# Use official Python base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
