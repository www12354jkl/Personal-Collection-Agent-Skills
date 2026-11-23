---
name: git-guardrails-claude-code
category: 工程与架构
description: 为 Claude Code 配置 Git 命令拦截钩子，降低误推送或误清理工作树的风险。
tags:
  - skill
  - git
  - claude-code
  - hooks
repo: https://github.com/mattpocock/skills
subpath: skills/misc/git-guardrails-claude-code
requires:
  - Claude Code、Bash 与 Git
reviewed: true
added: 2026-11-23
---

# git-guardrails-claude-code

> 仓库来源 · [mattpocock/skills](https://github.com/mattpocock/skills) · [上游 SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/misc/git-guardrails-claude-code/SKILL.md)

为 Claude Code 配置 Git 命令拦截钩子，降低误推送或误清理工作树的风险。

## 适用场景与核心能力

- 用 PreToolUse 钩子拦截推送、硬重置、强制删除分支等命令。
- 支持项目级和用户级设置，安装流程会先确定作用范围。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `skills/misc/git-guardrails-claude-code`。

可从仓库把完整目录复制到目标 Agent 的项目技能目录。

## 依赖与安全提示

- Claude Code、Bash 与 Git。

## 个人使用记录

-
