import chromadb

DB_DIR = "./chromadb"
# Initialize your Chroma vector store
chroma_client = chromadb.PersistentClient(path=DB_DIR)

collection = chroma_client.get_or_create_collection(name="mani_mama_collection")

#These are the metadata tagst to apply to use with the corresponding text file we are loading.
# metadata_tags_to_apply = {'chapter_and_slokas': 'Introduction and Dhyana Slokas 1 to 3', 'chapter': 'Introduction and Dhyana Slokas' }
# metadata_tags_to_apply = {'chapter_and_slokas': 'Introduction and Dhyana Slokas 4 to 8', 'chapter': 'Introduction and Dhyana Slokas' }
# metadata_tags_to_apply = {'chapter_and_slokas': 'Chapter-01-Slokas-1-to-23', 'chapter': 'Chapter-01' }
metadata_tags_to_apply = {'chapter_and_slokas': 'Chapter-01-Slokas-24-to-42', 'chapter': 'Chapter-01' }
# metadata_tags_to_apply = {'chapter_and_slokas': 'Chapter-01-sloka-43-to-47', 'chapter': 'Chapter-01' }
# metadata_tags_to_apply = {'chapter_and_slokas': 'Chapter-02-slokas-12-to-17', 'chapter': 'Chapter-02' }

# transcript_file = 'videos/001.txt'
# transcript_file = 'videos/002.txt'
# transcript_file = 'videos/003.txt'
transcript_file = 'videos/004.txt'
# transcript_file = 'videos/005.txt'
# transcript_file = 'videos/006.txt'

# Open the file safely
with open(transcript_file, 'r', encoding='utf-8') as file:
    content = file.read()
    
    # Split by a specific delimiter (e.g., a comma)
    tokens = content.split('--------------------------------------------------')

for atoken in tokens:
    tokenarr = atoken.split("] ")
    if len(tokenarr) == 2:
        doc_id = transcript_file + tokenarr[0].strip() + "] "
        thisdocmetadata = {}
        thisdocmetadata['doc_id'] = doc_id
        thisdocmetadata['chapter_and_slokas'] = metadata_tags_to_apply['chapter_and_slokas']
        thisdocmetadata['chapter'] = metadata_tags_to_apply['chapter']
        collection.upsert(documents=[tokenarr[1]], ids=[doc_id], metadatas=[thisdocmetadata])
        print("Added " + doc_id + str(thisdocmetadata))