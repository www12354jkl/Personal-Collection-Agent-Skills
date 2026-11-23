---
name: setup-matt-pocock-skills
category: Agent编排
description: 为项目配置 Matt Pocock 工程技能依赖的任务追踪、分流标签和领域文档位置。
tags:
  - skill
  - agent
  - configuration
  - issue-tracker
repo: https://github.com/mattpocock/skills
subpath: skills/engineering/setup-matt-pocock-skills
install_cmd: npx skills@latest add mattpocock/skills --skill setup-matt-pocock-skills
requires:
  - 目标项目
  - 按需使用 GitHub、GitLab 或本地 Markdown
reviewed: true
added: 2026-11-23
---

# setup-matt-pocock-skills

> 仓库来源 · [mattpocock/skills](https://github.com/mattpocock/skills) · [上游 SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md)

为项目配置 Matt Pocock 工程技能依赖的任务追踪、分流标签和领域文档位置。

## 适用场景与核心能力

- 先读取现有项目配置，确认用 GitHub、GitLab 还是本地 Markdown 维护任务。
- 按仓库惯例记录标签与词汇表、ADR 路径，供后续技能读取。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `skills/engineering/setup-matt-pocock-skills`。

```bash
npx skills@latest add mattpocock/skills --skill setup-matt-pocock-skills
```

## 依赖与安全提示

- 目标项目。
- 按需使用 GitHub、GitLab 或本地 Markdown。

## 个人使用记录

-
