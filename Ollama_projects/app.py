import os 
from dotenv import load_dotenv
import streamlit as st  
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# ##langsmith tracking
# os.environ["LANGCHAIN_API_KEY"] = None
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")

##prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system","You are an helpful assistant .please answer the question as best as you can"),
    ("user","Question:{question}")])

##streamlit framework
st.title("Langchain demo with Ollama")
input_text = st.text_input("What question you have in mind?")

##ollama model calling 
llm = Ollama(model="gemma3:1b")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))