FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /recipe_app

RUN pip install --upgrade

COPY requirements.txt requirements.txt

RUN pip install requirements.txt

COPY ./recipe_site_django .

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]