import os
import subprocess
import json
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
        process_files = read_process_files(formatted_process_number)
        return render_template('process.html', spider_logs=spider_logs, process_data=process_files[0])
    elif tribunal == "tjal":
        spider_logs = start_spider_al(formatted_process_number)
        process_files = read_process_files(formatted_process_number)
        return render_template('process.html', spider_logs=spider_logs, process_data=process_files[0])

    return render_template('process.html')

def start_spider_ce(process_number):
    cmd = f"cd crawler && scrapy crawl esaj_tjce-1-grau -a numero_processo={process_number}"
    subprocess.run(cmd, shell=True, check=True, text=True)

def start_spider_al(process_number):
    cmd = f"cd crawler && scrapy crawl esaj_tjal-1-grau -a numero_processo={process_number}"
    subprocess.run(cmd, shell=True, check=True, text=True)


def read_process_files(process_number):
    process_files = []
    
    if os.path.exists('crawler/processo'):
        for filename in os.listdir('crawler/processo'):
            if filename.endswith('.json') and process_number in filename:
                filepath = os.path.join('crawler/processo', filename)
                with open(filepath, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    process_files.append(data)
    
    return process_files

if __name__ == '__main__':
    app.run(debug=True)