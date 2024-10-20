from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

def test_prompt(model):
    template = """Question: {question}. You are the masterchef {name}.
    Always introduce yourself and lighten the mood with a trivia joke before saying bye"""

    prompt = PromptTemplate(input_variables=["name", "question"], template=template)
    chain = prompt | model
    result = chain.invoke(input={"question": "give me the Indian style chicken recipe for the day", "name":"Gordon Ramsay"})
    print(f"\n{result.strip()}\n")

def test_chat(model):
    prompt = ChatPromptTemplate([
        ("system", "You are the masterchef named {name}."),
        ("system", "You are currently drunk so lighten the mood with a trivia joke"),
        ("human", "{question}")
    ])

    chain = prompt | model
    result = chain.invoke({ "question": "give me the Indian style chicken recipe for the day.", "name": "Gordon Ramsay" })
    print(result)

if __name__ == "__main__":
    model = OllamaLLM(model="mistral:latest")
    test_prompt(model)
