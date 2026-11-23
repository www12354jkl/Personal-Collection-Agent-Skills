---
name: library-skills
description: 从已安装的依赖包发现代理技能，并管理项目中的技能链接。
tags:
  - skill
  - agent
  - package-management
  - dependencies
repo: https://github.com/tiangolo/library-skills
subpath: src/library_skills/tool_skill
version: 0.0.19
install_cmd: uvx library-skills --tool-skill
requires:
  - uvx 或 npx
  - 项目依赖已安装
reviewed: true
added: 2026-11-23
---

# library-skills

> 仓库来源 · [tiangolo/library-skills](https://github.com/tiangolo/library-skills) · [上游 SKILL.md](https://github.com/tiangolo/library-skills/blob/main/src/library_skills/tool_skill/SKILL.md) · [Library Skills 文档](https://library-skills.io)

从已安装的依赖包发现代理技能，并管理项目中的技能链接。

## 适用场景与核心能力

- 可检查失效或孤立的受管链接，并重新同步项目技能。
- 支持按名称安装和输出 JSON 的发现或列表模式。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `src/library_skills/tool_skill`。

```bash
uvx library-skills --tool-skill
npx library-skills --tool-skill
```

## 依赖与安全提示

- uvx 或 npx。
- 项目依赖已安装。

## 个人使用记录

-
