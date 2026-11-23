---
name: pdf
category: 图表与文档
description: 用 Poppler 和 Python 工具读取、制作、渲染并检查 PDF，适合对版面有要求的交付。
tags:
  - skill
  - document
  - pdf
  - rendering
repo: https://github.com/openai/skills
subpath: skills/.curated/pdf
install_cmd: $skill-installer pdf
requires:
  - Poppler
  - 按任务使用 reportlab、pdfplumber 或 pypdf
reviewed: true
added: 2026-11-23
---

# pdf

> 仓库来源 · [openai/skills](https://github.com/openai/skills) · [上游 SKILL.md](https://github.com/openai/skills/blob/main/skills/.curated/pdf/SKILL.md)

用 Poppler 和 Python 工具读取、制作、渲染并检查 PDF，适合对版面有要求的交付。

## 适用场景与核心能力

- 将页面渲染成图片，检查排版、裁切和可读性。
- 按工作选择 reportlab 生成 PDF，或用 pdfplumber 与 pypdf 提取及处理内容。

## 下载与安装（给其他项目 / Agent 用）

技能目录为 `skills/.curated/pdf`。

```text
$skill-installer pdf
```

## 依赖与安全提示

- Poppler。
- 按任务使用 reportlab、pdfplumber 或 pypdf。
- 这是从 OpenAI 技能仓库收录的独立 PDF 技能。

## 个人使用记录

-
