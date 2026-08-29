FROM python:3.11-slim
WORKDIR /app
COPY telemetry-normalization/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY proto/ /app/proto/
COPY telemetry-normalization/ /app/telemetry-normalization/
CMD ["python", "telemetry-normalization/client_stream.py"]
