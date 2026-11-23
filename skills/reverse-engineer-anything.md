---
name: reverse-engineer-anything
category: 工程与架构
description: 用 REA 检查已发布的软件、包或二进制文件，为行为说明和版本对比提供证据。
tags:
  - skill
  - reverse-engineering
  - diagnostics
  - analysis
repo: https://github.com/morluto/rea
subpath: .agents/skills/reverse-engineer-anything
version: "37"
install_cmd: npx skills add morluto/rea --skill reverse-engineer-anything
requires:
  - REA CLI 或 MCP
  - 按目标格式配置分析工具
reviewed: true
added: 2026-11-23
---

# reverse-engineer-anything

> 仓库来源 · [morluto/rea](https://github.com/morluto/rea) · [上游 SKILL.md](https://github.com/morluto/rea/blob/main/.agents/skills/reverse-engineer-anything/SKILL.md)

用 REA 检查已发布的软件、包或二进制文件，为行为说明和版本对比提供证据。

## 适用场景与核心能力

- 按目标格式选择分析能力，用源码外的随包资源和静态信息相互验证。
- 报告证据范围、工具限制和未能确认的结论，适合软件维护与兼容性排查。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `.agents/skills/reverse-engineer-anything`。

```bash
npx skills add morluto/rea --skill reverse-engineer-anything
```

## 依赖与安全提示

- REA CLI 或 MCP。
- 按目标格式配置分析工具。
- 本地说明标注版本 37。REA 的运行依赖随所选分析能力而异，配置见上游文档。

## 个人使用记录

-
