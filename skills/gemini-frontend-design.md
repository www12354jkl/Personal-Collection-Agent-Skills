---
name: gemini-frontend-design
aliases:
  - Gemini DemoLab
  - demolab
category: 前端与设计
description: Google Gemini 团队出品的前端界面设计与构建指南（针对 Gemini 4 模型特性调优），覆盖视觉方向与配色、首屏版式匹配（拒绝套模板 50/50 分栏）、三阶字号排版纪律、定制视觉与动效、反 AI 模板味清单及多视口交付前视觉自检。新建或改版网站、落地页、Web 应用与交互演示时使用。
tags:
  - skill
  - frontend
  - design
  - ui-ux
  - gemini
  - web
  - typography
repo: https://github.com/google-gemini/demolab
subpath: skills/gemini-frontend-design
ref: cd0c1f8540c0186ec9592af972a0700fa20909d4
version: 1.0.0
install_cmd: npx skills add https://github.com/google-gemini/demolab --skill gemini-frontend-design
requires:
  - 无额外运行时依赖（纯 SKILL.md 规范；视觉自检与配图分别复用宿主浏览器截图与生图工具）
reviewed: true
added: 2026-11-25
---

# gemini-frontend-design

> 仓库来源：[google-gemini/demolab](https://github.com/google-gemini/demolab) · [上游 SKILL.md](https://github.com/google-gemini/demolab/blob/cd0c1f8540c0186ec9592af972a0700fa20909d4/skills/gemini-frontend-design/SKILL.md)（License: Apache-2.0）

由 Google Gemini 团队维护的 DemoLab 前端设计 Skill，专门针对 Gemini 4 系列模型的前端视觉与代码倾向做过调优（官方评测相比无 Skill 偏好率 67%、相比常见第三方前端设计 Skill 偏好率 75%）。

## 适用场景与核心能力

- **视觉方向与配色纪律**：按主题材质与受众定制调色，避免模型默认陷入“米白配陶土”或“深灰配霓虹紫”反射；规范单行紧凑导航、WCAG AA 对比度与语义 Token。
- **排版克制与首屏张力**：全站最多 2 套字体、正文严格 3 阶字号（Hero 主标题与导航 Wordmark 不受限），禁止首屏出现 `< 13px` 细字；按网站类型决定是否使用 Hero（新闻/文档/仪表盘/工具页直接进内容，品牌/展示页打破千篇一律的 50/50 分栏）。
- **定制视觉与克制动效**：优先用生图工具或定制 SVG/Canvas 视觉替代占位图，动效显式声明属性（禁用 `transition: all`）并遵循 `prefers-reduced-motion`。
- **反 AI 模板味清单与验收**：禁止装饰性 Eyebrow/Kicker 标签、无交互徽章/胶囊、卡片套卡片、伪造 `"01/02"` 编号或 `"LIVE"` 圆点、空洞营销套话；交付前要求在桌面端（首屏 + 滚动区域）与 `390x844` 移动端实拍截图自检。

## 下载与安装（给其他项目 / Agent 用）

### 方式一：Vercel skills CLI（推荐）

```bash
# 安装到当前项目
npx skills add https://github.com/google-gemini/demolab --skill gemini-frontend-design

# 全局安装（用户级，自动同步至 Antigravity 与通用 .agents/skills）
npx skills add https://github.com/google-gemini/demolab --skill gemini-frontend-design -g -y
```

### 方式二：其他 CLI / 插件生态

```bash
# Antigravity CLI（整套 DemoLab 插件）
agy plugin install https://github.com/google-gemini/demolab

# Context7 CLI
npx ctx7 skills install /google-gemini/demolab gemini-frontend-design

# Claude Code
# /plugin marketplace add google-gemini/demolab
# /plugin install demolab@demolab
```

### 方式三：Git 稀疏检出（只拉取 `skills/gemini-frontend-design`）

```powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/google-gemini/demolab.git _tmp_demolab
git -C _tmp_demolab sparse-checkout set skills/gemini-frontend-design
New-Item -ItemType Directory -Force -Path .agents/skills | Out-Null
Copy-Item -Recurse -Force _tmp_demolab/skills/gemini-frontend-design .agents/skills/gemini-frontend-design
Remove-Item -Recurse -Force _tmp_demolab
```

## 依赖与安全提示

- 整个 Skill 仅包含单文件 `SKILL.md`（约 16 KB），**无任何可执行脚本或外部网络调用**，已全文核查安全无风险（`reviewed: true`）。
- 若需与 [impeccable](impeccable.md) 或 [ui-ux-pro-max](ui-ux-pro-max.md) 区分使用：`gemini-frontend-design` 偏轻量、直接、强针对 Gemini 4 视觉与排版规则约束；`impeccable` 偏 24 条显式交互命令与确定性 Slop 检测引擎。

## 个人使用记录

- 2026-11-25：已通过 `npx skills add ... -g -y` 全局安装至 `~/.gemini/config/skills/gemini-frontend-design` 与 `~/.agents/skills/gemini-frontend-design`。
