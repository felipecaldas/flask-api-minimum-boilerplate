import factory
from factory.alchemy import SQLAlchemyModelFactory
from app.models import db, User


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session 
        
    username = 'myusername'
    email = "myemail@asdf.dk"