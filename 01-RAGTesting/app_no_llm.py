import streamlit as st
import ollama

from langchain_ollama import ChatOllama
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_chroma import Chroma

import chromadb

DB_DIR = "./chromadb"
chroma_client = chromadb.PersistentClient(path=DB_DIR)
collection = chroma_client.get_or_create_collection(name="religious_collection")

def query_after_getting_matched_documents(user_query):
    results = collection.query(
            query_texts=[user_query], n_results=3
    )

    print(len(results['ids']))
    print(results['ids'])
    matches = results["documents"][0]
    results_text = ""
    if(len(matches) > 0):
        for i in range(1,len(matches),1):
            results_text += matches[i] + "\n"

    return {"answer": results_text, "source_documents": []}

st.title("💬 Gita Chatbot")

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
