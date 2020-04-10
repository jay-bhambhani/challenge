from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

db = SQLAlchemy()

def _get_or_create(model, **kwargs):
    result = model.query.filter_by(**kwargs).first()
    if result:
        return result
    else:
        row = model.from_dict(kwargs)
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def _add_to_db(data):
    try:
        db.session.add(data)
    except SQLAlchemyError:
        db.session.rollback()
