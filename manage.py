import os
from flask_script import Manager, Shell
from app import create_app


env = os.getenv("ENV") or "local"
app = create_app(env.lower())
manager = Manager(app)


def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def test():
    """ Run py.test """
    import pytest
    pytest.main(['--cov=app', '--html=report.html', 'tests'])


if __name__ == '__main__':
    manager.run()


