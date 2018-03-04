FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# CMD [ "python", "manage.py", "runserver", "-h", "0.0.0.0", "-p", "5000" ]
CMD [ "flask", "run", "-h", "0.0.0.0", "-p", "5000" ]