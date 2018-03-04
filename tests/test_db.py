from app.models import User, db
from factories.user_factory import UserFactory


def test_user_model(session):
    user = UserFactory()
    print(user.email)
    print(user.username)
    
    db.session.commit()

    users = User.query.all()
    print("OUTPUT")
    print(users)
    for u in users:
        print(u)


    assert False