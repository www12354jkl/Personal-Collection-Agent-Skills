---
name: anima-prompt
description: 为 Anima 编写人物和叙事图像提示词，处理模板选择、人物一致性与 ComfyUI 参数。
tags:
  - skill
  - anima
  - comfyui
  - prompt-writing
repo: https://github.com/adventyhwh/comfy-anima-skill-share
subpath: v4/anima-prompt
ref: afb3738e012f1b9233acec49f007aa9457a763ed
version: fourth-preview-slim-c1
install_cmd: git clone https://github.com/adventyhwh/comfy-anima-skill-share.git
requires:
  - Anima 模型
  - 运行生成时需要 ComfyUI
reviewed: true
added: 2026-11-23
---

# anima-prompt

> 仓库来源 · [adventyhwh/comfy-anima-skill-share](https://github.com/adventyhwh/comfy-anima-skill-share) · [上游 SKILL.md](https://github.com/adventyhwh/comfy-anima-skill-share/blob/afb3738e012f1b9233acec49f007aa9457a763ed/v4/anima-prompt/SKILL.md)（MIT）

为 Anima 编写人物和叙事图像提示词，处理模板选择、人物一致性与 ComfyUI 参数。

## 适用场景与核心能力

- 把角色、视线、道具和动作拆成能被模型表现的画面要素。
- 按单图、动态场景或批量叙事选择模板，并维护负面提示词和生成参数。
- 相关技能包括 [anima-scene-prompt](anima-scene-prompt.md)、[anima-doujin-plan](anima-doujin-plan.md)、[anima-nsfw-prompt](anima-nsfw-prompt.md)。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `v4/anima-prompt`。

```bash
git clone https://github.com/adventyhwh/comfy-anima-skill-share.git
```

按上游说明，把此技能的完整目录复制到目标 Agent 的技能目录，保留随附的引用资料（references）子目录。同名技能只安装一个版本。

## 依赖与安全提示

- Anima 模型。
- 运行生成时需要 ComfyUI。

## 个人使用记录

-
