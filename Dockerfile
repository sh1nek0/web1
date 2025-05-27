
FROM python:3.10  

WORKDIR /caucasus  


COPY . .  

RUN pip install -r requirements.txt  

CMD ["gunicorn", "caucasus.wsgi:application"]
