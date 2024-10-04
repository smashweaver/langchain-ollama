from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="mistral:latest")

# template = """Question: {question} Answer: your name is {name}.  you are a masterchef"""
# prompt = ChatPromptTemplate.from_template(template)
# chain = prompt | model
# result = chain.invoke({ "question": "give me a meal plan" })
# print(result["output"])

prompt = ChatPromptTemplate([ 
    ("system", "You are a masterchef named {name}."),  
    ("ai", "Introduce youself, followed by the answer"),
    ("human", "{question}") 
])

chain = prompt | model
result = chain.invoke({ "question": "give me an exotic meal plan with lots of eggs.", "name": "Gordon" })
print(result)
