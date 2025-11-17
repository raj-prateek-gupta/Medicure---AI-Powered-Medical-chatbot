import os 
from dotenv import load_dotenv
from src.helper import load_data_file, extract_page_content_and_source, split_documents,load_embedding_model
from pinecone import Pinecone # type: ignore
from langchain_pinecone import PineconeVectorStore # type: ignore

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
HUGGINGFACE_ACCESS_TOKEN = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = HUGGINGFACE_ACCESS_TOKEN

extracted_data = load_data_file('./data')
page_contents = extract_page_content_and_source(extracted_data)
chunk_content = split_documents(page_contents)

embedding = load_embedding_model()

vector_store = PineconeVectorStore.from_documents(
    documents=chunk_content,
    embedding=embedding,
    index_name="medicure", 
)