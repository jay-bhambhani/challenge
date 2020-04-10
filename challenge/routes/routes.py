from flask import request, abort, Blueprint

from challenge.model.base import _get_or_create, _add_to_db
from challenge.model.question import Question
from challenge.model.question_history import QuestionHistory
from challenge.model.topic import Topic

question = Blueprint('question', __name__)


@question.route("/question", methods=["POST"])
def add_question():
    request_data = request.get_json()
    _handle_missing_fields(request_data, 'topic', 'name')
    query = {'name': request_data['topic']['name']}
    topic = _get_or_create(Topic, **query)
    _handle_missing_fields(request_data, 'question', 'text')
    question_data = request_data['question']
    question = Question(topic.id, question_data['text'])
    _add_to_db(question)

    return question.to_dict()

@question.route("/question/<question_id>", methods=["GET"])
def get_question(question_id):
    question = Question.query.get_or_404(question_id)
    return question.to_dict()


@question.route("/question/<question_id>", methods=["PUT"])
def update_question(question_id):
    request_data = request.get_json()
    question = Question.query.get_or_404(question_id)
    _handle_missing_fields(request_data, 'question', 'text')
    question_data = request_data['question']
    text = question_data['text']
    history = QuestionHistory(question.id, text)
    _add_to_db(history)
    question.text = text
    _add_to_db(question)
    return question.to_dict()


@question.route("/history/question/<question_id>", methods=["GET"])
def get_question_history(question_id):
    history = QuestionHistory.query.filter_by(question_id=question_id).all()
    return {'history': [qh.to_dict() for qh in history]}

def _handle_missing_fields(request_data, key, value):
    if not request_data.get(key):
        abort(400, 'you must have a {key} field'.format(key=key))
    elif not isinstance(request_data.key, dict):
        abort(400, '{key} field is malformed json'.format(key=key))
    elif not request_data[key].get(value):
        abort(400, 'you must have a {key} field with a {value}'.format(key=key, value=value))
