FROM python:3.8

RUN mkdir /app
RUN pip install --upgrade pip
RUN pip install wait-for-it
COPY . /app
WORKDIR /app
ENV FLASK_APP app.py
ENV PG_HOST database
ENV PG_USER buoy
ENV PG_PW buoy0buoy
ENV PG_DB challenge
RUN pip install -r requirements.txt
RUN chmod u+x entrypoint.sh