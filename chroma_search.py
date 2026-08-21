from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings


load_dotenv()


documents = [
    Document(
        page_content="""
        LangGraph is a framework for building stateful, multi-actor applications
        with LLMs. It allows developers to define workflows as graphs consisting
        of nodes and edges.
        """,
        metadata={
            "source": "langgraph_intro.txt"
        }
    ),

    Document(
        page_content="""
        LangChain is a framework for developing applications powered by language
        models. It provides abstractions for prompts, models, tools, retrievers,
        agents, and document processing.
        """,
        metadata={
            "source": "langchain_intro.txt"
        }
    ),

    Document(
        page_content="""
        Retrieval-Augmented Generation, or RAG, combines document retrieval with
        language model generation. Relevant documents are retrieved from a vector
        database and provided to the LLM as context.
        """,
        metadata={
            "source": "rag_intro.txt"
        }
    ),

    Document(
        page_content="""
        Vector databases store numerical representations called embeddings.
        During retrieval, a query embedding is compared against stored document
        embeddings to find semantically similar content.
        """,
        metadata={
            "source": "vector_database.txt"
        }
    ),
]

print(documents[0].page_content)

embeddings=OpenAIEmbeddings(model="text-embedding-3-small")

vector_store=Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="basic_rag_learning",
)

query="What is vector database?"
results=vector_store.similarity_search(
    query=query,
    k=2
)

for index, result in enumerate(results):

    print(f"Result {index+1}:")
    print(result.page_content)
    print("_________________")
    print(result.metadata["source"])
