from IPython.display import display, Markdown
from crewai.flow.flow import Flow, listen, router, start
from crewai.flow.persistence import persist
from crewai import Crew
from app.memory import ContentState
from app.tasks import (
    create_blog_tasks,
    create_newsletter_tasks,
    create_linkedin_tasks
)
from app.crewai_workflow_validation.agents import (
    create_blog_agents,
    create_newsletter_agents,
    create_linkedin_agents
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

    @start()
    def get_user_input(self):
        """Get URL and desired content type from user"""
        url = "https://blog.crewai.com/pwc-choses-crewai/"
        content_type = "newsletter"
        self.state.url = url
        self.state.content_type = content_type
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
            agents=[researcher, writer],
            tasks=tasks,
            verbose=False
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
            agents=[researcher, writer],
            tasks=tasks,
            verbose=False
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
            agents=[researcher, writer],
            tasks=tasks,
            verbose=False
        )
        result = linkedin_crew.kickoff()
        self.state.final_content = result.raw
        return "LinkedIn content created"


if __name__ == "__main__":
    flow = ContentRouterFlow()
    result = flow.kickoff()  

    print(Markdown("## 📝 Generated Content").data)
    print(Markdown("---").data)

    content = str(flow.state.final_content)
    print(Markdown(content).data)

    print(Markdown("## Flow State Summary").data)
    print(Markdown(f"URL: {flow.state.url}").data)
    print(Markdown(f"Content Type: {flow.state.content_type}").data)
    print(Markdown(f"Final Content Length: {len(str(flow.state.final_content)).data} characters"))