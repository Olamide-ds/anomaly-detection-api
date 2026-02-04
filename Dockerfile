FROM python:3.11-slim

# Safer defaults for ML / HF
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TOKENIZERS_PARALLELISM=false
ENV OMP_NUM_THREADS=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files (NEW STRUCTURE)
COPY app ./app
COPY models ./models

# Expose API port
EXPOSE 8000

# Run the FastAPI app (NEW ENTRYPOINT)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

