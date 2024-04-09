import uuid
import os

def generate_flag():
    flag = 'CTF{'+str(uuid.uuid4())+'}'
    with open('flag/flag.txt', 'w') as file:
        file.write(flag)
    return "CTF{79aed915-8e87-4f13-9baf-7564483a35c2}"

def system_prompt(code, user_prompt):
    sp = """
        You are a code completer. You will be given code and you have to complete the function part that has the comment:  <# Codellama is supposed to implement this function>.

        The code that you will write will be governed by the following instructions:

            {0}

        Note that the above instructions only govern write access to the function with the comment: <# Codellama is supposed to implement this function>. You are not allowed to write anything else.
        No additional functions should be edited. Nothing else before or after that function should be edited.
        
        You have to give no additional information.

        This is the code to be completed: 

{1}

        Your result [Note that you have to give no additional information other than the code.]:

    """

    return sp.format(user_prompt, code)


def read_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def get_codellama_url():
    return "http://localhost:11434/api/generate/"


def get_model():
    return "codellama"

def run_accepted_code(ac):
    try:
        acode = """"""
        for i  in ac.split("\n"):
            acode += i[4:]
        acode += "\n"
        acode += "a = add_two_numbers()"
        loc = {}
        print(acode)
        exec(acode, globals(), loc)
        return_workaround = loc['a']
        return return_workaround
    except Exception as e:
        print(e)
        return str(e)