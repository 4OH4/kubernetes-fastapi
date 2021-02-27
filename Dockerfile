FROM python:3.7

COPY requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

EXPOSE 8080

COPY ./service /service

# Use the ping endpoint as a healthcheck,
# so Docker knows if the API is still running ok or needs to be restarted
HEALTHCHECK --interval=21s --timeout=3s --start-period=10s CMD curl --fail http://localhost:8080/ping || exit 1

CMD ["uvicorn", "service.main:app", "--host", "0.0.0.0", "--port", "8080"]
