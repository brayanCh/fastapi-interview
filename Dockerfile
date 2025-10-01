FROM python:3.13

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY internal/ ./internal/

# Expose port 8000
EXPOSE 8000

# Create entrypoint script that runs tests then starts the API
RUN echo '#!/bin/bash\n\
set -e\n\
echo "=========================================="\n\
echo "Running tests..."\n\
echo "=========================================="\n\
python -m pytest internal/tests/ -v\n\
TEST_EXIT_CODE=$?\n\
echo ""\n\
echo "=========================================="\n\
if [ $TEST_EXIT_CODE -eq 0 ]; then\n\
    echo "✓ All tests passed!"\n\
    echo "=========================================="\n\
    echo "Starting API server..."\n\
    echo "=========================================="\n\
    python -m internal.main \n\
else \n\
    echo "✗ Tests failed with exit code $TEST_EXIT_CODE"\n\
    echo "=========================================="\n\
    exit $TEST_EXIT_CODE\n\
fi' > /entrypoint.sh && chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]
