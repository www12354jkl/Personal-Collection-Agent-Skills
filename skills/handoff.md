---
name: handoff
category: Agent编排
description: 把现有会话的背景和下一步整理成可供新代理接手的 Markdown 交接稿。
tags:
  - skill
  - agent
  - handoff
  - documentation
repo: https://github.com/mattpocock/skills
subpath: skills/productivity/handoff
install_cmd: npx skills@latest add mattpocock/skills --skill handoff
requires:
  - 系统临时目录写入权限
reviewed: true
added: 2026-11-23
---

# handoff

> 仓库来源 · [mattpocock/skills](https://github.com/mattpocock/skills) · [上游 SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md)

把现有会话的背景和下一步整理成可供新代理接手的 Markdown 交接稿。

## 适用场景与核心能力

- 记录后续任务重点、已有产物的引用和建议调用的技能。
- 交接稿写入系统临时目录，敏感信息先从内容中移除。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `skills/productivity/handoff`。

```bash
npx skills@latest add mattpocock/skills --skill handoff
```

## 依赖与安全提示

- 系统临时目录写入权限。

## 个人使用记录

-
