


import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)
title_prompt = PromptTemplate(
    input_variables = ["Country"],
    template = """
    You are an experienced chef-cook.
    You need to find the favourite recipy based 
    on the following topic: {topic}
    Answer exactly with one title.
    """
)

speech_prompt = PromptTemplate(
    input_variables = ["title"],
    template = """
    You need to write a recipy of 100 words
    for the following title: {title}
    """
)

first_chain = title_prompt | llm | StrOutputParser()
second_chain = speech_prompt | llm
final_chain = first_chain | second_chain
st.title("Cuisine Recipy App")

topic = st.text_input("Enter the country:")

if topic:
    response = final_chain.invoke({"topic": topic
    })
    st.write(response.content)
    print(response)
