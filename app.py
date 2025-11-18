import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv

# LangChain imports
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Local imports
from src.helper import load_embedding_model
from src.prompt import prompt

# ----------------------------------------
#         INITIAL SETUP
# ----------------------------------------

load_dotenv()

app = FastAPI()

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML templates folder
templates = Jinja2Templates(directory="templates")

# Environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
HUGGINGFACE_ACCESS_TOKEN = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = HUGGINGFACE_ACCESS_TOKEN

# Load embedding model
embedding = load_embedding_model()

# Connect to existing Pinecone index
vector_store = PineconeVectorStore.from_existing_index(
    embedding=embedding,
    index_name="medicure"
)

# Retriever
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)


# Hugging Face LLM
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=HUGGINGFACE_ACCESS_TOKEN,
)

model = ChatHuggingFace(llm=llm)

# Build QA chain
QA_chain = create_stuff_documents_chain(
    llm=model,
    prompt=prompt
)

# ----------------------------------------
#         LCEL RAG PIPELINE
# ----------------------------------------


rag_chain = (
    {
        "question": RunnablePassthrough(),
        "context": retriever 
    }
    | QA_chain
    | StrOutputParser()
)

# ----------------------------------------
#              ROUTES
# ----------------------------------------

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


class ChatRequest(BaseModel):
    query: str


@app.post("/chat")
def chat_api(request_data: ChatRequest):
    response = rag_chain.invoke(request_data.query)
    return {"answer": response}
