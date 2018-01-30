from sqlalchemy import create_engine

from main import db

import models


def db_start():
    create_engine('sqlite:///tmp/test.db', convert_unicode=True)
    db.create_all()
    db.session.commit()
    post1 = models.BlogPosts()
    post1.subject = "Pierwszy"
    post1.text = "Tekst"

if __name__ == '__main__':
    db_start()