from flask import Flask, request, render_template, jsonify

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


@app.route('/process_prompt', methods=['POST'])
def process_prompt():
    MAX_INPUT_LENGTH = 256
    user_prompt = request.get_json()['prompt']
    print(len(user_prompt))
    if len(user_prompt) > MAX_INPUT_LENGTH:
        return jsonify({'error': 'Input length exceeds the maximum allowed length.'}), 400
    for keyword in restricted_keywords:
        if keyword in user_prompt:
            return jsonify({'error': 'Your input contains restricted keywords.'}), 400
    # Execute the user's code and retrieve the model response
    model_response = execute_code(user_prompt)

    return jsonify({'response': model_response})


if __name__ == '__main__':
    app.run(debug=True)
