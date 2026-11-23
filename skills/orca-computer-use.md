---
name: orca-computer-use
category: Agent编排
description: 通过 Orca 驱动原生应用或外部浏览器窗口，读取控件、执行交互并截图。
tags:
  - skill
  - orca
  - desktop
  - gui
repo: https://github.com/stablyai/orca
subpath: skills/orca-computer-use
install_cmd: npx skills add stablyai/orca --skill orca-computer-use
requires:
  - Orca CLI
  - 支持桌面控制的运行环境
reviewed: true
added: 2026-11-23
---

# orca-computer-use

> 仓库来源 · [stablyai/orca](https://github.com/stablyai/orca) · [上游 SKILL.md](https://github.com/stablyai/orca/blob/main/skills/orca-computer-use/SKILL.md)

通过 Orca 驱动原生应用或外部浏览器窗口，读取控件、执行交互并截图。

## 适用场景与核心能力

- 用可访问性树定位控件，并进行点击、输入或菜单操作。
- 根据应用窗口和平台能力选择后台交互方式。
- 相关技能包括 [orca-cli](orca-cli.md)。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `skills/orca-computer-use`。

```bash
npx skills add stablyai/orca --skill orca-computer-use
```

## 依赖与安全提示

- Orca CLI。
- 支持桌面控制的运行环境。
- 本地入口从已安装的 Orca CLI 读取匹配版本的操作指南。

## 个人使用记录

-
