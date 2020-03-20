FROM python:3-alpine

WORKDIR /entertainmentCrossing

COPY . .
RUN pip3 install -r requirements.txt

CMD ["python3", "run.py"]
