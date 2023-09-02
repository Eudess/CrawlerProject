from flask import Flask, jsonify, render_template, request
from utils import utils

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/numero_processo', methods=['post'])
def query_process_number():
    process_number = request.form.get('numero_processo')
    formatted_process_number = utils.formatter_npu(process_number)

    return render_template('process.html')

if __name__ == '__main__':
    app.run(debug=True)