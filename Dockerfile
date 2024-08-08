FROM python:3.12

WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv
RUN pipenv install --deploy

COPY . /app

CMD ["pipenv", "run", "python", "src/app.py"]
