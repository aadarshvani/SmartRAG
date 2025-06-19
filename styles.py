import streamlit as st

def load_custom_css():
    st.markdown("""
    <style>
    /* Mode selector styling */
    .mode-selector {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .mode-header {
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }
    
    .mode-header h3 {
        margin: 0;
        font-size: 1.8em;
        font-weight: 600;
    }
    
    .mode-options {
        display: flex;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap;
    }
    
    .mode-card {
        background: rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        color: white;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        min-width: 150px;
        flex: 1;
        max-width: 200px;
    }
    
    .mode-card:hover {
        background: rgba(255,255,255,0.3);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .mode-card.active {
        background: rgba(255,255,255,0.4);
        border-color: rgba(255,255,255,0.6);
        transform: translateY(-2px);
    }
    
    .mode-icon {
        font-size: 2.5em;
        margin-bottom: 10px;
        display: block;
    }
    
    .mode-title {
        font-weight: 600;
        margin-bottom: 8px;
        font-size: 1.1em;
    }
    
    .mode-desc {
        font-size: 0.85em;
        opacity: 0.9;
        line-height: 1.3;
    }
    
    /* Current mode indicator */
    .current-mode-indicator {
        text-align: center; 
        margin: 15px 0; 
        padding: 10px; 
        background: rgba(255,255,255,0.1); 
        border-radius: 10px; 
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)