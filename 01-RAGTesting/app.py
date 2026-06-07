import streamlit as st
import ollama

from langchain_ollama import ChatOllama
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_chroma import Chroma

import chromadb

DB_DIR = "./chromadb"
chroma_client = chromadb.PersistentClient(path=DB_DIR)
collections = chroma_client.list_collections()
print("Collections in ChromaDB:", collections)

vector_store = Chroma(collection_name="religious_collection", client=chroma_client)

def query_after_getting_matched_documents(user_query, ollama_model_name="granite4.1:3b"):
    # Create a retriever from the vector store getting top 10 similar documents
    retriever = vector_store.as_retriever(collection_name="religious_collection", search_type="similarity", search_kwargs={"k": 10})

    llm = ChatOllama(model=ollama_model_name, base_url=None)
    # ConversationalRetrievalChain wraps the LLM + retriever
    chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, return_source_documents=True)

    result = chain.invoke({"question": user_query, "chat_history":[]})
    print(result["answer"])
    matching_docs = result["source_documents"]
    print("Matching document IDs:")
    for doc in matching_docs:
        print(doc.id)

    return result

st.title("💬 Gita/Tattvabodha/Atmabodha Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        result = query_after_getting_matched_documents(prompt) 
        full_response += result['answer']
        matching_docs = result["source_documents"]
        
        full_response += "\n\n References: "
        for doc in matching_docs:
            full_response += "  \n" + str(doc.id)
        
        response_placeholder.markdown(full_response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
