---
name: markitdown
aliases:
  - MarkItDown
  - markitdown-mcp
  - markitdown-ocr
category: 插件与工具
description: 微软开源的多格式文件转结构化 Markdown 工具库与官方 MCP 服务（markitdown-mcp），支持 PDF、Word、PPT、Excel、HTML、EPub、ZIP、图片/音频与 YouTube 字幕转换，并支持 LLM Vision 内嵌图片 OCR 与 Azure 云端版面解析。需要让编码 Agent 读取二进制办公文档或搭建 RAG 文档预处理管线时使用。
tags:
  - plugin
  - mcp
  - tool
  - markdown
  - document
  - cli
  - python
repo: https://github.com/microsoft/markitdown
subpath: .
ref: ed178952a6672abdfd35b5f9e76a80b6cefc086e
version: 0.1.9
install_cmd: pip install "markitdown[all]"
requires:
  - Python 3.10 - 3.14 (推荐 uv 或虚拟环境隔离)
  - 可选：uv (支持 uvx 免建虚拟环境直接拉起 CLI / MCP) 或 Docker
reviewed: true
added: 2026-11-24
---

# MarkItDown（文档转 Markdown 工具 & MCP 服务）

> 仓库地址：[microsoft/markitdown](https://github.com/microsoft/markitdown)（微软 AutoGen 团队出品 · License: MIT · `markitdown-mcp` 版本：`0.0.1a8`）

面向 LLM 上下文投喂、RAG 检索与 Agent 文本分析管线的轻量级“万物转 Markdown”工具集（非 `SKILL.md` 技能包），重点保留标题层级、列表、表格、链接等语义结构并节省 Token。

## 核心能力与子包结构

- **支持的输入格式**：
  - **办公与电子书**：PDF、Word (`.docx`)、PPT (`.pptx`)、Excel (`.xlsx` / `.xls`)、Outlook 邮件、EPub
  - **网页、数据与压缩包**：HTML、CSV、JSON、XML、YouTube 链接（抓字幕）、`.zip`（递归遍历内部文件）
  - **多模态（可选服务）**：图片（EXIF 元数据 + 视觉大模型图注描述）、音频（EXIF + 语音转文字）
- **仓库三大实用包（`packages/`）**：
  1. **`markitdown`**：核心 Python 库与命令行工具（支持全量 `[all]` 或按需安装如 `[pdf,docx,pptx]`）。
  2. **`markitdown-mcp`**：官方 MCP Server（支持 `STDIO`、`Streamable HTTP`、`SSE`），暴露单一工具 `convert_to_markdown(uri)`（支持 `file:`、`http:`、`https:`、`data:` URI），安装时会自动拉取 `markitdown[all]`。
  3. **`markitdown-ocr`**：官方视觉 OCR 插件，直接复用 OpenAI 兼容 `llm_client` + `llm_model` 提取 PDF/DOCX/PPTX/XLSX 内嵌图片文字，无需安装本地重型 OCR 依赖。

## 部署与接入方式（给 Agent 客户端 / 日常命令行用）

### 方式一：挂载为 MCP Server（让 Antigravity / Claude 等直接读文档）

#### 1A. 用 `uvx` 零污染一键挂载（最省心，推荐）

只要本机装了 `uv`，无需手动建虚拟环境，直接在全局 MCP 配置（如 Antigravity 的 `~/.gemini/config/mcp_config.json`）里添加：

```json
{
  "mcpServers": {
    "markitdown": {
      "command": "uvx",
      "args": ["markitdown-mcp"]
    }
  }
}
```

> 若偏向持久安装后再调用，也可先跑一次 `uv tool install markitdown-mcp`（或虚拟环境 `pip install markitdown-mcp`），再将 `"command"` 填为 `"markitdown-mcp"`、`"args": []`。

#### 1B. Streamable HTTP 模式 / Docker 隔离运行

- **本地 HTTP 服务**（默认仅绑定 `127.0.0.1`）：
  ```bash
  markitdown-mcp --http --host 127.0.0.1 --port 3001
  # 客户端配置 url: "http://127.0.0.1:3001/mcp"
  ```
- **Docker 沙箱挂载指定目录**（限制本地文件访问范围更安全）：
  ```json
  {
    "mcpServers": {
      "markitdown": {
        "command": "docker",
        "args": ["run", "--rm", "-i", "-v", "D:/docs:/workdir", "markitdown-mcp:latest"]
      }
    }
  }
  ```

### 方式二：命令行 CLI 直接转换文件

```powershell
# 推荐用 uv tool 全局隔离安装 CLI
uv tool install "markitdown[all]"
# 或在虚拟环境中按需安装：pip install "markitdown[pdf,docx,pptx,xlsx]"

# 转换文件到 Markdown
markitdown report.docx -o report.md
```

### 方式三：Python 代码集成（含内嵌图片视觉 OCR）

```python
from markitdown import MarkItDown
from openai import OpenAI

# 基础离线转换
md = MarkItDown()
print(md.convert("sheet.xlsx").markdown)

# 启用 markitdown-ocr 插件（需先 pip install markitdown-ocr openai）
md_ocr = MarkItDown(
    enable_plugins=True,
    llm_client=OpenAI(),
    llm_model="gpt-4o",
)
print(md_ocr.convert("slides_with_charts.pptx").markdown)
```

## 依赖与安全提示

- **Python 版本要求**：Python `3.10` – `3.14`。
- **进程权限与 SSRF / 任意文件读取风险**：`markitdown` 与 `markitdown-mcp` 无内置鉴权，直接以当前用户权限读取本地文件或请求网络资源：
  - **切勿**将 `markitdown-mcp --http` 绑定到 `0.0.0.0` 暴露在公网或不可信局域网；
  - 在服务端业务代码调用时，处理外部不可信输入应优先使用窄接口 `convert_stream()` 或校验后的 `convert_local()`，避免直接把未过滤 URI 传给宽泛的 `convert()`。
- **云端计费提醒**：可选的 Azure Document Intelligence（`-d`）与 Azure Content Understanding（`--use-cu`）属于按次计费云 API，日常本地转换无需开启。

## 个人使用记录

- 2026-11-24：已通过 `uv tool`（清华镜像源）全局隔离安装 `markitdown-mcp`（`C:\Users\过二硫酸铵\.local\bin\markitdown-mcp.exe`）与 `markitdown` CLI（`C:\Users\过二硫酸铵\.local\bin\markitdown.exe`），并已挂载至 Antigravity 全局 `~/.gemini/config/mcp_config.json`。
