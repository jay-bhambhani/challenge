import hashlib
from datetime import datetime

from challenge.model.base import db
from challenge.model.conversations_questions import conversation_questions


class Conversation(db.Model):

    __tablename__ = 'conversation'

    id = db.Column(db.Text, primary_key=True)
    started = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Text, db.ForeignKey('user.id'), nullable=False)
    questions = db.relationship('QuestionHistory', secondary=conversation_questions, lazy='subquery',
                    backref=db.backref('conversations', lazy=True))

    def __init__(self, user_id: str):
        self.started = datetime.now()
        self.user_id = user_id

    def make_id(self):
        qs = ','.join([q.id for q in self.questions])
        data = ' '.join([self.user_id, self.started, str(qs)])
        return hashlib.md5(data.encode('utf-8')).hexadigest()

    @classmethod
    def from_dict(cls, d):
        user_id = d['user_id']
        return cls(user_id)

    def to_dict(self):
        return {
            'id': self.id,
            'started': self.started.isoformat(),
            'user_id': self.user_id,
            'questions': str([q.id for q in self.qs])
        }

    def __repr__(self):
        return '<Conversation id: {id}, started: {started}, user_id : {user_id}, questions: {qs}>'.format(
            id=self.id,
            started=self.started,
            user_id=self.question_id,
            qs=str([q.id for q in self.qs])
        )