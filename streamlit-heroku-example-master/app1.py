import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/siebert/sentiment-roberta-large-english"
API_TOKEN = "api_sErMXBdmAcnkozNxyWwmiEhTwcDJnpKeUG"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

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