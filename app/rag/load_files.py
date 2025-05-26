from langchain.document_loaders import PyPDFLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf(path):
    docs = PyPDFLoader(path).load()
    return split_docs(docs)

def load_web(url):
    docs = WebBaseLoader(url).load()
    return split_docs(docs)

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)


def load_context(source: str):
    """Loads and splits documents from either a PDF path or a URL."""
    if source.endswith(".pdf"):
        return load_pdf(source)
    elif source.startswith("http://") or source.startswith("https://"):
        return load_web(source)
    else:
        raise ValueError("Unsupported source. Provide a .pdf file or a URL.")
