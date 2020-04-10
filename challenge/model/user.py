import enum
import hashlib

from datetime import datetime

from challenge.model.base import db


class Sex(enum.Enum):
    MALE = 'm'
    FEMALE = 'f'

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False)
    age = db.Column(db.Integer)
    sex = db.Column(db.Enum(Sex))

    def __init__(self, name: str, age: int, sex: Sex):
        self.created = datetime.now()
        self.name = name
        self.age = age
        self.sex = sex
        self.id = self.make_id()

    def make_id(self):
        data = ' '.join([self.name])
        return hashlib.md5(data.encode('utf-8')).hexdigest()

    @classmethod
    def from_dict(cls, d):
        name = d['name']
        age = d['age']
        sex = Sex(d['sex'])
        return cls(name, age, sex)

    def to_dict(self):
        return {
            'id': self.id,
            'created': self.created.isoformat(),
            'name': self.name,
            'age': self.age,
            'sex': self.sex.value
        }

    def __repr__(self):
        return '<QuestionHistory id: {id}, created: {created}, question_id : {question_id}, text: {text}>'.format(
            id=self.id,
            created=self.created,
            question_id=self.question_id,
            text=self.text
        )