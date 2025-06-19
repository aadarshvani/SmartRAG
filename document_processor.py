import streamlit as st
import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class DocumentProcessor:
    @staticmethod
    def load_pdf(pdf_path: str):
        loader = PyPDFLoader(pdf_path)
        return loader.load()
    
    @staticmethod
    def split_documents(docs, chunk_size=600, chunk_overlap=150):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        return splitter.split_documents(docs)
    
    @staticmethod
    def get_embedding_model():
        return HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    
    @staticmethod
    def create_vector_store(splitted_docs, embedding_model):
        return FAISS.from_documents(splitted_docs, embedding_model)
    
    @staticmethod
    def process_uploaded_pdf(uploaded_file):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name
        
        docs = DocumentProcessor.load_pdf(tmp_file_path)
        splitted_docs = DocumentProcessor.split_documents(docs)
        
        if st.session_state.embedding_model is None:
            st.session_state.embedding_model = DocumentProcessor.get_embedding_model()
        
        vector_store = DocumentProcessor.create_vector_store(splitted_docs, st.session_state.embedding_model)
        st.session_state.vector_store = vector_store
        st.session_state.documents_loaded = True
        st.session_state.processed_docs_info = {
            'filename': uploaded_file.name,
            'pages': len(docs),
            'chunks': len(splitted_docs)
        }
        
        os.unlink(tmp_file_path)
        return len(docs), len(splitted_docs)