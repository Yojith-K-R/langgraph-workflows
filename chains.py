from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import (
    JsonOutputParser,
    PydanticOutputParser,
    StrOutputParser
)
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

parser=StrOutputParser()

prompt=ChatPromptTemplate.from_template(
    '''You are a helpful assistant. Please provide a summary of the following {topic}:
'''
)

uppercase=RunnableLambda(lambda x: x.upper())

def lowercase(text:str)->str:
    return {
        'text':text.lower(),
        'length':len(text.split(' '))
    }

lowerCaseRunnable=RunnableLambda(lowercase)

chain=prompt|llm|parser|RunnableLambda(lambda x:x.split())

# result=chain.batch([
#     {"topic":"Python programming language"},
#     {"topic":"Machine learning"},
#     {"topic":"Natural language processing"}
#     ])

result = chain.stream({
    "topic": "Python programming language"
})

for chunk in result:
    print(chunk, end="",flush=True)
# print(result)

