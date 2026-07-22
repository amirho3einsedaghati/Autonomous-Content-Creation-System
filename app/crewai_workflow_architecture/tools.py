from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool


# Initialize the search tool
search_tool_instance = DuckDuckGoSearchRun(k=3)

# Wrap the langchain tool with the CrewAI @tool decorator
@tool("DuckDuckGo Search")
def search_tool(query: str) -> str:
    """A Web Search Tool for searching the web using DuckDuckGo."""
    return search_tool_instance.run(query)