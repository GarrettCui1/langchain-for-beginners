from langchain_ollama import OllamaEmbeddings


def emb_text(embeddings: OllamaEmbeddings, text: str, model: str = "qwen3-embedding:0.6b"):
    embedding = embeddings.embed_documents([text])[0]
    # embedding = client.embeddings.create(input=text, model=model).data[0].embedding
    return embedding
