from crewai import Task, Agent


def create_newsletter_tasks(researcher: Agent, writer: Agent, url: str):
    research_task = Task(
        description=f"""
        Using ONLY the Knowledge Base Search tool (no web), extract the most relevant insights
        about: "{url}" from the preloaded text. Return:
        - 5–8 concise bullets
        - Concrete stats/claims/entities mentioned
        - 1–2 brief implications for enterprise readers
        """.strip(),
        expected_output="A compact research brief with 5–8 bullets, stats, and implications.",
        agent=researcher,
    )
    writing_task = Task(
        description="""
        Convert the research brief into a newsletter-ready section.

        Requirements:
        - ~350–450 words
        - Punchy subject line
        - Skimmable structure (short paragraphs + bullets)
        - Clear takeaways for busy professionals
        - End with a concise call to action
        """.strip(),
        expected_output="A complete newsletter section including a subject line and formatted copy.",
        agent=writer,
        context=[research_task],
    )
    return [research_task, writing_task]

def create_blog_tasks(researcher: Agent, writer: Agent, url: str):
    r = Task(
        description=f'Use ONLY Knowledge Base Search to extract blog-ready insights about "{url}".',
        expected_output="8–10 structured bullets with any concrete stats and short commentary.",
        agent=researcher,
    )
    w = Task(
        description="Write a 600–800 word blog post with intro, 2–3 sections, and a short conclusion.",
        expected_output="A polished blog post (markdown-ok).",
        agent=writer,
        context=[r],
    )
    return [r, w]

def create_linkedin_tasks(researcher: Agent, writer: Agent, url: str):
    r = Task(
        description=f'Use ONLY Knowledge Base Search to pull punchy insights about "{url}".',
        expected_output="5–7 tight bullets with a clear takeaway.",
        agent=researcher,
    )
    w = Task(
        description="Write a LinkedIn post (120–220 words) with a hook, bullets, and a soft CTA.",
        expected_output="A finalized LinkedIn post ready to paste.",
        agent=writer,
        context=[r],
    )
    return [r, w]  
