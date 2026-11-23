---
name: impeccable
category: 前端与设计
description: 为编码 Agent 提供前端设计词汇与审校体系，支持通过 24 个设计指令（如 polish、bolder、quieter、critique、audit、harden、live）优化页面、排查 AI 模板味（AI slop）并生成 PRODUCT.md / DESIGN.md 设计规范。用于设计、重塑或审查前端界面与 UI 组件时使用（非纯后端任务）。
tags:
  - skill
  - frontend
  - design
  - ui-ux
  - accessibility
  - lint
repo: https://github.com/pbakaus/impeccable
subpath: .agents/skills/impeccable
ref: b49177d32788f2dc585c42831d845dacf1ebed2c
version: 4.10.0
install_cmd: npx impeccable install
requires:
  - Node.js >= 18.19.0 (仅 npx 安装/CLI 时需要；Skill 运行使用内置或首次下载的二进制引擎)
reviewed: true
added: 2026-11-19
---

# impeccable

> 仓库地址：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 文档：[impeccable.style/docs](https://impeccable.style/docs)（License: Apache-2.0）

解决 AI 前端常见的“紫色渐变、千篇一律卡片套卡片、Inter 字体滥用”等模板味问题，提供设计指令体系、交互式浏览器实时调优与 62 条确定性反模式检测规则。

## 适用场景与核心能力

- **24 个设计指令**：
  - **风格微调（Steer）**：`bolder`、`quieter`、`distill`、`colorize`、`typeset`、`layout`、`animate`、`delight`、`overdrive`
  - **审查诊断（Review）**：`critique`（可用性启发式评分）、`audit`（无障碍/性能/响应式 P0–P3 报告）
  - **收尾加固（Finish）**：`polish`、`harden`、`clarify`、`adapt`、`optimize`、`onboard`
  - **实时与规划**：`live`（开发服务器页面内点选元素热替换变体）、`generate`、`shape`、`init`、`document`、`extract`
- **62 条确定性 Slop 检测**：无需 LLM / API Key，可在 Agent Hook、终端/CI（`npx impeccable detect` 支持 `--sarif` / `--github`）或 Chrome 扩展中运行。
- **跨工具兼容**：支持 Claude Code、Cursor、Codex CLI、Antigravity、Gemini CLI、GitHub Copilot、OpenCode 等。

## 下载与安装（给其他项目 / Agent 用）

### 方式一：官方交互式安装器（推荐，可选装设计 Hook）

```bash
# 在目标项目根目录执行（支持 --providers=claude,codex,cursor --scope=project|global）
npx impeccable install

# 更新已安装的 Skill
npx impeccable update
```

### 方式二：Git 稀疏检出（无需 Node，手动拷贝 Skill 目录）

> 仓库根目录为各 Agent 工具提交了对应构建目录（如 `.agents/`、`.claude/`、`.cursor/`、`.gemini/`）。按规范目录拉取 `.agents/skills/impeccable`：

```powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/pbakaus/impeccable.git _tmp_impeccable
git -C _tmp_impeccable sparse-checkout set .agents/skills/impeccable
New-Item -ItemType Directory -Force -Path .agents/skills | Out-Null
Copy-Item -Recurse -Force _tmp_impeccable/.agents/skills/impeccable .agents/skills/impeccable
Remove-Item -Recurse -Force _tmp_impeccable
```

## 依赖与安全提示

- **引擎二进制**：`npx` 仅用于安装器和 `detect` CLI；Skill 本身通过随附或首次下载到 `~/.impeccable/bin/` 的独立引擎二进制运行。
- **Live 模式注意**：仅在本地开发环境使用 `/impeccable live`，勿注入生产站点；若启用自动应用文案修改，注意 `package.json` 中的 `impeccable:manual-edit-validate` 钩子权限。
- **审核状态**：当前 `reviewed: false`。

## 个人使用记录

- 
