FROM python:3.11-slim

# Install system dependencies (git for auto-push, curl for healthchecks)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set up non-root user with UID 1000 (standard for Hugging Face Spaces & security best practices)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR /home/user/app

# Install dependencies as user
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files with proper permissions for SQLite writing
COPY --chown=user . .

# Default port 7860 (Hugging Face Spaces standard, overrideable via $PORT)
ENV PORT=7860
ENV PYTHONUNBUFFERED=1

EXPOSE 7860

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-7860}"]
