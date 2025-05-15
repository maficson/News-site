from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return 'Сервер працює!'

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return 'Файл отримано!', 200
    return 'Файл не надіслано', 400

if __name__ == '__main__':
    app.run()
