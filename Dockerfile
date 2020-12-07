FROM python:3.9-slim

WORKDIR /var/www/app

# create .venv dir (this is where pipenv will install)
RUN mkdir .venv

# install dep
RUN pip install --upgrade pip
RUN pip install pipenv

COPY . /var/www/app

RUN pipenv install --deploy

EXPOSE 5000
CMD [ ".venv/bin/gunicorn", "--workers=4", "--bind", "0.0.0.0:5000", "app:app" ]
