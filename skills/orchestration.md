---
name: orchestration
category: Agent编排
description: 用 Orca 工作代理分派任务并收结果，适合需要独立工作区或不同代理运行时的协作。
tags:
  - skill
  - orca
  - agent
  - orchestration
repo: https://github.com/stablyai/orca
subpath: skills/orchestration
install_cmd: npx skills add stablyai/orca --skill orchestration
requires:
  - Orca CLI 与已配置的工作代理
reviewed: true
added: 2026-11-23
---

# orchestration

> 仓库来源 · [stablyai/orca](https://github.com/stablyai/orca) · [上游 SKILL.md](https://github.com/stablyai/orca/blob/main/skills/orchestration/SKILL.md)

用 Orca 工作代理分派任务并收结果，适合需要独立工作区或不同代理运行时的协作。

## 适用场景与核心能力

- 以工作区、任务和分派记录关联工作代理。
- 跟踪进度、接收提问并把结果带回主会话。
- 相关技能包括 [orca-cli](orca-cli.md)。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `skills/orchestration`。

```bash
npx skills add stablyai/orca --skill orchestration
```

## 依赖与安全提示

- Orca CLI 与已配置的工作代理。
- 本地入口从已安装的 Orca CLI 读取匹配版本的操作指南。

## 个人使用记录

-
