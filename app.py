from flask import Flask, request, render_template, jsonify, Response
from ai.code_llama import ask_code_llama
from utils.helper import run_accepted_code
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)

# List of restricted keywords
restricted_keywords = ['file', 'flag', 'printf']


def execute_code(code):
    # Execute the user's code and retrieve the flag
    flag = 'CTF{example_flag}'
    return flag


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['prompt']
        for keyword in restricted_keywords:
            if keyword in user_input:
                return render_template('index.html', error='Your input contains restricted keywords.')
        # Execute the user's code and retrieve the flag
        flag = execute_code(user_input)
        return render_template('index.html', flag=flag)
    return render_template('index.html')


code = """
New code
# Codellama is supposed to implement this function
def add_two_numbers():
    with open('./../flag/flag.txt') as file:
        contents = file.read()
        return str(contents)
"""

user_prompt = """"""

@app.route('/interact', methods=['POST'])
def interact():
    global code
    global user_prompt
    user_prompt = request.get_json()['prompt']
    code = ask_code_llama(user_prompt)
    formatted_code = highlight(code, PythonLexer(), HtmlFormatter())
    return jsonify({'response': formatted_code})


@app.route('/process-response', methods=['POST'])
def process_response():
    accepted_response = request.get_json()['response']
    new_response = process_accepted_response(accepted_response)
    return jsonify({'newResponse': new_response})


def process_accepted_response(accepted_response):
    print(accepted_response.split(user_prompt)[1])
    new_response = run_accepted_code(accepted_response.split(user_prompt)[1])
    return new_response


if __name__ == '__main__':
    app.run(debug=True)