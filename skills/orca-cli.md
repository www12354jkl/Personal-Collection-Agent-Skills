---
name: orca-cli
description: "通过 Orca CLI 操作工作树、终端、仓库和内置浏览器。"
tags:
  - skill
  - orca
  - git
  - worktree
repo: "https://github.com/stablyai/orca"
subpath: "skills/orca-cli"
install_cmd: "npx skills add stablyai/orca --skill orca-cli"
requires:
  - "Orca 桌面应用与匹配版本的 Orca CLI"
reviewed: false
added: 2026-11-23
---

# orca-cli

> 仓库来源 · [stablyai/orca](https://github.com/stablyai/orca) · [上游 SKILL.md](https://github.com/stablyai/orca/blob/main/skills/orca-cli/SKILL.md)

通过 Orca CLI 操作工作树、终端、仓库和内置浏览器。

## 适用场景与核心能力

- 用于创建或检查 Orca 工作树、读取终端状态和管理交接。
- 使用已安装版本对应的 CLI 指南来确定子命令和参数。
- 相关技能包括 [orca-computer-use](orca-computer-use.md)、[orchestration](orchestration.md)。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `skills/orca-cli`。

```bash
npx skills add stablyai/orca --skill orca-cli
```

## 依赖与安全提示

- Orca 桌面应用与匹配版本的 Orca CLI。
- 本地入口从已安装的 Orca CLI 读取匹配版本的操作指南。

## 个人使用记录

-
