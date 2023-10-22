FROM python:3.11-buster

WORKDIR /src

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# ENTRYPOINT ["python", "/app/setup_data.py"]

CMD gunicorn --bind 0.0.0.0:8000 --workers 3 travel_proj.wsgi:application