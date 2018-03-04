FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# RUN apt-get update
# RUN apt install -y python3-dev
# RUN apt install -y libmysqlclient-dev
# RUN pip install mysqlclient
# RUN export FLASK_APP=autoapp.py
# RUN export FLASK_DEBUG=1

# CMD [ "python", "manage.py", "runserver", "-h", "0.0.0.0", "-p", "5000" ]
CMD [ "flask", "run", "-h", "0.0.0.0", "-p", "5000" ]