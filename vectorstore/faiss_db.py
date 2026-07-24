# pyrefly: ignore [missing-import]
from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embeddings):

    return FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )


def save_vector_store(vector_store, path="vectorstore/faiss_index"):

    vector_store.save_local(path)


def load_vector_store(embeddings, path="vectorstore/faiss_index"):

    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )