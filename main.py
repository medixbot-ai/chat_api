#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openai
from flask import Flask, jsonify, request

from configure import configure_pinecone
from utils import configure_openai, determine_intention, get_chat, read_file
from vector import query_vector

vector_index = "together"
app = Flask(__name__)
configure_openai()
configure_pinecone()

@app.route("/chat_ai",methods=['POST'])
def analyze_text():
    data = request.get_json()
    input_text = data.get('text', '')

    prompt = f"Determine the intention of the text: '{input_text}'. Is it about job ads, generate list of job positions according to the job description, list of all employee names,list top employee names?"

   # response = get_chat(prompt) 
   # generated_text = response['choices'][0]['text'].strip()

   # intention = determine_intention(generated_text)
   # # Return the result as JSON
   # if intention == "Job Ads Writing":
   #     response = get_chat(input_text)
   #     generated_text = response['choices'][0]['text'].strip()
   # elif  intention == "Listing Job Position":
   #     if len(read_file("project.txt")) == 0:
   #         response = get_chat(input_text)
   #         generated_text = response['choices'][0]['text'].strip()
   #     else:
   #         project = read_file("project.txt")
   #         input_text = input_text + "\n" +project
   #         response = get_chat(input_text)
   #         generated_text = response['choices'][0]['text'].strip()

   # elif intention == "Listing Top Employee Names" or intention == "Listing All Employee Names":
   #     generated_text = query_vector(vector_index,input_text)
   # else:
   #     generated_text = "please refine the prompt"
    result = {'input_text': input_text, 'generated_text': "Message from chat_ai endpoint","intention":"intention is ..."}
    return jsonify(result)

@app.route("/set_project",methods=['POST'])
def project():
    data = request.get_json()
    project = data.get('project', '')

    with open("project.txt","w") as f:
        f.write(project)
    return {"response":"Update project successfully"}


if __name__ == "__main__":
    app.run(debug=True)
