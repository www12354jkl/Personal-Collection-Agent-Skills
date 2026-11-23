---
name: claude-handoff
category: Agent编排
description: 把当前会话整理成交接摘要，并交给当前目录下的新 Claude Code 后台代理。
tags:
  - skill
  - claude-code
  - agent
  - handoff
repo: https://github.com/mattpocock/skills
subpath: skills/in-progress/claude-handoff
requires:
  - 支持后台代理的 Claude Code CLI
reviewed: true
added: 2026-11-23
---

# claude-handoff

> 仓库来源 · [mattpocock/skills](https://github.com/mattpocock/skills) · [上游 SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/in-progress/claude-handoff/SKILL.md)

把当前会话整理成交接摘要，并交给当前目录下的新 Claude Code 后台代理。

## 适用场景与核心能力

- 摘要记录后续任务、建议调用的技能和已有工件位置。
- 交接稿在系统临时目录保存，技能要求先去掉凭据和个人信息。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `skills/in-progress/claude-handoff`。

此技能位于上游的在研目录。可将完整技能目录复制到目标 Agent 的项目技能目录。

## 依赖与安全提示

- 支持后台代理的 Claude Code CLI。

## 个人使用记录

-
