import streamlit as st
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool

class SearchManager:
    @staticmethod
    def get_search_tool():
        search = DuckDuckGoSearchRun()
        return Tool(
            name="web_search",
            description="Search the web for current information",
            func=search.run
        )
    
    @staticmethod
    def web_search(query: str) -> str:
        if st.session_state.search_tool is None:
            st.session_state.search_tool = SearchManager.get_search_tool()
        
        results = st.session_state.search_tool.func(query)
        return results[:1000]