FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /recipe_app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./recipe_site_django .

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]