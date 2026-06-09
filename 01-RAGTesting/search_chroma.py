import chromadb

DB_DIR = "./chromadb"
chroma_client = chromadb.PersistentClient(path=DB_DIR)
collection = chroma_client.get_or_create_collection(name="religious_collection")

results = collection.query(
        query_texts=["what is the nature of the soul?"], n_results=3
)

print(len(results['ids']))
matches = results["documents"][0]
print(results['ids'][0])
results_text = ""
if(len(matches) > 0):
    for i in range(1,len(matches),1):
        results_text += matches[i] + "\n"

# print(results_text)
