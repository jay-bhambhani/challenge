import hashlib
from datetime import datetime

from challenge.model.base import db


class QuestionHistory(db.Model):

    __tablename__ = 'question_history'

    id = db.Column(db.Text, primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
    question_id = db.Column(db.Text, db.ForeignKey('question.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, question_id: str, text: str):
        self.created = datetime.now()
        self.question_id = question_id
        self.text = text
        self.id = self.make_id()

    def make_id(self):
        data = ' '.join([self.question_id, self.text, self.created.isoformat()])
        return hashlib.md5(data.encode('utf-8')).hexdigest()

    @classmethod
    def from_dict(cls, d):
        question_id = d['question_id']
        text = d['text']
        return cls(question_id, text)

    def to_dict(self):
        return {
            'id': self.id,
            'created': self.created.isoformat(),
            'question_id': self.question_id,
            'text': self.text
        }

    def __repr__(self):
        return '<QuestionHistory id: {id}, created: {created}, question_id : {question_id}, text: {text}>'.format(
            id=self.id,
            created=self.created.isoformat(),
            question_id=self.question_id,
            text=self.text
        )