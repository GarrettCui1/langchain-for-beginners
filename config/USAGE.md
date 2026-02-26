# 代理配置使用说明

本项目已统一代理配置管理，避免在每个文件中重复配置代理。

## 使用方法

### 1. 配置环境变量（可选）

编辑 `.env` 文件，配置代理设置（如果需要）：

```bash
# 如果需要使用代理服务器
HTTP_PROXY=http://your-proxy:port
HTTPS_PROXY=http://your-proxy:port
NO_PROXY=localhost,127.0.0.1  # 本地服务不走代理

# 如果要禁用代理，设置为空值
HTTP_PROXY=
HTTPS_PROXY=
```

默认情况下，系统会自动配置 `NO_PROXY=localhost,127.0.0.1`，确保 Ollama 等本地服务直连。

### 2. 在代码中使用

在任何需要配置代理的 Python 文件中，添加以下导入：

```python
# 导入配置模块（必须在加载环境变量之前）
from config.proxy_config import configure_proxy

# 应用代理配置
configure_proxy()

# 然后加载环境变量
from dotenv import load_dotenv
load_dotenv()

# 你的代码...
```

或者更简洁的方式：

```python
# 从 config 包导入，自动执行配置
import config

# 然后加载环境变量
from dotenv import load_dotenv
load_dotenv()

# 你的代码...
```

### 3. 调试代理配置

如果需要查看代理配置详情，在 `.env` 文件中添加：

```bash
DEBUG=1
```

运行程序时会输出当前的代理配置信息。

## 配置模块位置

- `config/proxy_config.py` - 核心代理配置逻辑
- `config/__init__.py` - 包初始化文件
- `.env.example` - 环境变量配置模板

## 示例代码

见 `scripts/test_setup.py` 中的实际使用示例。
