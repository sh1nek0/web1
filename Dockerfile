
FROM python:3.10  

WORKDIR /caucasus  


COPY requirements.txt  requirements.txt
RUN pip install -r requirements.txt

COPY . . 


CMD ["gunicorn", "caucasus.wsgi:application"]
