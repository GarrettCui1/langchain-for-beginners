# CLAUDE.cn.md

此文件为 Claude Code (claude.ai/code) 在使用本仓库代码时提供指导。

## 课程概述

**LangChain 初学者课程** 是微软的教育课程，教授使用 LangChain 进行 AI 应用开发。课程采用"以 Agent 为先"的教学方法，依次教授工具 → Agent → Agentic RAG 系统，以反映现代生产级 AI 系统的构建方式。

课程包含 9 个章节（00-环境搭建 到 08-Agentic RAG 系统），每个章节都包含：
- `/code` - 逐步代码示例
- `/samples` - 额外示例
- `/solution` - 挑战题解答
- `README.md` - 章节内容和讲解
- `assignment.md` - 实践挑战

## 开发环境

### 前置要求
- Python 3.10+ 必需
- GitHub 账户（用于免费访问 GitHub Models）
- `.env` 文件包含 AI 提供商凭据

### AI 提供商配置
课程通过环境变量支持两种 AI 提供商：

**GitHub Models（免费 - 推荐用于学习）：**
- `AI_API_KEY` - GitHub 个人访问令牌
- `AI_ENDPOINT=https://models.inference.ai.azure.com`
- `AI_MODEL=gpt-5-mini`（默认）
- `AI_EMBEDDING_MODEL=text-embedding-ada-002`

**Microsoft Foundry（Azure - 生产环境使用）：**
- `AI_API_KEY` - Azure OpenAI API 密钥
- `AI_ENDPOINT=https://your-resource.openai.azure.com/openai/v1`

### 设置命令

**虚拟环境：**
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

**环境文件：**
```bash
cp .env.example .env  # 复制并使用您的凭据进行编辑
```

**测试设置：**
```bash
python scripts/test_setup.py  # 验证 AI 提供商连接
```

**运行任意章节代码：**
```bash
cd XX-chapter-name/code/
python filename.py
```

## 架构与关键目录

### 目录结构模式
每个章节遵循以下结构：
```
XX-chapter-name/
├── README.md              # 章节课程和演练
├── assignment.md          # 实践挑战
├── code/                  # 分步代码文件
│   ├── 01_example.py
│   ├── 02_example.py
│   └── ...
├── samples/               # 额外工作示例
│   └── advanced_examples.py
└── solution/              # 作业解答
    └── challenge_solution.py
```

### 根级目录
- `/00-course-setup/` - 环境设置和测试脚本
- `/01-introduction/` - 核心 LangChain 概念和首次 LLM 调用
- `/02-chat-models/` - 聊天模型、流式处理、错误处理、token 跟踪
- `/03-prompts-messages-outputs/` - 提示工程、结构化输出、Pydantic 模式
- `/04-function-calling-tools/` - 函数调用和工具使用
- `/05-agents/` - 自主 Agent、ReAct 模式、create_agent()、中间件
- `/06-mcp/` - 模型上下文协议 (MCP) 与外部服务集成
- `/07-documents-embeddings-semantic-search/` - 文档加载、嵌入、向量存储
- `/08-agentic-rag-systems/` - 具有智能决策能力的检索增强生成

### 核心依赖
项目使用 LangChain v1.x 包：
- `langchain-openai` - OpenAI 兼容模型集成
- `langchain-core` - 核心 LangChain 功能
- `langchain` - 主要 LangChain 工具
- `langchain-azure-ai` - Azure 特定集成
- `langchain-mcp-adapters>=0.1.14` - MCP 协议支持

### 开发容器
项目通过 `.devcontainer/` 包含 GitHub Codespaces 支持：
- Python 3.13 环境自动设置
- 虚拟环境自动激活
- 从 `.env.example` 自动创建 `.env`
- GitHub 令牌集成以实现无缝设置

## 测试和验证

**环境验证：**
`scripts/test_setup.py` 文件测试 AI 提供商连接并验证开发环境。在开始章节练习之前运行此脚本以确认设置正确工作。

**代码验证：**
大多数代码示例都是独立的，可以独立运行。每个示例通常以测试调用结束，显示预期的输出格式。

## 重要说明

- 所有代码示例都设计为用 `python filename.py` 独立运行
- 课程默认使用 GitHub Models（使用 GitHub 令牌免费使用）
- 没有特殊测试框架 - 通过运行示例手动验证输出
- 使用 `python-dotenv` 从 `.env` 文件加载环境变量
- 代码使用 `ChatOpenAI` 类同时支持 OpenAI 和 GitHub Models 端点
