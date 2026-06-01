import chromadb


DB_DIR = "./chromadb"
# Initialize your Chroma vector store
chroma_client = chromadb.PersistentClient(path=DB_DIR)

collection = chroma_client.get_or_create_collection(name="mani_mama_collection")

results = collection.query(
    query_texts=["Why is the symbolism of cow"],
    n_results = 5
)

print(results)