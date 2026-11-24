---
name: lightpanda
aliases:
  - Lightpanda
  - lightpanda-browser
  - lightpanda-mcp
category: 插件与工具
description: 用 Zig 从零编写的面向 AI Agent 与自动化的超轻量无头浏览器（非 Chromium 分支），内置 V8 引擎、CDP/WebDriver BiDi 服务、原生 MCP Server（stdio / HTTP 多会话）与 Agent / PandaScript 模式，内存与速度较 Headless Chrome 显著优化。需要为编码 Agent 挂载轻量网页抓取、自动化浏览器或替代重型 Chromium 跑 Puppeteer/Playwright 时使用。
tags:
  - plugin
  - mcp
  - browser
  - headless
  - automation
  - cdp
  - cli
  - docker
repo: https://github.com/lightpanda-io/browser
subpath: .
ref: 8bc75b49b316dbc6973f98ad6b4e77cc5b8c71c4
version: 1.0.5
install_cmd: docker run -d --name lightpanda -p 127.0.0.1:9222:9222 lightpanda/browser:latest
requires:
  - Linux (glibc >= 2.35 x86_64 / >= 2.38 arm64) 或 macOS
  - Windows 需通过 WSL2 或 Docker 运行（无原生 Windows 二进制）
reviewed: true
added: 2026-11-24
---

# Lightpanda Browser（AI 无头浏览器 & 原生 MCP 服务）

> 仓库地址：[lightpanda-io/browser](https://github.com/lightpanda-io/browser) · 官网：[lightpanda.io](https://lightpanda.io)（License: AGPL-3.0-only）

从零用 Zig + V8 + Libcurl + html5ever 打造的轻量级无头浏览器（非 `SKILL.md` 技能包，配套独立 Skill 见 [lightpanda-io/agent-skill](https://github.com/lightpanda-io/agent-skill)）。不包含完整图形渲染管线，官方 100 页抓取基准峰值内存约 123MB、耗时约 5s（对比 Headless Chrome 约 2GB / 46s）。

## 核心能力与使用形态

- **CLI 直接抓取（`lightpanda fetch`）**：支持导出 HTML（`--dump html`）、Markdown（`--dump markdown`）、结构化元数据（`--dump structured_data`：JSON-LD/OpenGraph/meta）及纯文本渲染 PNG/PDF；支持 `--wait-until`、`--wait-selector`、`--wait-script`、`--obey-robots`。
- **CDP & WebDriver BiDi 服务（`lightpanda serve`）**：暴露 `ws://127.0.0.1:9222`（或 `--unix-socket`），可直接被 Puppeteer / Playwright 连接，支持 `--protocol cdp` 与 `--protocol webdriver`。
- **原生 MCP Server（`lightpanda mcp`）**：
  - 支持 **stdio** 与 **HTTP（`--port 9223`，路径 `/mcp`）**，HTTP 模式通过 `Mcp-Session-Id` 实现多 Agent 会话隔离或共享；
  - 支持 `--tools goto,tree,click` 仅暴露所需工具以节省上下文（`lightpanda mcp --list-tools` 查看完整清单）；
  - 内置 `run` 工具可直接执行 PandaScript。
- **内置 Agent 与 PandaScript（`lightpanda agent` / `lightpanda run`）**：同进程自然语言驱动网页操作，用 `/save` 导出纯 JS 的确定性脚本，后续生产回放无需再消耗 LLM Token。

## 安装与接入方式（给其他项目 / Agent 用）

> [!WARNING] Windows 运行限制
> Lightpanda **没有原生 Windows 可执行文件**。在 Windows 上请使用 **Docker**，或在 **WSL2** 内按 Linux 步骤安装（WSL 会自动转发 `localhost:9222` 给宿主机上的 Puppeteer/Playwright）。

### 方式一：Docker 一键运行 CDP 服务（跨平台最省心）

```bash
docker run -d --name lightpanda \
  -e LIGHTPANDA_DISABLE_TELEMETRY=true \
  -p 127.0.0.1:9222:9222 \
  lightpanda/browser:latest
```

### 方式二：Linux / WSL2 / macOS 下载二进制（或包管理器）

```bash
# macOS (Homebrew)
brew install lightpanda-io/browser/lightpanda

# Linux / WSL2 (x86_64 nightly；arm64 将架构改为 aarch64)
curl -L -o lightpanda https://github.com/lightpanda-io/browser/releases/download/nightly/lightpanda-x86_64-linux
chmod a+x ./lightpanda
./lightpanda version
```

> 也可通过 Nix 直接运行：`nix run github:lightpanda-io/browser -- --help`。

### 方式三：挂载为原生 MCP Server

#### 3A. stdio 模式（单客户端）

```json
{
  "mcpServers": {
    "lightpanda": {
      "command": "/path/to/lightpanda",
      "args": ["mcp", "--tools", "goto,markdown,links,tree,click,fill"],
      "env": {
        "LIGHTPANDA_DISABLE_TELEMETRY": "true"
      }
    }
  }
}
```

#### 3B. HTTP 多会话模式（多 Agent 共享进程）

```bash
LIGHTPANDA_DISABLE_TELEMETRY=true lightpanda mcp --host 127.0.0.1 --port 9223
# 客户端 POST JSON-RPC 到 http://127.0.0.1:9223/mcp
```

## 依赖与安全提示

- **默认遥测提醒**：Lightpanda 默认收集并发送使用遥测，建议统一配置环境变量 `LIGHTPANDA_DISABLE_TELEMETRY=true` 关闭。
- **网络暴露风险**：`serve`（CDP/BiDi）与 `mcp --port` 均无内置鉴权，务必仅监听 `127.0.0.1` 或使用 `--unix-socket`，不要暴露到公网。
- **Linux libc 限制**：预编译 Linux 二进制依赖 glibc（`x86_64 >= 2.35`、`arm64 >= 2.38`），无法直接运行在 Alpine（musl）或 Android/Termux。
- **许可证**：`AGPL-3.0-only`（基于其源码修改并对外提供网络服务时注意开源协议要求）。
- **审核状态**：当前 `reviewed: false`。

## 个人使用记录

- 
