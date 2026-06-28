from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import StructuredTool
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from llm import llm
from tools import get_order, get_product, search_products



class OrderInput(BaseModel):
    order_id: str = Field(description="Customer order ID, e.g. ORD-1002")

class ProductInput(BaseModel):
    product_id: str = Field(description="Product ID, e.g. P101")

class SearchInput(BaseModel):
    query: str = Field(description="Keyword to search products by, e.g. 'shoes'")


tools = [
    StructuredTool.from_function(
        func=get_order,
        name="get_order",
        description="Fetch order details using an order ID.",
        args_schema=OrderInput,
    ),
    StructuredTool.from_function(
        func=get_product,
        name="get_product",
        description="Fetch product details using a product ID.",
        args_schema=ProductInput,
    ),
    StructuredTool.from_function(
        func=search_products,
        name="search_products",
        description="Search products using a keyword.",
        args_schema=SearchInput,
    ),
]


SYSTEM_PROMPT = """You are an AI customer support agent for an online store.

Decide which tool(s) to call based on the customer's question, and call
them in the correct order if more than one is needed.

Rules:
- Always use a tool to look up factual information. Never guess or invent
  order or product details.
- If a tool reports that something was not found, tell the customer
  politely instead of making something up.
- Turn the raw tool output into a short, clear, customer-friendly answer.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])


agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


def run_agent(question: str) -> str:
    """Required entry point: takes a customer question, returns an answer."""
    response = agent_executor.invoke({"input": question})
    return response["output"]


if __name__ == "__main__":
    while True:
        question = input("\nYou : ")
        if question.lower() == "exit":
            break
        print("\nAI :", run_agent(question))