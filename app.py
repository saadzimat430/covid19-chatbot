import json
import os
import pickle

import dialogflow
import numpy as np
import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# run Flask app
if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get_disease", methods=['POST'])
def get_disease():
    data = request.get_json()
    symptoms = data['queryResult']['parameters']['symptom']

    disease = requests.get('https://flask832.herokuapp.com/get_disease?symptoms={0}'.format(','.join(symptoms))).content
    disease_json = json.loads(disease)
    response = """
             You might have {0}.
         """.format(disease_json['data'])

    reply = {
    "fulfillmentText": response,
    }

    return jsonify(reply)


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)

        return response.query_result.fulfillment_text

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    response_text = {"message": fulfillment_text}

    return jsonify(response_text)