import hashlib
from datetime import datetime

from challenge.model.base import db


class Topic(db.Model):

    __tablename__ = 'topic'

    id = db.Column(db.Text, primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.Text)

    def __init__(self, name:str):
        self.name = name
        self.created = datetime.now()
        self.id = self.make_id()

    def make_id(self):
        return hashlib.md5(self.name.encode('utf-8')).hexdigest()

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'])

    def to_dict(self):
        return {
            'id': self.id,
            'created': self.created.isoformat(),
            'name': self.name
        }

    def __repr__(self):
        return '<Topic id: {id}, created: {created}, name: {name}>'.format(
            id=self.id,
            created=self.created.isoformat(),
            name=self.name
        )

db.Index('idx_topic__name', Topic.name, unique=True)
