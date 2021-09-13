import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/siebert/sentiment-roberta-large-english"
headers = {"Authorization": f"Bearer" + os.getenv("API_TOKEN")}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

st.title('Sentiment Analysis')
form = st.form(key='my_form')
text = form.text_input(label='Enter some text')


submit_button = form.form_submit_button(label='Submit')

output = query({"inputs":text})
score = output


if submit_button:
    st.subheader('Data')
    st.write(output)