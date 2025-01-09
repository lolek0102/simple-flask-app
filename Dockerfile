//FROM python:3.9-slim


//WORKDIR /app


//COPY . /app


//RUN pip install -r requirements.txt


//EXPOSE 5000


//CMD ["python", "app.py"]
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]
