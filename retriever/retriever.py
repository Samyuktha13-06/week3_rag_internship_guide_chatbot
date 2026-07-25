from vectorstore.faiss_db import load_vector_store
from embeddings.embedding_model import get_embedding_model


def get_retriever():

    embeddings = get_embedding_model()

    vector_store = load_vector_store(embeddings)

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 3
        }
    )

    return retriever