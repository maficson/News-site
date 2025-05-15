from flask import Flask, request
import os

app = Flask(__name__)

# Папка для збереження файлів
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return '''
        <h1>Файл-сервер працює!</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Завантажити файл">
        </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return f'Файл {file.filename} отримано та збережено!'
    return 'Файл не надіслано', 400

# Головний запуск з підтримкою порту Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
