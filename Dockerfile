FROM python:3.8.1-alpine

RUN pip install flask

ADD . .

ENV FLASK_APP "server"
ENV FLASK_ENV "development"
CMD ["flask", "run", "--host", "0.0.0.0"]
