import streamlit as st
import requests

url = 'https://api.berri.ai/create_app'
data = {'user_email': 'akshatpunia04@gmail.com'}

st.title('lmao')
uf = st.file_uploader("Choose a PDF file", type="pdf")
user_input = st.text_input("Ask your query about the document you uploaded?")

if uf is not None:
    pdf_bytes = uf.read()

    files = {'data_source': ('uploaded.pdf', pdf_bytes)}
    response = requests.post(url, files=files, data=data)
    response.raise_for_status()  
    api_endpoint = response.json()['api_endpoint']

    user_query = user_input
    final_url = api_endpoint + "&query=" + user_query
    response = requests.get(final_url)
    system_response = response.json()["response"]
    st.write(system_response)