FROM python:3.10-slim-buster
EXPOSE 5000
COPY requirements.txt /
RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install --no-cache-dir -r requirements.txt
COPY /authentication_project /authentication_project
ENV PYTHONPATH /authentication_project
WORKDIR /authentication_project/apps
CMD ["python", "main.py"]
