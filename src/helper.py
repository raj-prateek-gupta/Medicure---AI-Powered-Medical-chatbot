from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


def load_data_file(data):
  
  loader = DirectoryLoader(
    data,
    glob="*.pdf",
    loader_cls=PyPDFLoader
  )

  document = loader.load()
  return document

def extract_page_content_and_source(docs):
    final_docs = []
    for doc in docs:
        src=doc.metadata.get("source", "unknown")
        final_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source":src}
            )
        )
    return final_docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)
    return chunks

def load_embedding_model():
    """
    Download and initialize the HuggingFace embedding model.
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_model = HuggingFaceEmbeddings(
      model_name=model_name
    )

    return embedding_model


