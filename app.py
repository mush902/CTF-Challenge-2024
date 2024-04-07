from flask import Flask, request, render_template, jsonify, Response
from ai.code_llama import ask_code_llama
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


example_code = """
def greet(name):
    print(f"Hello, {name}!")
    print("Hi)
    print("Hello")
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

    greet("World")
"""


@app.route('/interact', methods=['POST'])
def interact():
    MAX_INPUT_LENGTH = 256
    user_prompt = request.get_json()['prompt']

    # if len(user_prompt) > MAX_INPUT_LENGTH:
    #     return jsonify({'error': 'Input length exceeds the maximum allowed length.'}), 400
    # for keyword in restricted_keywords:
    #     if keyword in user_prompt:
    #         return jsonify({'error': 'Your input contains restricted keywords.'}), 400
    # Execute the user's code and retrieve the model response
    #model_response = ask_code_llama(user_prompt)

    formatted_code = highlight(example_code, PythonLexer(), HtmlFormatter())
    print(formatted_code)
    return jsonify({'response': formatted_code})


# @app.route('/interact', methods=['POST'])
# def interact():
#     user_prompt = request.get_json()['prompt']
#     return Response(ask_code_llama(user_prompt), content_type="text/plain")


@app.route('/process-response', methods=['POST'])
def process_response():
    accepted_response = request.get_json()['response']
    new_response = process_accepted_response(accepted_response)
    return jsonify({'newResponse': new_response})


def process_accepted_response(accepted_response):
    new_response = 'This is the new response generated from the accepted response.'
    return new_response


if __name__ == '__main__':
    app.run(debug=True)