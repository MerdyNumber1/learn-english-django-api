FROM python:3.8

WORKDIR /usr/src/app
COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv && pipenv install
RUN git clone https://github.com/vishnubob/wait-for-it.git

CMD ["./wait-for-it/wait-for-it.sh", "postgres:$POSTGRES_PORT", "--", "pipenv", "run", "prod"]
