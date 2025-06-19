import streamlit as st

def initialize_session_state():
    """Initialize all session state variables"""
    defaults = {
        'chat_history': [],
        'vector_store': None,
        'embedding_model': None,
        'documents_loaded': False,
        'search_tool': None,
        'processed_docs_info': None,
        'selected_mode': 'rag'
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value