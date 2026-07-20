import os
from crewai import LLM, Agent, Crew
from crewai.flow.flow import Flow, listen, router, start
from crewai.flow.persistence import persist
from app.crewai_workflow_architecture.tools import search_tool

AGENT_LLM = LLM(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    model="openrouter/cohere/north-mini-code:free",
    temperature=0.7
)

def create_newsletter_agents():
    researcher = Agent(
        role="Newsletter Content Researcher",
        goal="Extract key insights from preloaded text only.",
        backstory="Local-only researcher.",
        llm=AGENT_LLM,
        tools=[search_tool],
        mode="research",
    )
    writer = Agent(
        role="Newsletter Writer",
        goal="Create a concise newsletter from the research.",
        backstory="Concise, on-brand copy.",
        llm=AGENT_LLM,
        mode="write",
    )
    return researcher, writer

def create_blog_agents():
    researcher = Agent(
        role="Blog Researcher",
        goal="Extract insights strictly from the preloaded text for a blog post.",
        backstory="Local-only researcher.",
        llm=AGENT_LLM,
        tools=[search_tool],
        mode="research",
    )
    writer = Agent(
        role="Blog Writer",
        goal="Write a clear, engaging 600–800 word blog post from the research.",
        backstory="Narrative from bullets.",
        llm=AGENT_LLM,
        mode="write",
    )
    return researcher, writer

def create_linkedin_agents():
    researcher = Agent(
        role="LinkedIn Researcher",
        goal="Extract crisp, high-signal points strictly from the preloaded text.",
        backstory="Local-only researcher.",
        llm=AGENT_LLM,
        tools=[search_tool],
        mode="research",
    )
    writer = Agent(
        role="LinkedIn Writer",
        goal="Write an engaging LinkedIn post with a hook and scannable bullets.",
        backstory="Concise, professional.",
        llm=AGENT_LLM,
        mode="write",
    )
    return researcher, writer  
