#!/bin/bash

# install dependencies
pip install -r requirements.txt

# Run the Flask server
flask run --host=0.0.0.0 --port=80
