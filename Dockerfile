FROM python:3.10.5

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install -Ur requirements.txt

CMD ["python", "main.py"]

