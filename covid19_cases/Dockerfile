FROM python:3.8
WORKDIR /app
COPY covid_app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8050

CMD [ "python", "./covid_app.py" ]