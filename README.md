# flask-api-minimum-boilerplate
A basic boilerplate for flask with flask-restful and pytest

* Python 3.6
* pytest 3.0.6
* pytest-coverage 4.3.4
* Flask 0.12
* flask-restful 0.3.5
* flask-script 2.0.5

The boilerplate builds an API by using Flask's blueprint functionality. 
he API will be available on /api/v1/

The only endpoint setup is: /api/v1/status which returns a status message.

##Project Structure
  ```sh
  ├── README.md
  ├── app.py
  ├── config.py
  ├── requirements.txt
  ├── app
  │   ├── __init__.py
  │   ├── api_v1
  │   │   ├── __init__.py
  │   │   ├── routes.py
  └── tests
  │       └── conftest.py
  ```
  
##Project Setup
```
>> virtualenv venv -p python3
>> source venv/bin/activate
>> pip install -r requirements.txt
>> python manage.py runserver
```
Point your browser/GET request to:
http://localhost:5000/api/v1/status

```
{
    status: "Up and running"
}
```


##Testing
