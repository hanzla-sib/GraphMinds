from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

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
        result = chain.invoke(
            {
                "context": "The pizza was delicious and the service was great. I loved the pepperoni pizza and the crust was perfect.",
                "question": user_input
            }
        )
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

