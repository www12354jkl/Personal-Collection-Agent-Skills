---
name: vibestart
description: 通过 vibestart-cli 自由组合经过 CI 验证的全栈 TypeScript 技术栈（React/Next/TanStack Start/Electron/Expo + Hono/Effect + Drizzle/Prisma + Better Auth + Vite+），并支持增量添加能力（add）、状态诊断（doctor）与保留业务修改的三方合并升级（upgrade）。用于创建新 TypeScript 项目或维护含 vibestart.jsonc 的工程时使用。
tags:
  - skill
  - typescript
  - fullstack
  - scaffold
  - cli
  - vite-plus
repo: https://github.com/VinkyDev/vibestart
subpath: skills/vibestart
ref: c3beb5a767e4ddb93c549094b1df6464308b3b0e
version: 0.2.4
install_cmd: npx skills add VinkyDev/vibestart --skill vibestart
requires:
  - Node.js >= 22.12.0
reviewed: false
added: 2026-11-19
---

# vibestart

> 仓库地址：[VinkyDev/vibestart](https://github.com/VinkyDev/vibestart) · 工作台：[vibestart.net/studio](https://vibestart.net/studio)（License: MIT）

专为 AI 编码 Agent 设计的全栈 TypeScript 脚手架与持续演进工具：所有技术栈组合均在 CI 实际跑通类型检查、Lint、测试与构建，并通过 `AGENTS.md` 与 `vp run ready` 约束后续代码质量。

## 适用场景与核心能力

- **两种模式**：`Standard`（React SPA / TanStack Start / Next.js / Electron / Expo + Hono / oRPC / OpenAPI + Drizzle / Prisma / Mongoose + Better Auth + Tailwind 4）与 `Effect`（`--mode effect`，更严格的服务链路模型）。
- **核心工作流**：
  - 创建项目：`npx --yes vibestart-cli --list --json` 查看可选栈后生成工程；
  - 增量加能力：`npx --yes vibestart-cli add --list --json`（如 Knip、Ultracite、Docker 等）；
  - 体检与升级：`doctor --offline --json` 诊断，`upgrade --dry-run --json` 预览并通过三方合并升级底层模板、保留你的业务代码。
- **统一检查链**：生成的项目内置 [Vite+](https://viteplus.dev)（`vp run dev` / `vp run ready`），集成 Oxlint、Oxfmt、Knip、Vitest、Playwright。

## 下载与安装（给其他项目 / Agent 用）

> [!NOTE] 子目录说明
> Skill 位于仓库的 `skills/vibestart/`；安装 Skill 本身不会自动安装 CLI 或项目依赖，使用时通过 `npx --yes vibestart-cli` 调起。

### 方式一：通过 skills CLI 安装

```bash
npx skills add VinkyDev/vibestart --skill vibestart
```

### 方式二：Git 稀疏检出（只拉取 `skills/vibestart`）

```powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/VinkyDev/vibestart.git _tmp_vibestart
git -C _tmp_vibestart sparse-checkout set skills/vibestart
New-Item -ItemType Directory -Force -Path .agents/skills | Out-Null
Copy-Item -Recurse -Force _tmp_vibestart/skills/vibestart .agents/skills/vibestart
Remove-Item -Recurse -Force _tmp_vibestart
```

## 依赖与使用提示

- **Node.js >= 22.12.0**（CLI `apps/cli/package.json` 要求）。
- 在维护已有项目执行写入操作（`add` / `upgrade`）前，要求目标工程 Git 工作区干净，且需保留 `vibestart.jsonc` 中的 `name` 与 `version`。
- **审核状态**：当前 `reviewed: false`（本机已有同源安装版可对照参考）。

## 个人使用记录

- 
