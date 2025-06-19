import streamlit as st
from datetime import datetime

# Import modular components
from session_state import initialize_session_state
from styles import load_custom_css
from ui_components import UIComponents
from chat_engine import ChatEngine

def main():
    st.set_page_config(
        page_title="SmartRAG - AI Assistant",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Load custom CSS
    load_custom_css()
    
    initialize_session_state()
    
    # Render sidebar
    groq_api_key, uploaded_file = UIComponents.render_sidebar()
    
    # Main content area
    UIComponents.render_chat_interface()
    
    # Chat input
    user_input = st.chat_input("💭 Type your message here...", key="main_chat_input")
    
    # Mode selector
    selected_mode = UIComponents.render_mode_selector()
    
    if user_input:
        # Validate inputs
        is_valid, error_message = UIComponents.validate_inputs(groq_api_key, selected_mode)
        
        if not is_valid:
            st.error(error_message)
            return
        
        # Add user message to chat history
        st.session_state.chat_history.append({
            "user": user_input,
            "assistant": "🤔 Thinking...",
            "timestamp": datetime.now().isoformat()
        })
        
        # Generate response
        with st.spinner(f"🚀 Processing with {selected_mode.upper()} mode..."):
            response = ChatEngine.get_response(user_input, groq_api_key, selected_mode)
        
        # Update chat history with response
        st.session_state.chat_history[-1]["assistant"] = response
        
        st.rerun()

if __name__ == "__main__":
    main()