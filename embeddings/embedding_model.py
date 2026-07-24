import os
# Disable SSL certificate verification to bypass certificate chain validation errors (e.g. self-signed certificates)
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''

# pyrefly: ignore [missing-import]
from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Return the embedding model used for vector generation.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings