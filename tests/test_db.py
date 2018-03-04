from app.models import User


def test_user_model(session):
    user = User(username='testuser', email="per@per.dk")

    session.add(user)
    session.commit()

    assert user.id > 0    