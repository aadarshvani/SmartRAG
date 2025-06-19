import streamlit as st
from typing import List, Dict
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda
from search_manager import SearchManager
from prompt_manager import PromptManager

class ChatEngine:
    @staticmethod
    def get_llm(api_key: str):
        return ChatGroq(model="gemma2-9b-it", api_key=api_key)
    
    @staticmethod
    def format_chat_history(chat_history: List[Dict]) -> str:
        if not chat_history:
            return "No previous conversation"
        
        formatted = []
        for chat in chat_history[-3:]:
            formatted.append(f"User: {chat['user'][:100]}...")
            formatted.append(f"Assistant: {chat['assistant'][:100]}...")
        
        return "\n".join(formatted)
    
    @staticmethod
    def build_rag_chain(vector_store, llm, mode="rag"):
        retriever = vector_store.as_retriever(search_kwargs={"k": 3}) if vector_store else None

        def process_query(inputs):
            question = inputs["question"]
            context = ""
            web_results = ""
            chat_history = ChatEngine.format_chat_history(st.session_state.chat_history)
            
            if mode in ["rag", "hybrid"] and retriever:
                docs = retriever.invoke(question)
                context = "\n\n".join([doc.page_content for doc in docs])
            
            if mode in ["search", "hybrid"]:
                web_results = SearchManager.web_search(question)
            
            return {
                "context": context,
                "web_results": web_results,
                "question": question,
                "chat_history": chat_history
            }

        # Select prompt based on mode
        if mode == "rag":
            prompt = PromptManager.get_rag_prompt()
        elif mode == "search":
            prompt = PromptManager.get_search_prompt()
        else:
            prompt = PromptManager.get_hybrid_prompt()
        
        rag_chain = (
            RunnableLambda(process_query)
            | prompt
            | llm
        )
        
        return rag_chain
    
    @staticmethod
    def get_response(user_input: str, groq_api_key: str, mode: str = "rag"):
        llm = ChatEngine.get_llm(groq_api_key)
        rag_chain = ChatEngine.build_rag_chain(st.session_state.vector_store, llm, mode)
        result = rag_chain.invoke({"question": user_input})
        return result.content