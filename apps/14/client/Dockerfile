FROM python

WORKDIR ~
COPY . .

EXPOSE 8080

RUN pip install -r reqs.txt

ENTRYPOINT ["python3", "app.py", ">", "/output.txt"]

