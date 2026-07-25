from rag.rag_chain import ask_question

question = "What are the GitHub guidelines?"

response = ask_question(question)

print("Question:")
print(question)

print("\nAnswer:")
print(response)