FROM python

WORKDIR ~
COPY . .

RUN pip install -r reqs.txt

EXPOSE 8080

ENTRYPOINT ["python3", "app.py"]

