---
name: wizard
description: "把需要人工完成的配置、授权或迁移步骤写成交互式 Bash 向导。"
tags:
  - skill
  - bash
  - automation
  - provisioning
repo: "https://github.com/mattpocock/skills"
subpath: "skills/engineering/wizard"
install_cmd: "npx skills@latest add mattpocock/skills --skill wizard"
requires:
  - "Bash"
  - "涉及 GitHub 配置时需要 gh CLI"
reviewed: false
added: 2026-11-23
---

# wizard

> 仓库来源 · [mattpocock/skills](https://github.com/mattpocock/skills) · [上游 SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/wizard/SKILL.md)

把需要人工完成的配置、授权或迁移步骤写成交互式 Bash 向导。

## 适用场景与核心能力

- 使用模板组织阶段、确认提示、URL 打开和进度显示。
- 按阶段收集输入，可写入 .env 或通过已授权的 gh CLI 写入所需配置。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `skills/engineering/wizard`。

```bash
npx skills@latest add mattpocock/skills --skill wizard
```

## 依赖与安全提示

- Bash。
- 涉及 GitHub 配置时需要 gh CLI。

## 个人使用记录

-
