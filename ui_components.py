import streamlit as st
from document_processor import DocumentProcessor

class UIComponents:
    @staticmethod
    def render_sidebar():
        """Render sidebar with Streamlit components only"""
        with st.sidebar:
            st.header("🧠 SmartRAG")
            st.caption("Intelligent Document & Web Assistant")
            
            # API Key Section
            st.subheader("🔑 API Configuration")
            groq_api_key = st.text_input(
                "Groq API Key",
                type="password",
                placeholder="Enter your Groq API key...",
                help="Get your API key from Groq Console"
            )
            
            st.divider()
            
            # Document Upload Section
            st.subheader("📁 Document Upload")
            uploaded_file = st.file_uploader(
                "Upload PDF Document",
                type="pdf",
                help="Upload a PDF file to enable RAG functionality"
            )
            
            if uploaded_file:
                if st.button("📤 Process Document", key="process_btn", use_container_width=True):
                    with st.spinner("🔄 Processing document..."):
                        DocumentProcessor.process_uploaded_pdf(uploaded_file)
                    st.rerun()
            
            # Document Status
            if st.session_state.documents_loaded and st.session_state.processed_docs_info:
                info = st.session_state.processed_docs_info
                st.success(f"✅ **{info['filename']}**  \n📄 {info['pages']} pages • 🔤 {info['chunks']} chunks")
            
            st.divider()
            
            # Session Statistics
            st.subheader("📊 Session Statistics")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("💬 Messages", len(st.session_state.chat_history))
            with col2:
                st.metric("📄 Documents", "✅" if st.session_state.documents_loaded else "❌")
            
            st.divider()
            
            # Clear Chat Button
            if st.button("🗑️ Clear Chat History", key="clear_btn", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()
        
        return groq_api_key, uploaded_file
    
    @staticmethod
    def render_chat_interface():
        """Render chat interface with Streamlit components only"""
        st.title("🧠 SmartRAG Assistant")
        st.caption("Your intelligent companion for document analysis and web search")
        
        if st.session_state.chat_history:
            for chat in st.session_state.chat_history:
                with st.chat_message("user"):
                    st.markdown(chat["user"])
                with st.chat_message("assistant"):
                    st.markdown(chat["assistant"])
        else:
            st.info("👋 **Welcome to SmartRAG!**  \nYour intelligent assistant for document analysis and web search")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("**🔑 Add API Key**  \nEnter your Groq API key in the sidebar")
            with col2:
                st.markdown("**📄 Upload Document**  \nOptional: Upload a PDF for document-based queries")
            with col3:
                st.markdown("**💬 Start Chatting**  \nType your question and select your preferred mode")
    
    @staticmethod
    def render_mode_selector():
        """Render enhanced mode selector with custom styling"""
        
        # Create columns for mode selection
        col1, col2, col3 = st.columns(3)
        
        modes = [
            {"key": "rag", "title": "RAG Only", "icon": "📄", "desc": "Document-based responses"},
            {"key": "search", "title": "Search Only", "icon": "🔍", "desc": "Web search responses"},
            {"key": "hybrid", "title": "Hybrid", "icon": "🔄", "desc": "Combined approach"}
        ]
        
        cols = [col1, col2, col3]
        
        for i, mode in enumerate(modes):
            with cols[i]:
                if st.button(
                    f"{mode['icon']} {mode['title']}\n{mode['desc']}", 
                    key=f"mode_{mode['key']}",
                    use_container_width=True
                ):
                    st.session_state.selected_mode = mode['key']
        
        # Display current mode
        current_mode = st.session_state.selected_mode
        mode_names = {"rag": "RAG Only", "search": "Search Only", "hybrid": "Hybrid"}
        mode_descs = {
            "rag": "📄 Using uploaded document knowledge",
            "search": "🔍 Using real-time web search",
            "hybrid": "🔄 Using both documents and web search"
        }
        
        st.markdown(f"""
        <div class="current-mode-indicator">
            <strong>Current Mode: {mode_names[current_mode]}</strong><br>
            <small>{mode_descs[current_mode]}</small>
        </div>
        """, unsafe_allow_html=True)
        
        return current_mode
    
    @staticmethod
    def validate_inputs(groq_api_key: str, selected_mode: str) -> tuple:
        """Validate user inputs and return validation status"""
        if not groq_api_key:
            return False, "⚠️ Please enter your Groq API key in the sidebar"
        
        if selected_mode in ["rag", "hybrid"] and not st.session_state.documents_loaded:
            return False, "⚠️ Please upload and process a document for RAG/Hybrid mode"
        
        return True, ""