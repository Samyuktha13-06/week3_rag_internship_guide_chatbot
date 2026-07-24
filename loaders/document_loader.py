# pyrefly: ignore [missing-import]
from langchain_community.document_loaders import PyPDFLoader


def load_documents(pdf_path: str):
    """
    Load the internship guide PDF.

    Returns:
        List of LangChain Document objects.
    """

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents