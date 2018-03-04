import logging
import os

import click

from app import create_app


logging.basicConfig(level=logging.INFO)
app = create_app((os.getenv("ENV") or "local").lower())


@app.shell_context_processor
def make_shell_context():
    return dict(app=app)


@app.cli.command()
def test():
    """Run py.test on the full test suite"""
    import psycopg2
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    import pytest


    con = psycopg2.connect(
        dbname='postgres', 
        user=os.getenv('POSTGRES_USER', 'tester'), 
        host=os.getenv('POSTGRES_HOST', 'db'),
        password=os.getenv('POSTGRES_PASSWORD', '12345'),
    )
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    try:
        cur.execute('CREATE DATABASE ' + 'flaskdb_test')
    except:
        logging.info("Test database already exists")
    cur.close()
    con.close()

    pytest.main(['tests', '-v', '-l'])

