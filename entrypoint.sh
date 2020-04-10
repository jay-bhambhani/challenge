#!/usr/bin/env bash
wait-for-it -s database:5432
flask db upgrade
flask run --host=0.0.0.0 --port=8000