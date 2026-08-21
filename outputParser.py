# OpenAI
from openai import OpenAI

# Validation
from pydantic import BaseModel, Field

# Typing
from typing import List, Dict, Optional, Literal

# Utilities
import json

# LangChain (optional)
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import (
    JsonOutputParser,
    PydanticOutputParser,
    StrOutputParser
)
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv()


class SupportTicket(BaseModel):
    customer_name:str
    category:Literal["Billing", "Technical", "General"] = Field(..., description="Category of the support ticket")
    priority:Literal["Low", "Medium", "High"] = Field(..., description="Priority of the support ticket")
    summary:str=Field(min_length=10, max_length=200, description="Summary of the support ticket")


prompt = ChatPromptTemplate.from_template(
    '''You are a helpful assistant. Please create a support ticket based on the following information:
    {text}

    {format_instructions}'''
)

llm=chatopenai=ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

chain=prompt|llm|PydanticOutputParser(pydantic_object=SupportTicket)

try:
    result=chain.invoke({
    "text":"iam yojith facing soome buying issue","format_instructions":PydanticOutputParser(pydantic_object=SupportTicket).get_format_instructions()
})
    print(result)
    print(result.customer_name)
    print(result.category)
    print(result.priority)
    print(result.summary)
    print(type(result))

except Exception as e:
    print("Error:", e)
    result=None
    

parser=PydanticOutputParser(pydantic_object=SupportTicket)
def test_support_ticket():
   
    try:
        result = parser.parse({
            "customer_name": "John Doe",
            "priority": "no",
        })
        print(result)

    except Exception as e:
        print("Parsing failed:", e)


test_support_ticket()


