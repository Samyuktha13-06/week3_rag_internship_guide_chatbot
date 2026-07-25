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
    try:
        # Attempt to load from the local cache first to avoid network calls and SSL issues
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"local_files_only": True}
        )
    except Exception:
        # Fallback to online loading if the model is not found in the local cache
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    return embeddings