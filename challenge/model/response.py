import hashlib
from datetime import datetime

from challenge.model.base import db


class Response(db.Model):

    __tablename__ = 'response'

    id = db.Column(db.Text, primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
    conversation_id = db.Column(db.Text, db.ForeignKey('conversation.id'), nullable=False)
    question_history_id = db.Column(db.Text, db.ForeignKey('question_history.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, conversation_id: str, question_history_id: str, text: str):
        self.created = datetime.now()
        self.question_history_id = question_history_id
        self.conversation_id = conversation_id
        self.text = text
        self.id = self.make_id()

    def make_id(self):
        data = ' '.join([self.question_history_id, self.conversation_id, self.created, self.text])
        return hashlib.md5(data.encode('utf-8')).hexadigest()

    @classmethod
    def from_dict(cls, d):
        conversation_id = d['conversation_id']
        question_history_id = d['question_history_id']
        text = d['text']
        return cls(conversation_id, question_history_id, text)

    def to_dict(self):
        return {
            'id': self.id,
            'created': self.created.isoformat(),
            'question_history_id': self.question_history_id,
            'conversation_id': self.conversation_id,
            'text': self.text
        }

    def __repr__(self):
        return '<Response id: {id}, created: {created}, conversation_id: {conversation_id}, question_history_id : {question_history_id}, text: {text}>'.format(
            id=self.id,
            created=self.created.isoformat(),
            conversation_id=self.conversation_id,
            question_history_id=self.question_history_id,
            text=self.text
        )