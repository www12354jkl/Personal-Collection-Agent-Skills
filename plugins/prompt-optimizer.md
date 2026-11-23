---
name: prompt-optimizer
aliases:
  - 提示词优化器
category: 插件与工具
description: 开源 AI 提示词优化工具与 MCP 服务，支持系统/用户提示词迭代优化、变量模板复用、多模型同题竞技场对比、文生图/图生图提示词工作区，提供 Web 应用、桌面客户端、Chrome 浏览器插件、Docker 部署及 MCP Server 接入。需要系统性优化与评测 Prompt 或为客户端挂载提示词优化 MCP 工具时使用。
tags:
  - plugin
  - mcp
  - chrome-extension
  - prompt
  - tool
  - docker
repo: https://github.com/linshenkx/prompt-optimizer
subpath: .
ref: 62b49a1f646af499b6c472c16984b19ab7a358cb
version: 2.16.0
install_cmd: docker run -d -p 8081:80 --restart unless-stopped --name prompt-optimizer linshen/prompt-optimizer
requires:
  - Docker (一键运行 Web + HTTP MCP 服务)
  - 或 Node.js 24 + pnpm 10.6.1 (本地构建运行 / stdio MCP)
reviewed: true
added: 2026-11-19
---

# Prompt Optimizer（提示词优化器）

> 仓库地址：[linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) · 在线体验：[prompt.always200.com](https://prompt.always200.com)（License: AGPL-3.0）

纯前端/本地优先的提示词优化与评测工具（非 `SKILL.md` 技能包），除 Web / 桌面客户端与 Chrome 扩展外，还内置 **MCP Server**（`packages/mcp-server`），可把提示词优化能力直接挂载到 AI 客户端。

## 核心能力与交付形态

- **核心功能**：系统/用户提示词优化与定向迭代、变量模板与多轮会话测试、多模型同题对比竞技场、单/多结果评估链路、文生图/图生图工作区与资产收藏。
- **四种使用形态**：
  1. **Web / Docker 部署**：同时启动 Web 页面与 Streamable HTTP MCP 服务（`/mcp` 路径）。
  2. **MCP Server（HTTP 或 stdio）**：暴露 `optimize-user-prompt`、`optimize-system-prompt`、`iterate-prompt` 三个 MCP 工具。
  3. **桌面客户端**：GitHub Releases 下载 `.exe` / `.dmg` / `.AppImage`（支持连 Ollama 等本地服务）。
  4. **Chrome 浏览器插件**：Chrome Web Store 安装即用。

## 部署与接入方式（给其他项目 / 客户端用）

### 方式一：Docker 一键启动 Web + HTTP MCP（推荐）

```bash
docker run -d -p 8081:80 \
  -e VITE_OPENAI_API_KEY=your_key \
  -e MCP_DEFAULT_MODEL_PROVIDER=openai \
  --restart unless-stopped \
  --name prompt-optimizer \
  linshen/prompt-optimizer
# Web: http://localhost:8081
# MCP (Streamable HTTP): http://localhost:8081/mcp
```

> 国内 Docker Hub 较慢可换镜像：`registry.cn-guangzhou.aliyuncs.com/prompt-optimizer/prompt-optimizer`

### 方式二：本地源码构建 stdio MCP Server

```bash
git clone https://github.com/linshenkx/prompt-optimizer.git
cd prompt-optimizer
pnpm install
pnpm build:core
pnpm mcp:build
```

然后在客户端 `mcpServers` 中配置（stdio）：

```json
{
  "mcpServers": {
    "prompt-optimizer": {
      "command": "node",
      "args": ["/absolute/path/to/prompt-optimizer/packages/mcp-server/bin/prompt-optimizer-mcp.cjs", "--transport=stdio"],
      "env": {
        "VITE_OPENAI_API_KEY": "your_key",
        "MCP_DEFAULT_MODEL_PROVIDER": "openai"
      }
    }
  }
}
```

## 依赖与安全提示

- **本地构建依赖**：Node.js 24（`^24.22.1`）+ `pnpm@10.6.1`。
- **公网部署提醒**：公开托管 Web 前端时**不要**在环境变量里预置 `VITE_*` API Key，因为 `VITE_*` 变量会打包进前端资源暴露给浏览器；如需访问控制可配 `ACCESS_PASSWORD`（MCP `/mcp` 路由在 v1.4.0+ 已绕过 Basic Auth）。
- **许可证**：`AGPL-3.0-only`（二次开发并对外提供网络服务时注意开源传染性条款）。
- **审核状态**：当前 `reviewed: false`。

## 个人使用记录

- 
