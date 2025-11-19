# Use official slim Python
FROM python:3.11-slim

# system deps for common python wheels (adjust if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# set a working directory
WORKDIR /app

# Copy dependency files first (cache layer)
COPY requirements.txt .

# If you use a constraints file, copy it here as well:
# COPY constraints.txt .

# Install Python dependencies (non-root)
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy application
COPY . .

# Expose the port (Render will supply $PORT)
EXPOSE 8000

# Use an environment variable PORT if provided by Render. Default 8000.
# Use sh -c so ${PORT} expands
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000} --loop auto --http h11"]
