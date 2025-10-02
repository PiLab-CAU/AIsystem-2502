# 1. Python 기반 이미지
FROM python:3.9-slim

# 2. working directory
WORKDIR /app

# 3. Install requirements 
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt


# 4. copying app
COPY app.py .
# 5. run
CMD ["python", "app.py"]
