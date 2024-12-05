ARG PYTHON_VERSION=3.12-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

COPY pyproject.toml requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code

ENV SECRET_KEY "kGqFfkyrBCtzP5juiYhXfl86QAadCZHMZZBOWTVf9yQyeyUTbK"
RUN python manage.py collectstatic --noinput

EXPOSE 8000
RUN python manage.py migrate --noinput
CMD ["gunicorn","--bind",":8000","--workers","2","rzpercussion_site.wsgi"]
