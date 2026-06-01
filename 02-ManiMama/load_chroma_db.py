import chromadb

DB_DIR = "./chromadb"
# Initialize your Chroma vector store
chroma_client = chromadb.PersistentClient(path=DB_DIR)

collection = chroma_client.get_or_create_collection(name="mani_mama_collection")

# transcript_file = 'videos/001.txt'
# transcript_file = 'videos/002.txt'
# transcript_file = 'videos/003.txt'
# transcript_file = 'videos/004.txt'
transcript_file = 'videos/005.txt'

# Open the file safely
with open(transcript_file, 'r', encoding='utf-8') as file:
    content = file.read()
    
    # Split by a specific delimiter (e.g., a comma)
    tokens = content.split('--------------------------------------------------')

for atoken in tokens:
    tokenarr = atoken.split("] ")
    if len(tokenarr) == 2:
        doc_id = transcript_file + tokenarr[0].strip() + "] "
        collection.add(documents=[tokenarr[1]], ids=[doc_id])
        print("Added " + doc_id)