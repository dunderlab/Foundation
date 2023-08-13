# Usar una imagen base de Python 3.11
FROM python:3.11

LABEL image="dunderlab/python311"
LABEL version="1.3"
LABEL maintainer="yencardonaal@unal.edu.co"
LABEL description=""
LABEL project=""
LABEL documentation=""
LABEL license="BSD 2-Clause"

# Establecer un directorio de trabajo
WORKDIR /app

ENV PIP_ROOT_USER_ACTION=ignore

# Instalar cualquier dependencia necesaria.
RUN pip install confluent-kafka \
                docker \
                numpy \
                scipy \
                matplotlib \
                tornado \
                flask \
                mne \
                jupyterlab \
                figurestream \
                radiant-framework \
                dunderlab-foundation \
                dunderlab-docs \
                figurestream
