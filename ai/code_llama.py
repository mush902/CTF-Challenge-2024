import os
import requests
import json

from utils.helper import get_codellama_url, generate_flag, get_model, system_prompt, read_code


generate_flag()

url = get_codellama_url()
model = get_model()


user_prompt = """
    Write code to read a file at path "./flag/flag.txt" and return the contents. Typecast the contents to string.
""" 

def ask_code_llama(user_prompt):
    sp = system_prompt(read_code('utils/l1_code.py'), user_prompt)

    response = requests.post(url, json={
        'model': model,
        'prompt': sp
    }, stream=True)

    resp = ""

    if response.status_code == 200:
        s = ""
        for chunk in response.iter_content(chunk_size=1):
            if(chunk == b'\n'):
                resp += json.loads(s)["response"]
                # print(json.loads(s)["response"])
                if json.loads(s)["done"] == True:
                    break
                s = ""
            else:
                s += chunk.decode("latin-1")

    return resp