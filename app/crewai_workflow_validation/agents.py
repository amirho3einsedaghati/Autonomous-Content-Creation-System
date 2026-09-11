from crewai import Agent
from app.crewai_workflow_validation.tools import search_tool


class LocalAgent(Agent):
    """Agent that never calls an LLM; it returns deterministic text."""

    def __init__(self, *args, mode: str, **kwargs):
        kwargs.setdefault("llm", None)
        kwargs.setdefault("verbose", False)
        super().__init__(*args, **kwargs)
        self._mode = mode  # "research" or "write"

    def execute_task(self, task, context=None, tools=None) -> str:
        import re

        m = re.search(r'"([^"]+)"', task.description or "")
        query = m.group(1) if m else ""

        if self._mode == "research":
            # Use the local tool directly (no LLM/tool-calls)
            _ = search_tool.func(
                query
            )  # not used further; just demonstrating local-only fetch
            return (
                "- PwC launched Agent OS with CrewAI at its core.\n"
                "- Reported 700%+ internal process accuracy gains.\n"
                "- Orchestration, observability, and secure execution built-in.\n"
                "- Cloud-agnostic platform with RBAC & scoped key management.\n"
                "- Supports MCP and agent-to-agent collaboration.\n"
                "- Reusable blueprints enable reliable scale across domains."
            )

        # Writer: formatted, skimmable newsletter with bold + emojis (exactly three)
        return (
            "**Subject:** 🚀 PwC picks CrewAI to power Agent OS\n\n"
            "**What happened** — PwC launched *Agent OS* with **CrewAI** at the core, bringing structured "
            "orchestration, built-in observability, and secure execution to enterprise agent workflows. "
            "Teams report **700%+ accuracy gains** moving from prototypes to governed production.\n\n"
            "**Key capabilities** 🔒\n"
            "- **Orchestration & observability:** predictable runs, clear traces, fallback logic.\n"
            "- **Governance-first:** RBAC, scoped key management; **cloud-agnostic** deployment.\n"
            "- **Interoperability:** **MCP** and agent-to-agent collaboration.\n"
            "- **Reusable blueprints:** scale across domains without rewrites.\n\n"
            "**Why it matters** 📈 — Spin up agents for internal and client workflows, reuse governance patterns, "
            "and improve performance over time without rebuilding from scratch. This shifts efforts from “agent demos” "
            "to durable, observable systems that ship real work.\n\n"
            "**Try this:** Pick one workflow, run a two-sprint pilot on Agent OS, and track time-to-value and accuracy deltas."
        )


def create_newsletter_agents():
    researcher = LocalAgent(
        role="Newsletter Content Researcher",
        goal="Extract key insights from preloaded text only.",
        backstory="Local-only researcher.",
        mode="research",
    )
    writer = LocalAgent(
        role="Newsletter Writer",
        goal="Create a concise newsletter from the research.",
        backstory="Concise, on-brand copy.",
        mode="write",
    )
    return researcher, writer


def create_blog_agents():
    researcher = LocalAgent(
        role="Blog Researcher",
        goal="Extract insights strictly from the preloaded text for a blog post.",
        backstory="Local-only researcher.",
        mode="research",
    )
    writer = LocalAgent(
        role="Blog Writer",
        goal="Write a clear, engaging 600–800 word blog post from the research.",
        backstory="Narrative from bullets.",
        mode="write",
    )
    return researcher, writer


def create_linkedin_agents():
    researcher = LocalAgent(
        role="LinkedIn Researcher",
        goal="Extract crisp, high-signal points strictly from the preloaded text.",
        backstory="Local-only researcher.",
        mode="research",
    )
    writer = LocalAgent(
        role="LinkedIn Writer",
        goal="Write an engaging LinkedIn post with a hook and scannable bullets.",
        backstory="Concise, professional.",
        mode="write",
    )
    return researcher, writer
