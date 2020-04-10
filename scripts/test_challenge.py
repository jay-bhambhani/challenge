import json

import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('type', help='question or history of question')
parser.add_argument('-c', '--command', help='create or update question')
parser.add_argument('-t', '--topic_name', help='topic name')
parser.add_argument('-n', '--question_text', help='question_text')
parser.add_argument('-q', '--question_id', help='question id to input')


def create_record(topic, question_text):
    data = {'topic': {'name': topic}, 'question': {'text': question_text}}
    response = requests.post('http://localhost:8000/question', json=data)
    return response.json()

def update_record(question_id, question_text):
    pl = {'question': {'text': question_text}}
    response = requests.put('http://localhost:8000/question/{question_id}'.format(question_id=question_id), json=pl)
    return response.json()


def view_history(question_id):
    response = requests.get('http://localhost:8000/history/question/{question_id}'.format(question_id=question_id))
    return response.json()

if __name__ == '__main__':
    args = parser.parse_args()
    if args.type == 'question':
        if args.command == 'create':
            print(create_record(args.topic_name, args.question_text))
        elif args.command == 'update':
            print(update_record(args.question_id, args.question_text))
    if args.type == 'history':
        print(view_history(args.question_id))



