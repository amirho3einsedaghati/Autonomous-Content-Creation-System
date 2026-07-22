import nest_asyncio
nest_asyncio.apply()

from crewai.tools import tool


# Local "knowledge base" (no web used for validation purposes)

PRELOADED_TEXT = """
PwC Choses CrewAI to Help Power Their Global Agent OS
PwC has launched Agent OS — with CrewAI as one piece at the core, powering structured orchestration, observability, and secure execution. From 700%+ accuracy gains to global rollout — this is AI in production.

João (Joe) Moura
Jul 30, 2025
2 min

PwC Choses CrewAI to Help Power Their Global Agent OS
Photo by Sean Pollock / Unsplash
Enterprise leaders aren’t just experimenting with AI agents anymore.

They’re deploying them—across operations, systems, and workflows.

We’re seeing it firsthand with our customers, organizations like the U.S. Department of Defense, PepsiCo, RBC, and now—PwC.

PwC has selected CrewAI as one of the foundational layers within their agent OS to enable agent transformation. Not a test. Not a pilot. This is enabling full-scale Enterprise deployment.

Why CrewAI and PwC?
PwC is one of the largest professional services firms in the world—and one of CrewAI’s most advanced customers.

After seeing 700%+ improvements in internal process accuracy using CrewAI-powered agents, this is why PwC is enabling CrewAI within agent OS more broadly.

When it’s time to move from prototype to production—you can build on CrewAI.

Here’s why.

Simple to Start
Proven OSS foundation
No-code builder with Crew Studio
Great integration surface
Reliable, Repeatable Outcomes
Scoped memory, structured flows, secure tool use
Built-in observability and fallback logic
Adaptive agent learning (ALHF, ALAF)
Impossible to Outgrow
Reusable components (agents, tools, flows)
Vendor-neutral, exportable architecture
Enterprise-grade governance and compliance
PwC Launches agent OS with CrewAI
PwC has launched agent OS, a cloud-agnostic, enterprise orchestration platform deployed across client and internal systems to govern and scale AI agents globally.

This is designed to integrate directly with a wide range of third-party tools and capabilities, creating a flexible foundation for agentic workflows.

PwC’s customers can now:

Spin up agents for internal and client-facing workflows
Reuse logic and governance patterns across domains
Monitor and improve agents over time without rebuilding from scratch
Plug into a battle-tested open agent ecosystem
Benefit from enterprise-grade security (RBAC) & secure key management across frameworks and cloud providers
Enable secure agent access to corporate data stores via proven patterns like MCP
And CrewAI is now part of the core foundation.

Through our native support for:

Model Context Protocol (MCP) for scoped agent execution
Agent-to-Agent (A2A) messaging for structured collaboration
Blueprint-mapped orchestration, tool reuse, fallback handling, and full observability
This isn’t about building smarter agents.
It’s about building smarter ecosystems.

If You’re Building for Complexity — Start Here
Whether you’re rolling out your first workflow or deploying agents across departments, here’s what we’ve learned:

You don’t need another agent demo. You need a system.

CrewAI is one of the simplest, most reliable, and most scalable agentic AI suite on the market.

That’s why we’re trusted by the world’s largest organizations—and now natively available through PwC's agent OS.

The future of work will be built on agents.
CrewAI and PwC are scaling agents for the Enterprise.
""".strip()

def _filter_text(query: str, corpus: str) -> str:
    if not query:
        return corpus
    terms = {t.lower() for t in query.split() if len(t) >= 3}
    if not terms:
        return corpus
    paras = [p.strip() for p in corpus.split("\n\n") if p.strip()] # paragraphs
    hits = [p for p in paras if any(t in p.lower() for t in terms)]
    return "\n\n".join(hits) if hits else corpus

@tool("Knowledge Base Search")
def search_tool(query: str) -> str:
    """A Knowledge Base Search tool returns ONLY text from PRELOADED_TEXT (strictly no web)."""
    return _filter_text(query, PRELOADED_TEXT)