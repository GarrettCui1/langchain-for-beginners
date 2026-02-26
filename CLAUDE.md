# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Course Overview

**LangChain for Beginners** is a Microsoft educational course teaching AI application development with LangChain. The course uses an agent-first progression approach, teaching tools → agents → agentic RAG systems to mirror modern production AI systems.

The course consists of 9 chapters (00-setup through 08-agentic-rag-systems), each with:
- `/code` - Step-by-step code examples
- `/samples` - Additional examples
- `/solution` - Challenge solutions
- `README.md` - Chapter content and explanations
- `assignment.md` - Hands-on challenges

## Development Environment

### Prerequisites
- Python 3.10+ required
- GitHub Account (for GitHub Models free access)
- `.env` file with AI provider credentials

### AI Provider Configuration
The course supports two AI providers via environment variables:

**GitHub Models (Free - Recommended for learning):**
- `AI_API_KEY` - GitHub Personal Access Token
- `AI_ENDPOINT=https://models.inference.ai.azure.com`
- `AI_MODEL=gpt-5-mini` (default)
- `AI_EMBEDDING_MODEL=text-embedding-ada-002`

**Microsoft Foundry (Azure - Production use):**
- `AI_API_KEY` - Azure OpenAI API Key
- `AI_ENDPOINT=https://your-resource.openai.azure.com/openai/v1`

### Setup Commands

**Virtual Environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

**Environment File:**
```bash
cp .env.example .env  # Copy and edit with your credentials
```

**Test Setup:**
```bash
python scripts/test_setup.py  # Verifies AI provider connection
```

**Run Any Chapter Code:**
```bash
cd XX-chapter-name/code/
python filename.py
```

## Architecture & Key Directories

### Directory Structure Pattern
Each chapter follows this structure:
```
XX-chapter-name/
├── README.md              # Chapter lessons and walkthroughs
├── assignment.md          # Hands-on challenges
├── code/                  # Step-by-step code files
│   ├── 01_example.py
│   ├── 02_example.py
│   └── ...
├── samples/               # Additional working examples
│   └── advanced_examples.py
└── solution/              # Solutions for assignments
    └── challenge_solution.py
```

### Root Level Directories
- `/00-course-setup/` - Environment setup and test scripts
- `/01-introduction/` - Core LangChain concepts and first LLM call
- `/02-chat-models/` - Chat models, streaming, error handling, token tracking
- `/03-prompts-messages-outputs/` - Prompt engineering, structured outputs, Pydantic schemas
- `/04-function-calling-tools/` - Function calling and tool usage
- `/05-agents/` - Autonomous agents, ReAct pattern, create_agent(), middleware
- `/06-mcp/` - Model Context Protocol (MCP) integration with external services
- `/07-documents-embeddings-semantic-search/` - Document loading, embeddings, vector stores
- `/08-agentic-rag-systems/` - Retrieval-Augmented Generation with agentic decision-making

### Core Dependencies
The project uses LangChain v1.x packages:
- `langchain-openai` - OpenAI-compatible model integration
- `langchain-core` - Core LangChain functionality
- `langchain` - Main LangChain utilities
- `langchain-azure-ai` - Azure-specific integrations
- `langchain-mcp-adapters>=0.1.14` - MCP protocol support

### Development Containers
The project includes GitHub Codespaces support via `.devcontainer/`:
- Automatic Python 3.13 environment setup
- Auto-activation of virtual environment
- Automatic `.env` creation from `.env.example`
- GitHub token integration for seamless setup

## Testing and Validation

**Environment Validation:**
The `scripts/test_setup.py` file tests AI provider connectivity and validates the development environment. Run this to confirm your setup is working correctly before starting chapter exercises.

**Code Validation:**
Most code examples are self-contained and can be run independently. Each typically ends with a test invoke showing expected output format.

## Important Notes

- All code examples are designed to be run independently with `python filename.py`
- The course uses GitHub Models by default (free with GitHub token)
- No special test framework - output is validated manually by running examples
- Environment variables are loaded using `python-dotenv` from `.env` file
- Code uses `ChatOpenAI` class for both OpenAI and GitHub Models endpoints
