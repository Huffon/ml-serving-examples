FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-devel

WORKDIR /app

COPY . .

RUN apt-get -y update && \
    apt-get -y install apt-utils gcc

RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["uvicorn", "src.app.app:app", "--host", "0.0.0.0", "--port", "8080"]