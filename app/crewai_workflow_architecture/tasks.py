from crewai import Task, Agent


def create_newsletter_tasks(researcher: Agent, writer: Agent, url: str):
    research_task = Task(
        description=f"""
        Analyze the content from {url} and extract the most newsworthy insights for a newsletter.
        Focus on:
        1. Most important news or updates
        2. Actionable insights subscribers can use immediately
        3. Key statistics or data points
        4. Industry implications
        5. Quick takeaways for busy professionals

        Prioritize information that provides immediate value.
        """,
        expected_output="A focused research summary highlighting the most valuable and actionable insights",
        agent=researcher,
    )
    writing_task = Task(
        description="""
        Create a compelling newsletter section based on the research.

        Requirements:
        - 400-600 words
        - Catchy subject line
        - Scannable format with bullet points
        - Clear action items or takeaways
        - Conversational yet professional tone
        - Include relevant links or resources
        - End with a clear call-to-action

        Format for easy reading in email.
        """,
        expected_output="A complete newsletter section with subject line and formatted content",
        agent=writer,
        context=[research_task],
    )
    return [research_task, writing_task]

def create_blog_tasks(researcher: Agent, writer: Agent, url: str):
    r = Task(
        description=f"""
        Analyze the content from {url} and extract key insights for a blog post.
        Your analysis should identify:
        1. Main themes and key points
        2. Interesting insights or data points
        3. Potential angles for blog content
        4. Target audience considerations
        5. SEO-worthy topics and keywords

        Provide a comprehensive research summary that will guide blog writing.
        """,
        expected_output="A detailed research summary with key insights, themes, and recommendations for blog content",
        agent=researcher,
    )
    w = Task(
        description="""
        Create an engaging blog post based on the research findings.

        Requirements:
        - 800-1200 words
        - Engaging headline
        - Clear introduction with hook
        - Well-structured body with subheadings
        - Actionable insights or takeaways
        - Strong conclusion
        - SEO-optimized content
        - Professional yet accessible tone

        Format the output in markdown.
        """,
        expected_output="A complete, well-structured blog post in markdown format",
        agent=writer,
        context=[r], # integrate research findings as aditional context
    )
    return [r, w]

def create_linkedin_tasks(researcher: Agent, writer: Agent, url: str):
    r = Task(
        description=f"""
        Analyze the content from {url} and extract insights suitable for LinkedIn audience.
        Consider what would engage LinkedIn's professional audience based on the content.
        """,
        expected_output="Research summary focused on professional insights and engagement opportunities",
        agent=researcher,
    )
    w = Task(
        description="""
        Create an engaging LinkedIn post based on the research.

        Requirements:
        - 150-300 words (optimal LinkedIn length)
        - Professional yet conversational tone
        - Include relevant hashtags (3-5)
        - Pose a question to encourage engagement
        - Share a key insight or lesson learned from the content
        - Use line breaks for readability
        - Include a call-to-action for comments

        Make it shareable and discussion-worthy.
        """,
        expected_output="A complete LinkedIn post with hashtags and engagement elements",
        agent=writer,
        context=[r],
    )
    return [r, w]  
