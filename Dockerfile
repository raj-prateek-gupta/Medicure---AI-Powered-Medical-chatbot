# Use official slim Python
FROM python:3.11-slim

# System dependencies for scientific Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /app

# Copy dependency file first (to maximize layer caching)
COPY requirements.txt .

# Install dependencies
RUN python -m pip install --upgrade pip setuptools wheel \
 && pip install -r requirements.txt

# Copy actual application
COPY . .

# Expose port (Render injects PORT env)
EXPOSE 8000

# Start Uvicorn with PORT from Render
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]
