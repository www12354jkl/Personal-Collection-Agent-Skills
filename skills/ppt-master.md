---
name: ppt-master
category: 图表与文档
description: 将文档、PDF、DOCX 或主题转换为原生可编辑的 PowerPoint（.pptx），支持原生形状、母版版式继承、数据驱动图表与表格、AI 生图/联网搜图、演讲备注语音旁白及套用已有 .pptx 模板。需要生成、美化、重构或套模板制作原生 PPTX 时使用。
tags:
  - skill
  - pptx
  - powerpoint
  - presentation
  - document
  - python
repo: https://github.com/hugohe3/ppt-master
subpath: skills/ppt-master
ref: d8f704bc8c1552d53a8769b55d1eecd22c782042
version: 6.10.0
install_cmd: npx skills add hugohe3/ppt-master
requires:
  - Python 3.10 - 3.14
  - pip install -r requirements.txt
  - Pandoc (可选，仅转换 .doc/.odt/.rtf/.tex 等小众格式时需要)
reviewed: true
added: 2026-11-19
---

# ppt-master

> 仓库地址：[hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)（License: MIT）

本地运行的原生 PowerPoint 生成与重构工作流：产物为原生 DrawingML `.pptx`（非扁平截图），支持母版/版式、原生图表与表格、OMML 公式、Morph 转场动画与旁白音频。

## 适用场景与核心能力

- **多路线工作流**：支持「快速生成」「确认设计规范后逐页精制」「图片转 PPTX」「美化已有 PPTX」「套用自有 `.pptx` 模板填充新内容」。
- **多源文档解析**：Python 原生处理 PDF、DOCX、HTML、EPUB、ipynb 等（仅 `.doc`/`.odt`/`.tex` 等需可选装 Pandoc）。
- **视觉素材获取**：支持直接使用宿主 Agent 原生生图工具，或配置 `image_gen.py` / `image_search.py`（Pexels/Pixabay/Openverse 等）。
- **大上下文与Token提示**：作者提示全流程 token 消耗较高，推荐使用大上下文模型（如 Gemini / Kimi K3.1 / Claude）。

## 下载与安装（给其他项目 / Agent 用）

> [!WARNING] 安装注意事项
> 1. 仅用 `npx skills add` 拉取 Skill 后，仍需按仓库根目录的 `requirements.txt` 安装 Python 依赖，否则后处理导出脚本无法运行。
> 2. `SKILL.md` 强制先执行 `scripts/attribution_guard.py` 校验，运行脚本前需确保目录结构完整。

### 方式一：完整克隆作为独立工作区（作者推荐）

```bash
git clone https://github.com/hugohe3/ppt-master.git
# 国内备用镜像：git clone https://atomgit.com/hugohe3/ppt-master.git
cd ppt-master
pip install -r requirements.txt
```

### 方式二：通过 skills CLI / Marketplace 拉取纯 Skill

```bash
# 跨 Agent CLI（需另行配好 requirements.txt 依赖）
npx skills add hugohe3/ppt-master

# 或 Git 稀疏检出 skills/ppt-master + requirements.txt
```

```powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/hugohe3/ppt-master.git _tmp_ppt
git -C _tmp_ppt sparse-checkout set skills/ppt-master requirements.txt
New-Item -ItemType Directory -Force -Path .agents/skills | Out-Null
Copy-Item -Recurse -Force _tmp_ppt/skills/ppt-master .agents/skills/ppt-master
Copy-Item -Force _tmp_ppt/requirements.txt .agents/skills/ppt-master/requirements.txt
Remove-Item -Recurse -Force _tmp_ppt
```

## 依赖与安全提示

- **Python 3.10–3.14** + `pip install -r requirements.txt`（Windows 安装 Python 时记得勾选 Add to PATH）。
- **配置 API Key**：网络生图/搜图等可选能力通过 `.env`（复制 `.env.example`）或 `~/.ppt-master/.env` 配置。
- **审核状态**：当前 `reviewed: false`。

## 个人使用记录

- 
