import os
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
    tribunal = utils.get_tribunal(formatted_process_number)
    if tribunal == "tjce":
        spider_logs = start_spider_ce(formatted_process_number)
        return render_template('process.html', spider_logs=spider_logs)

    return render_template('process.html')

def start_spider_ce(process_number):
   os.system("cd crawler && scrapy crawl esaj_tjce-1-grau -a numero_processo=" + process_number)

if __name__ == '__main__':
    app.run(debug=True)