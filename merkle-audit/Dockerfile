FROM python:3.11-slim
WORKDIR /app
COPY merkle-audit/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY proto/ /app/proto/
COPY merkle-audit/ /app/merkle-audit/
CMD ["python", "merkle-audit/audit_server.py"]
