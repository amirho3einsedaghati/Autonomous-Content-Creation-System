import os
from crewai import LLM, Agent

from app.crewai_workflow_architecture.tools import search_tool

AGENT_LLM = LLM(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    model="openrouter/cohere/north-mini-code:free",
    temperature=0.7,
)


def create_newsletter_agents():
    researcher = Agent(
        role="Newsletter Content Researcher",
        goal="Extract key insights from web content for newsletter format",
        backstory="""You are an expert at identifying the most newsworthy and actionable
        insights from web content. You understand what makes content valuable for
        newsletter subscribers and how to present information concisely.""",
        llm=AGENT_LLM,
        tools=[search_tool],
        max_iter=3,
        verbose=False,
    )
    writer = Agent(
        role="Newsletter Writer",
        goal="Create engaging newsletter content that provides immediate value",
        backstory="""You are a newsletter specialist who knows how to craft content
        that busy professionals want to read. You excel at creating scannable,
        actionable content with clear takeaways.""",
        llm=AGENT_LLM,
        verbose=False,
    )
    return researcher, writer


def create_blog_agents():
    researcher = Agent(
        role="Blog Content Researcher",
        goal="Extract and analyze web content to identify key insights for blog posts",
        backstory="""You are an expert content researcher who specializes in analyzing
        web content and identifying the most valuable insights for creating engaging blog posts.
        You excel at understanding complex topics and breaking them down into digestible content.""",
        llm=AGENT_LLM,
        tools=[search_tool],
        verbose=False,
        max_iter=3,
    )
    writer = Agent(
        role="Blog Content Writer",
        goal="Transform research into engaging, well-structured blog posts",
        backstory="""You are a skilled blog writer with expertise in creating compelling
        content that engages readers and drives meaningful discussions. You excel at taking
        complex information and making it accessible and interesting.""",
        llm=AGENT_LLM,
        verbose=False,
    )
    return researcher, writer


def create_linkedin_agents():
    researcher = Agent(
        role="LinkedIn Content Researcher",
        goal="Extract professional insights suitable for LinkedIn audience",
        backstory="""You are an expert at identifying professional insights and industry
        trends that resonate with LinkedIn's professional audience. You understand what
        content drives engagement on professional networks.""",
        llm=AGENT_LLM,
        tools=[search_tool],
        verbose=False,
        max_iter=3,
    )
    writer = Agent(
        role="LinkedIn Content Writer",
        goal="Create engaging LinkedIn posts that drive professional engagement",
        backstory="""You are a LinkedIn content specialist who knows how to craft posts
        that get noticed in the professional feed. You excel at creating content
        that sparks meaningful professional discussions.""",
        llm=AGENT_LLM,
    )
    return researcher, writer
