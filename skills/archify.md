---
name: archify
description: 将想法、计划、Mermaid 草稿或真实代码库转换为可交互的独立 HTML 图表（架构图、工作流、时序图、数据流、生命周期、ERD、类图、树图、时间线、瀑布图 10 类）或四风格单页 Explainer 讲解页。需要可视化系统结构、调用链路或生成带源码证据的可分享讲解页时使用（不适合做监控仪表盘）。
tags:
  - skill
  - diagram
  - architecture
  - explainer
  - visualization
  - html
repo: https://github.com/tt-a1i/archify
subpath: archify
ref: 44781293f38728baf04dbad33ce1a0cef8c39cca
version: 3.2.0
install_cmd: npx -y skills@latest add https://archify.si --skill archify
requires:
  - Node.js (运行 bin/archify.mjs)
reviewed: true
added: 2026-11-19
---

# archify

> 仓库地址：[tt-a1i/archify](https://github.com/tt-a1i/archify) · 官网：[archify.si](https://archify.si)（License: Apache-2.0）

把自然语言描述或代码仓库转换成布局校验过、可交互、离线可用的单个 HTML 图表或一页式 Explainer。

## 适用场景与核心能力

- **10 种交互图表**：`architecture`、`workflow`、`sequence`、`dataflow`、`lifecycle`、`erd`、`class`、`tree`、`timeline`、`waterfall`，支持深浅主题切换、路径高亮（Upstream/Downstream）、导出 PNG/SVG/WebM 及分享卡片。
- **一页式 Explainer**：结论先行，用多面板、表格、代码引用和可联动流程图把复杂问题讲清楚（可导出图片或打印 PDF）。
- **Architecture Delta**：支持对比 `base.json` 与 `head.json` 生成 PR/设计评审差异图。
- **内置交付门禁**：`node bin/archify.mjs finalize` 自动串联校验、严格检查与真实浏览器渲染检查。

## 下载与安装（给其他项目 / Agent 用）

> [!NOTE] 子目录说明
> 仓库根目录下真正的用户 Skill 位于 `archify/`（含 `SKILL.md` 与 `bin/archify.mjs`）；`.agents/skills/` 下还附带 `archify-review`、`archify-tuning` 等维护辅助 Skill。

### 方式一：通过 skills CLI 安装

```bash
# 安装到当前项目（加 --global 为全局安装，--copy 为复制而非软链接）
npx -y skills@latest add https://archify.si --skill archify --copy --yes

# 或在对话中直接让 Agent 读取官方安装指南：
# Install Archify for me by reading https://raw.githubusercontent.com/tt-a1i/archify/main/llms.txt
```

### 方式二：Git 稀疏检出（只拉取 `archify/`）

```powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/tt-a1i/archify.git _tmp_archify
git -C _tmp_archify sparse-checkout set archify
New-Item -ItemType Directory -Force -Path .agents/skills | Out-Null
Copy-Item -Recurse -Force _tmp_archify/archify .agents/skills/archify
Remove-Item -Recurse -Force _tmp_archify
```

## 依赖与安全提示

- **依赖**：需要 Node.js 环境运行 `bin/archify.mjs`，可用 `node <installed-path>/bin/archify.mjs doctor` 验证安装。
- **隐私/网络提示**：交付产物为离线 HTML，但 Skill 默认含低频版本更新检查（请求 `https://archify.si/skill-updates/archify/stable.json`）；如需完全禁用网络检查，设置环境变量 `ARCHIFY_UPDATE_CHECK_DISABLED=1`。
- **审核状态**：当前 `reviewed: false`，首次运行 `bin/archify.mjs` 前建议快速核对。

## 个人使用记录

- 
