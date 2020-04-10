from challenge.model.base import db

conversation_questions = db.Table(
    'conversation_questions',
    db.Column('conversation_id', db.Text, db.ForeignKey('conversation.id'), primary_key=True),
    db.Column('question_id', db.Text, db.ForeignKey('question_history.id'), primary_key=True)
)