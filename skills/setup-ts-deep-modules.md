---
name: setup-ts-deep-modules
description: "用 dependency-cruiser 约束 TypeScript 包的导入边界，将公开入口作为包间依赖面。"
tags:
  - skill
  - typescript
  - architecture
  - lint
repo: "https://github.com/mattpocock/skills"
subpath: "skills/in-progress/setup-ts-deep-modules"
requires:
  - "TypeScript 项目、dependency-cruiser 和同源技能 codebase-design"
reviewed: false
added: 2026-11-23
---

# setup-ts-deep-modules

> 仓库来源 · [mattpocock/skills](https://github.com/mattpocock/skills) · [上游 SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/in-progress/setup-ts-deep-modules/SKILL.md)

用 dependency-cruiser 约束 TypeScript 包的导入边界，将公开入口作为包间依赖面。

## 适用场景与核心能力

- 根据项目目录结构设置入口规则与私有目录约束。
- 通过验证用例确认非法跨包导入会被检测到。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `skills/in-progress/setup-ts-deep-modules`。

此技能位于上游的在研目录。可将完整技能目录复制到目标 Agent 的项目技能目录。

## 依赖与安全提示

- TypeScript 项目、dependency-cruiser 和同源技能 codebase-design。

## 个人使用记录

-
