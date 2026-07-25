# pyrefly: ignore [missing-import]
from langchain_core.output_parsers import StrOutputParser

from prompts.rag_prompt import rag_prompt
from retriever.retriever import get_retriever
from utils.llm import llm

retriever = get_retriever()

output_parser = StrOutputParser()


def ask_question(question: str):

    documents = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    chain = (
        rag_prompt
        | llm
        | output_parser
    )

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response