from langchain_core.prompts import PromptTemplate

class PromptManager:
    @staticmethod
    def get_rag_prompt():
        return PromptTemplate.from_template(
            """You are SmartRAG, an intelligent AI assistant. Use the document context to answer the question accurately.

Context: {context}
Question: {question}
Chat History: {chat_history}

Answer based on the context provided:"""
        )
    
    @staticmethod
    def get_search_prompt():
        return PromptTemplate.from_template(
            """You are SmartRAG, an AI assistant with web search capabilities. Use the search results to provide current information.

Search Results: {web_results}
Question: {question}
Chat History: {chat_history}

Answer based on the search results:"""
        )
    
    @staticmethod
    def get_hybrid_prompt():
        return PromptTemplate.from_template(
            """You are SmartRAG, an intelligent AI assistant with access to documents and web search. Provide comprehensive answers using both sources.

Document Context: {context}
Web Search Results: {web_results}
Question: {question}
Chat History: {chat_history}

Answer using both document context and search results:"""
        )