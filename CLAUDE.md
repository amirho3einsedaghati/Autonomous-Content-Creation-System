# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository implements an **Autonomous Content Creation System** that uses CrewAI framework to create content (blogs, newsletters, LinkedIn posts) from web URLs through specialized agent workflows. The system demonstrates event-driven architecture with state management, agent specialization, and workflow orchestration.

## High-Level Architecture

### Core Components

**1. Content Router Flow (`app/crewai_workflow_architecture/workflow_main.py`)**
- Event-driven architecture using CrewAI Flow decorators
- Routes content creation to specialized crews based on content type
- Manages state across workflow steps using Pydantic models
- Demonstrates dynamic routing and parallel processing capabilities

**2. Agent System (`app/crewai_workflow_architecture/agents.py`)**
- Three agent types: Blog, Newsletter, and LinkedIn crews
- Each crew consists of a Researcher and Writer agent
- Researchers extract insights and perform web searches
- Writers create content in specified formats and lengths
- Uses OpenRouter LLM with temperature 0.7 for consistent results

**3. Task Management (`app/crewai_workflow_architecture/tasks.py`)**
- Specialized task definitions for each content type
- Clear expected outputs and formatting requirements
- Tasks have context dependencies between research and writing phases
- Specific word count and formatting requirements for each content type

**4. Tools (`app/crewai_workflow_architecture/tools.py`)**
- Web search tool using DuckDuckGo via LangChain
- Enables research agents to gather information from URLs
- Returns formatted search results for content creation

### State Management

**ContentState (`app/memory.py`)**
- Pydantic model managing workflow state
- Tracks: URL input, content type, final content, metadata
- Used across all workflow components for state persistence

## Development Workflow

### Project Structure
```
app/
├── crewai_workflow_architecture/
│   ├── workflow_main.py    # Main flow orchestrator
│   ├── agents.py          # Agent definitions
│   ├── tasks.py           # Task definitions
│   └── tools.py           # Search and tools
├── crewai_workflow_validation/
│   ├── workflow_val.py    # Validation example
│   ├── agents.py          # Local-only agents
│   ├── tasks.py           # Validation tasks
│   └── tools.py           # Knowledge base search
├── memory.py              # State management
├── __init__.py
├── docs/                  # Documentation folder (currently empty)
├── results/               # Generated content output
├── .flake8
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── .venv/
```

### Common Commands

**1. Run the main workflow:**
```bash
cd /home/amir/my\ Projects\ on\ Github/Autonomous-Content-Creation-System
python -m app.crewai_workflow_architecture.workflow_main
```

**2. Run validation example:**
```bash
cd /home/amir/my\ Projects\ on\ Github/Autonomous-Content-Creation-System
python -m app.crewai_workflow_validation.workflow_val
```

**3. Check project structure:**
```bash
find /home/amir/my\ Projects\ on\ Github/Autonomous-Content-Creation-System -type f -name "*.py" | grep -v __pycache__ | grep -v ".venv"
```

**4. View requirements:**
```bash
cat /home/amir/my\ Projects\ on\ Github/Autonomous-Content-Creation-System/requirements.txt
```

### Development Tasks

**New Content Type:**
- Add new agent in `agents.py` (e.g., Twitter content)
- Define tasks in `tasks.py` for the new content type
- Add listener method in `workflow_main.py`
- Update user input validation

**Enhance Existing Content Types:**
- Modify agent backstories/roles in `agents.py`
- Update task descriptions and requirements in `tasks.py`
- Adjust formatting expectations in writer tasks

**Tool Enhancements:**
- Add new tools in `tools.py`
- Update agent tool configurations
- Create specialized search tools for specific domains

**State Management:**
- Add new fields to `ContentState` in `memory.py`
- Update workflow state handling in main flow
- Add state validation and transformation methods

## Architecture Patterns

### 1. Event-Driven Flow
- Uses CrewAI Flow decorators (@start, @router, @listen)
- Clean separation of concerns
- State management across async operations

### 2. Agent Specialization
- Each content type has dedicated agents
- Researchers focus on extraction/analysis
- Writers focus on content creation
- Shared LLM configuration and tools

### 3. Context-Based Tasking
- Research tasks feed into writing tasks
- Clear information flow between agents
- Expected outputs clearly defined

### 4. Persistence
- Workflow state saved to files
- Results stored in organized directory structure
- State management with Pydantic models

## Key Files to Understand

**Critical for workflow understanding:**
- `app/crewai_workflow_architecture/workflow_main.py` - Main orchestrator
- `app/crewai_workflow_architecture/agents.py` - Agent definitions
- `app/crewai_workflow_architecture/tasks.py` - Task specifications
- `app/crewai_workflow_architecture/tools.py` - Available tools

**For validation/testing:**
- `app/crewai_workflow_validation/workflow_val.py` - Validation example
- `app/crewai_workflow_validation/tools.py` - Local knowledge base

**For state management:**
- `app/memory.py` - State model definition

## Code Review Guidelines

When reviewing changes:

1. **Workflow Changes:**
   - Ensure all content types remain supported
   - Verify state management across new/removed methods
   - Check for proper agent/task assignments

2. **Agent Modifications:**
   - Maintain clear role definitions
   - Preserve expected output specifications
   - Update tool configurations appropriately

3. **Task Updates:**
   - Keep expected outputs realistic
   - Ensure context dependencies work correctly
   - Verify formatting requirements are clear

4. **Tool Integration:**
   - Test web search functionality
   - Verify tool responses integrate with agents
   - Check error handling in tools

## Important Considerations

1. **Dependencies:** Extensive requirements.txt with 200+ packages
2. **Environment:** Requires OPENROUTER_API_KEY environment variable
3. **Output Format:** Content is saved in markdown format
4. **State Management:** Pydantic models ensure type safety
5. **Architecture:** Follows CrewAI patterns for agent workflows

This system provides a solid foundation for autonomous content creation with specialized agents for different content formats and comprehensive state management.