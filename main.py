import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("openai_api_key")


def chat_with_csv(df, prompt):
    llm = OpenAI(api_token='sk-proj-Jkg8D6OMNx9wigpkpwF0T3BlbkFJ5ebjuAdNCUPIruKJoElT')
    pandas_ai = PandasAI(llm)
    response = pandas_ai.run(df, prompt=prompt)

    return response


st.set_page_config(layout='wide')

st.title("ChatCSV powered by LLM")

user_data = st.file_uploader("Upload your CSV file", type='csv')

if user_data is not None:

    col1, col2 = st.columns([3, 3])

    with col1:
        st.info("CSV Uploaded Successfully")
        data = pd.read_csv(user_data)
        st.dataframe(data, use_container_width=True)

    with col2:

        st.info("Chat Below")

        chat= st.text_area("Enter your query")

        if chat is not None:
            if st.button("Chat with CSV"):
                st.info("Your Query: " + chat)
                response = chat_with_csv(data, chat)
                st.success(response)






