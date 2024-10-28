FROM python:3.10-slim

WORKDIR /jp-cadastro

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=deploy.DJANGO_SETTINGS_MODULE

RUN python manage.py collectstatic --noinput

RUN python manage.py migrate --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "deploy.wsgi:application"]