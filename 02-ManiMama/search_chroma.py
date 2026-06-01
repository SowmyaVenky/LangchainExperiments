import chromadb


DB_DIR = "./chromadb"
# Initialize your Chroma vector store
chroma_client = chromadb.PersistentClient(path=DB_DIR)
collection = chroma_client.get_or_create_collection(name="mani_mama_collection")

results = collection.get(
   where={'chapter': {"$eq": "Chapter-02"}}
)

print(len(results['ids']))

if len(results['ids']) > 0:
    for i in range(1,10):
        print(results['ids'][i])
        print(results['metadatas'][i])