"""
Vector Store and Semantic Search

Run: python 07-documents-embeddings-semantic-search/code/06_vector_store.py

🤖 Try asking GitHub Copilot Chat (https://github.com/features/copilot):
- "What's the difference between InMemoryVectorStore and persistent stores like Pinecone?"
- "Can I save and load a vector store to avoid recomputing embeddings?"
"""

import os
import certifi
import ssl

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import AzureOpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from milvus_utils import get_milvus_client, create_collection, get_search_results
from encoder import emb_text
from tqdm import tqdm

load_dotenv()

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
MILVUS_ENDPOINT = os.getenv("MILVUS_ENDPOINT")
MILVUS_TOKEN = os.getenv("MILVUS_TOKEN")


def get_embeddings_endpoint():
    """Get the Azure OpenAI endpoint, removing /openai/v1 suffix if present."""
    endpoint = os.getenv("AI_ENDPOINT", "")
    if endpoint.endswith("/openai/v1"):
        endpoint = endpoint.replace("/openai/v1", "")
    elif endpoint.endswith("/openai/v1/"):
        endpoint = endpoint.replace("/openai/v1/", "")
    return endpoint


def main():
    print("🗄️  Vector Store and Semantic Search\n")

    # embeddings = AzureOpenAIEmbeddings(
    #     azure_endpoint=get_embeddings_endpoint(),
    #     api_key=os.getenv("AI_API_KEY"),
    #     model=os.getenv("AI_EMBEDDING_MODEL", "text-embedding-ada-002"),
    #     api_version="2024-02-01",
    # )

    embeddings = OllamaEmbeddings(
        model=os.getenv("AI_EMBEDDING_MODEL", "qwen3-embedding:0.6b"),
    )

    # Create documents about different topics
    docs = [
        Document(
            page_content="Python is a popular programming language for data science and machine learning.",
            metadata={"category": "programming", "language": "python"},
        ),
        Document(
            page_content="JavaScript is widely used for web development and building interactive websites.",
            metadata={"category": "programming", "language": "javascript"},
        ),
        Document(
            page_content="Machine learning algorithms can identify patterns in large datasets.",
            metadata={"category": "AI", "topic": "machine-learning"},
        ),
        Document(
            page_content="Neural networks are inspired by the human brain and used in deep learning.",
            metadata={"category": "AI", "topic": "deep-learning"},
        ),
        Document(
            page_content="Cats are independent pets that enjoy napping and hunting mice.",
            metadata={"category": "animals", "type": "mammals"},
        ),
        Document(
            page_content="Dogs are loyal companions that love playing fetch and going for walks.",
            metadata={"category": "animals", "type": "mammals"},
        ),
    ]

    print(f"📚 Creating vector store with {len(docs)} documents...\n")

    # Get clients
    milvus_client = get_milvus_client(uri=MILVUS_ENDPOINT, token=MILVUS_TOKEN)

    # Set SSL context
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    embeddings = OllamaEmbeddings(
        model=os.getenv("AI_EMBEDDING_MODEL", "qwen3-embedding:0.6b"),
    )

    # Create collection
    dim = len(emb_text(embeddings, "test"))
    create_collection(milvus_client=milvus_client, collection_name=COLLECTION_NAME, dim=dim)

    # Insert data
    data = []
    count = 0
    for doc in tqdm(docs, desc="Creating embeddings"):
        try:
            vector = emb_text(embeddings, doc.page_content)
            data.append({"vector": vector, "text": doc.page_content})
            count += 1
        except Exception as e:
            print(
                f"Skipping document due to an error during the embedding process:\n{e}"
            )
            continue
    print("Total number of loaded documents:", count)

    # Insert data into Milvus collection
    mr = milvus_client.insert(collection_name=COLLECTION_NAME, data=data)
    print("Total number of entities/chunks inserted:", mr["insert_count"])

    # Create vector store
    # vector_store = InMemoryVectorStore.from_documents(docs, embeddings)

    print("✅ Vector store created!\n")
    print("=" * 80 + "\n")

    # Perform semantic searches
    searches = [
        {"query": "programming languages for AI", "k": 2},
        {"query": "pets that need exercise", "k": 2},
        {"query": "building websites", "k": 2},
        {"query": "understanding data patterns", "k": 2},
    ]

    for search in searches:
        query = search["query"]
        k = search["k"]
        print(f'🔍 Search: "{query}" (top {k} results)\n')



        # Generate query embedding
        query_vector = emb_text(embeddings, query)
        # Search in Milvus collection
        search_res = get_search_results(
            milvus_client, COLLECTION_NAME, query_vector, ["text"]
        )

        # Retrieve lines and distances
        retrieved_lines_with_distances = [
            (res["entity"]["text"], res["distance"]) for res in search_res[0]
        ]

        # Create context from retrieved lines
        context = "\n".join(
            [
                line_with_distance[0]
                for line_with_distance in retrieved_lines_with_distances
            ]
        )

        # results = vector_store.similarity_search(query, k=k)

        print(f"   {context}")

        print("─" * 80 + "\n")

    print("=" * 80)
    print("\n💡 Key Insights:")
    print("   - Vector stores enable fast similarity search over documents")
    print("   - Semantic search finds relevant content even without exact keyword matches")
    print("   - Metadata helps categorize and filter results")


if __name__ == "__main__":
    main()
