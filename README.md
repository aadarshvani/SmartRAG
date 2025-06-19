# SmartRAG - Intelligent AI Assistant

A sophisticated RAG-based AI assistant built with Streamlit that supports document analysis, web search, and hybrid modes for comprehensive information retrieval.

**Developed by:** Aadarsh Vani - Gen AI Data Scientist

## Features

- **📄 RAG Mode**: Query uploaded PDF documents using advanced retrieval-augmented generation
- **🔍 Search Mode**: Real-time web search capabilities for current information
- **🔄 Hybrid Mode**: Combines document knowledge with web search for comprehensive answers
- **💬 Interactive Chat**: Streamlined chat interface with conversation history
- **📊 Session Management**: Track document processing and conversation statistics

## Installation

1. **Install Python 3.8+:**
   Ensure you have Python 3.8 or higher installed on your system.

2. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd smartrag
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API credentials:**
   - Get your Groq API key from [Groq Console](https://console.groq.com/)
   - Enter the API key in the sidebar when running the application

## Usage

1. **Start the application:**
   ```bash
   streamlit run main.py
   ```

2. **Configure the application:**
   - Enter your Groq API key in the sidebar
   - Upload a PDF document (optional, required for RAG mode)
   - Select your preferred mode (RAG, Search, or Hybrid)

3. **Start chatting:**
   - Type your questions in the chat input
   - The assistant will respond based on your selected mode

## Project Structure

```
smartrag/
├── main.py                     # Main Streamlit application
├── session_state.py           # Session state management
├── styles.py                  # Custom CSS styles
├── document_processor.py      # PDF processing and vectorization
├── search_manager.py          # Web search functionality
├── chat_engine.py             # Chat logic and LLM integration
├── ui_components.py           # UI rendering components
├── prompt_manager.py          # Prompt templates
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Modes Explained

### RAG Only Mode 📄
- Analyzes uploaded PDF documents
- Uses FAISS vector store for efficient similarity search
- Perfect for document-specific queries

### Search Only Mode 🔍
- Performs real-time web searches using DuckDuckGo
- Provides current and up-to-date information
- Ideal for recent events and general knowledge

### Hybrid Mode 🔄
- Combines both document analysis and web search
- Provides comprehensive answers from multiple sources
- Best for complex queries requiring diverse information

## Technical Details

- **LLM**: Groq's Gemma2-9B-IT model
- **Embeddings**: HuggingFace all-MiniLM-L6-v2
- **Vector Store**: FAISS for efficient similarity search
- **Document Processing**: RecursiveCharacterTextSplitter for optimal chunking
- **Search Engine**: DuckDuckGo for web search

## Configuration

### Environment Variables (Optional)
Create a `.env` file for default configurations:
```env
GROQ_API_KEY=your_groq_api_key_here
CHUNK_SIZE=600
CHUNK_OVERLAP=150
```

### Document Processing Parameters
- **Chunk Size**: 600 characters (adjustable)
- **Chunk Overlap**: 150 characters (adjustable)
- **Retrieval**: Top 3 similar chunks per query

## Deployment

### Local Deployment
```bash
streamlit run main.py --server.port 8501
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 8501
CMD ["streamlit", "run", "main.py", "--server.address", "0.0.0.0"]
```

### Cloud Deployment
Compatible with:
- Streamlit Community Cloud
- Heroku
- AWS EC2
- Google Cloud Platform
- Azure Container Instances

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your Groq API key is valid and entered correctly
2. **Document Upload Issues**: Check PDF file size and format
3. **Search Not Working**: Verify internet connection for web search functionality
4. **Memory Issues**: Large PDFs may require system memory adjustments

### Performance Tips

- Keep PDF documents under 50MB for optimal performance
- Use RAG mode for faster responses with uploaded documents
- Clear chat history regularly for better performance

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Aadarsh Vani**  
Gen AI Data Scientist  
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)

## Acknowledgments

- Streamlit for the amazing web framework
- LangChain for the powerful AI orchestration
- Groq for fast LLM inference
- HuggingFace for embedding models