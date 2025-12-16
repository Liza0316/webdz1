# FROM python:3.11-slim
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3.11
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONPATH="/usr/local/lib/python3.11/site-packages"
RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
RUN /bin/bash -c "DJANGO_SETTINGS_MODULE=practice1.settings python -m django collectstatic --noinput"
RUN DJANGO_SETTINGS_MODULE=practice1.settings python manage.py migrate --fake
EXPOSE 8080
CMD ["gunicorn", "practice1.wsgi:application", "--bind", "0.0.0.0:8080"]