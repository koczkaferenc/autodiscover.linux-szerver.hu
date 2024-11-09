FROM python:latest
RUN mkdir /app
COPY app /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python3","app.py"]