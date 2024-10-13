#!/bin/bash

# install dependencies
pip install -r requirements.txt

# Run the Flask server
export FLASK_APP=app.py
export FLASK_ENV=development
flask run