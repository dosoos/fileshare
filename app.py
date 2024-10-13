from flask import Flask, render_template, request, send_from_directory
from datetime import datetime
from werkzeug.serving import get_interface_ip
import socket
import time
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    files = request.files.getlist('files')
    for file in files:
        while os.path.exists(os.path.join(UPLOAD_FOLDER, file.filename)):
            file.filename = file.filename + '_' + str(int(time.time()))
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return {'code': 0, 'message': 'success'}


@app.route('/delete/<filename>', methods=['DELETE'])
def delete(filename):
    os.remove(os.path.join(UPLOAD_FOLDER, filename))
    return {'code': 0, 'message': 'success'}


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


# static css/* and js/*
@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file('/static/' + path)


@app.route('/')
def index():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    files = []
    for file in os.listdir(UPLOAD_FOLDER):
        date = datetime.fromtimestamp(os.path.getctime(os.path.join(UPLOAD_FOLDER, file)))
        files.append(
            {
                'filename': file, 
                'create_time': date.strftime('%Y-%m-%d %H:%M:%S')
            } 
        )
    main_url = 'http://' + get_interface_ip(socket.AF_INET)
    return render_template('index.html', files=files, main_url=main_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
