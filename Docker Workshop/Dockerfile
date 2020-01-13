FROM python:3.6.5-alpine3.7

RUN apk update && apk add sudo

COPY requirements.txt /python_api/requirements.txt

RUN pip install -r /python_api/requirements.txt

COPY . template

EXPOSE 300

CMD ["python", "-u", "api.py"]