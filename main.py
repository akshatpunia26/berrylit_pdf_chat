import streamlit as st
import requests
url = 'https://api.berri.ai/create_app'
data = {'user_email': 'akshatpunia04@gmail.com'}
st.title('Berrylit - a Berri.ai and Streamlit Implementation')
st.write("This code provides a simple interface for users to upload a PDF file and ask a question related to it. The code utilizes Streamlit to create the web interface and the Berri API to process the uploaded file and provide the answer to the user's query.")
uf = st.file_uploader("Choose a PDF file", type="pdf")
user_input = st.text_input("Ask your query about the document you uploaded?")
st.info('Ignore the error message, trying to fix')
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

    st.markdown('''
## TO run this code and use the chabot locally:

1. Clone the repository and navigate to the directory in your terminal.
    ```sh
    git clone https://github.com/username/repo-name.git
    cd repo-name
    ```

2. Install the required packages using pip.
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Python script using the following command:
    ```sh
    streamlit run pdf_query_chatbot.py
    ```

4. The chatbot interface will open in your default browser. You can upload a PDF file by clicking on the "Choose a PDF file" button and ask your query related to the document. 

Note: The code uses the Berri API to process the uploaded PDF file and provide the answer to the user's query. To use this code, you need to have a Berri API key. This code has been tested with Python 3.7 and Streamlit 0.84.0. The code is provided as-is and is free to use and modify.
''')