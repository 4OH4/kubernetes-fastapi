FROM python:3.7

COPY requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

EXPOSE 8080

COPY ./service /service

CMD ["uvicorn", "service.main:app", "--host", "0.0.0.0", "--port", "8080"]
