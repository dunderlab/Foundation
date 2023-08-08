FROM archlinux:base-devel

LABEL image="dunderlab/djangoship"
LABEL version="1.1"
LABEL maintainer="yencardonaal@unal.edu.co"
LABEL description=""
LABEL project=""
LABEL documentation=""
LABEL license="BSD 2-Clause"

RUN pacman --noconfirm -Suy \
    && pacman --noconfirm -S git vim apache postgresql python

COPY startup.sh /usr/local/bin/

RUN mkdir /etc/djangoship/
COPY django.conf.template /etc/djangoship/

RUN chmod +x /usr/local/bin/startup.sh

WORKDIR /app

RUN python -m venv venv311 \
    && source venv311/bin/activate \
    && pip install django django-filter django_extensions psycopg2 channels djangorestframework mod_wsgi \
    && deactivate


WORKDIR /app/djangoship

EXPOSE 80

CMD ["/usr/local/bin/startup.sh"]
