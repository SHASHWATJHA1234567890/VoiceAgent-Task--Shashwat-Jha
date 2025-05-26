from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def build_faiss_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(chunks, embeddings)
