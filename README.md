# flask-api-minimum-boilerplate
A basic boilerplate for flask with flask-restful and pytest

* Python 3.6
* pytest 3.0.6
* pytest-coverage 2.4.0
* pytest-html 1.14.2
* Flask 0.12
* flask-restplus 0.10.1
* flask-script 2.0.5

The boilerplate builds an API by using Flask's blueprint functionality. 
he API will be available on /api/v1/

The only endpoint setup is: /api/v1/status which returns a status message.

## Project Structure
  ```sh
  ├── README.md
  ├── app.py
  ├── config.py
  ├── requirements.txt
  ├── app
  │   ├── __init__.py
  │   └── api_v1
  │       ├── __init__.py
  │       ├── routes.py
  └── tests
          ├── test_routes.py
          └── conftest.py
  ```
  
## Project Setup
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


## Testing

Will run py.test like: 'py.test --cov=app tests'.
```
>> python manage.py test
```
