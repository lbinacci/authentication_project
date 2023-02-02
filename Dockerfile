FROM python:3.10-slim-buster
COPY requirements.txt /
RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install --no-cache-dir -r requirements.txt
COPY /authentication_project /authentication_project
ENV PYTHONPATH=$PYTHONPATH:/authentication_project
WORKDIR /authentication_project/authentication_project/apps
CMD ["python", "main.py"]
