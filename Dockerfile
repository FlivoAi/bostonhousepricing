FROM python:3.7
COPY . /app
RUN pip install lightgbm pandas numpy google-cloud-aiplatform protobuf==3.20.3 google-cloud-storage
COPY app.py ./app.py
EXPOSE 5000
ENTRYPOINT ["python", "app.py","5000"]
