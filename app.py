from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/numero_processo', methods=['post'])
def query_process_number():
    numero_processo = request.form.get('numero_processo')
    print(numero_processo)
    return render_template('process.html')

if __name__ == '__main__':
    app.run(debug=True)