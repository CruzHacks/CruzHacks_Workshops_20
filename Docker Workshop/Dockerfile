FROM python:3.6.5-alpine3.7

COPY ./ /python_api

RUN pip install Flask==1.1.1

EXPOSE 5000

WORKDIR /python_api

CMD ["python", "server.py"]