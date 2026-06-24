import os
from typing import List
from flask import Flask, Response, render_template, send_from_directory, abort

app = Flask(__name__)

VERSIONS_DIR = os.path.join(app.root_path, 'versions')
LATEST_DOWNLOAD = 'Bitcode IDE 4.0.0.msi'


@app.route('/')
def index() -> str:
    return render_template('index.html')


@app.route('/downloads')
def downloads() -> str:
    try:
        versions: List[str] = sorted(os.listdir(VERSIONS_DIR), reverse=True)
    except FileNotFoundError:
        versions = []
    return render_template('downloads.html', versions=versions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
