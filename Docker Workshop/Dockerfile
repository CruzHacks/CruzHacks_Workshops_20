FROM python:3.6.5-alpine3.7

# COPY requirements.txt /python_api/requirements.txt

COPY ./ python_api

RUN pip install -r /python_api/requirements.txt

EXPOSE 5000

WORKDIR /python_api/

CMD ["python", "-u", "server.py"]