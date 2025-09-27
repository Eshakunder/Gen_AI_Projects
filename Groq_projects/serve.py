# langserve is a package from the LangChain ecosystem that helps you deploy LangChain models, chains, and agents as APIs (usually REST or gRPC). Instead of writing a lot of FastAPI/Flask boilerplate, you just wrap your chain and expose it as a service.

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="Gemma2-9b-it",groq_api_key=groq_api_key)


system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system",system_template),("user","{text}")])

parser = StrOutputParser()

##create chain
chain = prompt_template | model | parser

##App definition
app = FastAPI(title="langchain_server",
              version="1.0",
              description="A simple langchain server with groq model")

##Add chain as route
add_routes(app,chain , path='/chain')



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
