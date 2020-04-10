import os

from flask import Flask
from flask_migrate import Migrate
from challenge.routes.routes import question


app = Flask(__name__)
app.register_blueprint(question)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{password}@{host}/{db}'.format(
    user = os.environ.get('PG_USER'),
    password = os.environ.get('PG_PW'),
    host = os.environ.get('PG_HOST'),
    db = os.environ.get('PG_DB')
)


from challenge.model import *
from challenge.model.base import db
db.init_app(app)
migrate = Migrate(app, db, directory=os.path.join('challenge', 'migrations'))

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)