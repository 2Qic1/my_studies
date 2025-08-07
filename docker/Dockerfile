FROM python:latest
RUN apt-get update && apt-get install python3-pip -y && pip install --upgrade pip && pip install pipenv
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app_site.py"]
