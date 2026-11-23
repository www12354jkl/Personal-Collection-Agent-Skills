---
name: anima-workflow
description: 为 Anima 批量生成、对比测试、读图审计和漫画交付提供运行约定。
tags:
  - skill
  - anima
  - comfyui
  - workflow
repo: https://github.com/adventyhwh/comfy-anima-skill-share
subpath: v4/anima-workflow
ref: afb3738e012f1b9233acec49f007aa9457a763ed
version: v1.4
install_cmd: git clone https://github.com/adventyhwh/comfy-anima-skill-share.git
requires:
  - ComfyUI
  - 同源技能 anima-prompt
reviewed: true
added: 2026-11-23
---

# anima-workflow

> 仓库来源 · [adventyhwh/comfy-anima-skill-share](https://github.com/adventyhwh/comfy-anima-skill-share) · [上游 SKILL.md](https://github.com/adventyhwh/comfy-anima-skill-share/blob/afb3738e012f1b9233acec49f007aa9457a763ed/v4/anima-workflow/SKILL.md)（MIT）

为 Anima 批量生成、对比测试、读图审计和漫画交付提供运行约定。

## 适用场景与核心能力

- 按轮次归档生成物，用相同主题、人物和种子比较方案。
- 记录重试和人工抽查结果，按成片、原图和废案管理交付。
- 相关技能包括 [anima-prompt](anima-prompt.md)、[anima-doujin-plan](anima-doujin-plan.md)、[anima-change](anima-change.md)。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `v4/anima-workflow`。

```bash
git clone https://github.com/adventyhwh/comfy-anima-skill-share.git
```

按上游说明，把此技能的完整目录复制到目标 Agent 的技能目录，保留随附的引用资料（references）子目录。同名技能只安装一个版本。

## 依赖与安全提示

- ComfyUI。
- 同源技能 anima-prompt。

## 个人使用记录

-
