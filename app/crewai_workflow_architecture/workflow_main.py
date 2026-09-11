import os
from IPython.display import Markdown
from datetime import datetime, timezone
from crewai.flow.flow import Flow, listen, router, start
from crewai.flow.persistence import persist
from crewai import Crew
from app.memory import ContentState
from app.crewai_workflow_architecture.tasks import (
    create_blog_tasks,
    create_newsletter_tasks,
    create_linkedin_tasks,
)
from app.crewai_workflow_architecture.agents import (
    create_blog_agents,
    create_newsletter_agents,
    create_linkedin_agents,
)


@persist(verbose=False)
class ContentRouterFlow(Flow[ContentState]):
    """
    A dynamic workflow that routes content creation to specialized crews.

    Flow Overview:
    1. START: Get user input (URL + content type)
    2. ROUTE: Direct to appropriate content crew
    3. PROCESS: Execute specialized content creation
    4. FINISH: Return the final content

    This flow demonstrates:
    - Event-driven architecture with decorators
    - State management across workflow steps
    - Dynamic routing based on user input
    - Parallel processing capabilities
    """

    def __init__(self):
        """
        Enable tracing directly in your Flow
        """
        super().__init__(tracing=True)

    @start()
    def get_user_input(self):
        """Get URL and desired content type from user"""
        return "Input collected"

    @router(get_user_input)
    def route_to_crew(self, previous_result):
        """Route to appropriate crew based on content type"""
        return self.state.content_type

    @listen("blog")
    def process_blog_content(self):
        """Process content using blog crew"""
        researcher, writer = create_blog_agents()
        tasks = create_blog_tasks(researcher, writer, self.state.url)
        blog_crew = Crew(
            agents=[researcher, writer], tasks=tasks, verbose=False
        )
        result = blog_crew.kickoff()
        self.state.final_content = result.raw
        return "Blog content created"

    @listen("newsletter")
    def process_newsletter_content(self):
        """Process content using newsletter crew"""
        researcher, writer = create_newsletter_agents()
        tasks = create_newsletter_tasks(researcher, writer, self.state.url)
        newsletter_crew = Crew(
            agents=[researcher, writer], tasks=tasks, verbose=False
        )
        result = newsletter_crew.kickoff()
        self.state.final_content = result.raw
        return "Newsletter content created"

    @listen("linkedin")
    def process_linkedin_content(self):
        """Process content using LinkedIn crew"""
        researcher, writer = create_linkedin_agents()
        tasks = create_linkedin_tasks(researcher, writer, self.state.url)
        linkedin_crew = Crew(
            agents=[researcher, writer], tasks=tasks, verbose=False
        )
        result = linkedin_crew.kickoff()
        self.state.final_content = result.raw
        return "LinkedIn content created"


if __name__ == "__main__":
    flow = ContentRouterFlow()

    # # pass user inputs to the flow via kickoff(inputs=...).
    # # CrewAI automatically maps those inputs into your flow state
    # # (when the keys match your state fields).
    # url = "https://www.ibm.com/think/topics/agentic-ai"
    # content_type = "blog"
    # result = flow.kickoff(
    #     inputs={
    #         "url": url,
    #         "content_type": content_type
    #     }
    # )

    # If you're building a CLI, gather the input before calling kickoff()
    # because it cleanly separates input collection from workflow execution
    # and makes your flow reusable from a CLI, web app, or API.
    root_path = input("Root Path: ").strip()
    url = input("URL: ").strip()
    while True:
        content_type = (
            input("Content Type (blog/newsletter/linkedin): ").lower().strip()
        )
        if content_type in ["blog", "newsletter", "linkedin"]:
            break

    result = flow.kickoff(inputs={"url": url, "content_type": content_type})

    print(Markdown("## 📝 Generated Content").data)
    print(Markdown("---").data)

    content = str(flow.state.final_content)
    md_data = Markdown(content).data
    print(md_data)

    file_path = root_path + f"/results/{content_type}"
    os.makedirs(file_path, exist_ok=True)

    datetime_utc = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
    with open(
        os.path.join(file_path, f"completion_{datetime_utc}.md"), "w"
    ) as f:
        f.write(md_data)
