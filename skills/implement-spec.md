---
name: implement-spec
description: 按任务依赖推进整份工程规格，并将各项改动集成到一条分支。
tags:
  - skill
  - engineering
  - orchestration
  - issue-tracker
repo: https://github.com/mattpocock/skills
subpath: skills/engineering/implement-spec
install_cmd: npx skills@latest add mattpocock/skills --skill implement-spec
requires:
  - Git 工作树、项目任务追踪器和支持子代理的宿主
reviewed: true
added: 2026-11-23
---

# implement-spec

> 仓库来源 · [mattpocock/skills](https://github.com/mattpocock/skills) · [上游 SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/implement-spec/SKILL.md)

按任务依赖推进整份工程规格，并将各项改动集成到一条分支。

## 适用场景与核心能力

- 识别当前可以开工的任务，并用独立 Git 工作树隔离并行实现。
- 根据任务追踪器的关闭规则衔接集成与交付。
- 相关技能包括 [to-spec](to-spec.md)、[to-tickets](to-tickets.md)、[implement](implement.md)。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `skills/engineering/implement-spec`。

```bash
npx skills@latest add mattpocock/skills --skill implement-spec
```

## 依赖与安全提示

- Git 工作树、项目任务追踪器和支持子代理的宿主。

## 个人使用记录

-
