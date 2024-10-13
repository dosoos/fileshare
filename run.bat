@echo off

@REM Install the required packages
pip install -r requirements.txt

@REM Run the Flask server
flask run --host=0.0.0.0 --port=80
