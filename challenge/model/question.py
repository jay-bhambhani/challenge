import hashlib
from datetime import datetime

from challenge.model.base import db


class Question(db.Model):

    __tablename__ = 'question'

    id = db.Column(db.Text, primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
    topic_id = db.Column(db.Text, db.ForeignKey('topic.id'), nullable=False)
    initial_text = db.Column(db.Text, nullable=False)

    def __init__(self, topic_id:str, text:str):
        self.created = datetime.now()
        self.topic_id = topic_id
        self.initial_text = text
        self.id = self.make_id()

    def make_id(self):
        data = ' '.join([self.topic_id, self.initial_text])
        return hashlib.md5(data.encode('utf-8')).hexdigest()

    @classmethod
    def from_dict(cls, d):
        topic_id = d['topic']
        text = d['text']
        return cls(topic_id, text)

    def to_dict(self):
        return {
            'id': self.id,
            'created': self.created.isoformat(),
            'topic_id': self.topic_id,
            'initial_text': self.initial_text
        }

    def __repr__(self):
        return '<Question id: {id}, topic_id : {topic_id}, text: {text}>'.format(
            id=self.id,
            topic_id=self.topic_id,
            text=self.text
        )


