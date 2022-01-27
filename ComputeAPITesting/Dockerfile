FROM python:3.8

WORKDIR /backendautomation

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./features ./features

COPY ./utilities ./utilities

CMD ["behave"]