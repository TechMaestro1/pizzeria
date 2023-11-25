FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /base
COPY requirements.txt /base/
RUN pip install -r requirements.txt
COPY . /base/