import chromadb

DB_DIR = "./chromadb"
chroma_client = chromadb.PersistentClient(path=DB_DIR)

from pypdf import PdfReader

def load_pdf_text(file_path: str):
    """Extracts text from a PDF file using native pypdf."""
    reader = PdfReader(file_path)
    full_text = []
    page_counter = 0
    
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text.append(text)
            page_counter += 1
            
    return "\n".join(full_text), page_counter

# Usage
pdf_text, page_counter = load_pdf_text("documents/bhagavad-gita-in-english-source-file.pdf")
print("Total number of pages in the pdf is : " + str(page_counter))  # Print total number of pages
print("Total document length from the pdf is : " + str(len(pdf_text)))  # Print first 500 characters
collection = chroma_client.get_or_create_collection(name="religious_collection")

from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000 , chunk_overlap = 200 )
documents = text_splitter.split_text(pdf_text)
print("Total number of chunks created from the pdf is : " + str(len(documents)))

ids = [f"page_{i}" for i in range(len(documents))]

# 3. Add documents to the collection
# Chroma automatically generates embeddings if no embedding function is provided
collection.add(
    documents=documents,
    ids=ids
)