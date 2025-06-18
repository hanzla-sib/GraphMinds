from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
model=OllamaLLM(
    model="llama3.1",
)
    
    
template="""
you are expert in answering questions about a pizza restaurant

here are some relevant reviews:
{context}

here is the question to answer : {question}
"""


prompt=ChatPromptTemplate.from_template(template)

chain=prompt | model

while True:
    try:
        user_input = input("Enter your question (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        retriever_result = retriever.invoke(user_input)
        result = chain.invoke(
            {
                "context": retriever_result,
                "question": user_input
            }
        )
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

