FROM python:3.12

RUN useradd -m alex

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip cache purge

COPY . .

RUN chown -R alex:alex /app

RUN python manage.py collectstatic --noinput

CMD ["sh", "-c", "gunicorn", "recipe_site_django.wsgi:application", "--bind", "0.0.0.0:8000"]