FROM python:3.8 as base

WORKDIR /usr/src/app
COPY . .

RUN pip install pipenv && pipenv install
RUN git clone https://github.com/vishnubob/wait-for-it.git

FROM base as prod
WORKDIR /usr/src/app
COPY --from=base /usr/src/app /usr/src/app/

RUN pipenv run python app/manage.py collectstatic --noinput
