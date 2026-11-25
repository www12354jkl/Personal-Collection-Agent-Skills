---
name: find-skills
aliases:
  - skills.sh
  - 技能检索
category: Agent编排
description: Vercel Labs 官方的 Agent Skills 发现与安装指导技能，引导 Agent 通过 skills.sh 排行榜和 npx skills find / add 命令搜索、甄别并安装社区技能包。当本地目录未命中、需要从开放生态查找并扩展新技能能力时使用。
tags:
  - skill
  - agent
  - skills-cli
  - discovery
  - package-management
repo: https://github.com/vercel-labs/skills
subpath: skills/find-skills
ref: 57217cf86ba38148a57af9e90d14a4c049558330
version: 1.9.0
install_cmd: npx skills add https://github.com/vercel-labs/skills --skill find-skills
requires:
  - Node.js >= 22.20.0（运行 npx skills find / add / update）
reviewed: true
added: 2026-11-25
---

# find-skills

> 仓库来源：[vercel-labs/skills](https://github.com/vercel-labs/skills) · 生态索引：[skills.sh](https://skills.sh/)（License: MIT）

引导编码 Agent 通过 `npx skills` CLI 在 `skills.sh` 开放生态中搜索、筛选并安装 Agent Skills；与本地优先检索规则搭配时，适合作为本地目录未命中时的外部兜底检索入口。

## 适用场景与核心能力

- **按需检索生态技能**：通过 `npx skills find [query] [--owner <owner>]` 或先看 `skills.sh` 排行榜定位高安装量成熟技能。
- **质量甄别门禁**：推荐前要求核验安装量（优先 `1K+`，警惕 `< 100`）、发布者信誉（优先官方组织）以及源仓库 GitHub Stars，不盲目推荐搜索结果。
- **一键安装与更新**：通过 `npx skills add <owner/repo@skill> -g -y` 全局或项目级安装，支持 `npx skills update` 与 `npx skills ls -g`。

## 下载与安装（给其他项目 / Agent 用）

### 方式一：Vercel skills CLI（推荐）

```bash
# 安装到当前项目
npx skills add https://github.com/vercel-labs/skills --skill find-skills

# 全局安装（同步至 Antigravity 与通用 .agents/skills）
npx skills add https://github.com/vercel-labs/skills --skill find-skills -g -y
```

### 方式二：Git 稀疏检出（只拉取 `skills/find-skills`）

```powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/vercel-labs/skills.git _tmp_skills
git -C _tmp_skills sparse-checkout set skills/find-skills
New-Item -ItemType Directory -Force -Path .agents/skills | Out-Null
Copy-Item -Recurse -Force _tmp_skills/skills/find-skills .agents/skills/find-skills
Remove-Item -Recurse -Force _tmp_skills
```

## 依赖与安全提示

- 整个 Skill 仅包含单文件 `SKILL.md`（约 5.5 KB，无自带可执行脚本）；执行其中的 `npx skills find` / `add` 需要 `Node.js >= 22.20.0`。
- `skills.sh` 页面中 Snyk 标为 `Med Risk` 主要源于指导 Agent 调用外部 `npx skills add` 安装第三方技能；实际安装未知第三方技能前仍应先审查来源和脚本内容。
- 已核查全文，标记 `reviewed: true`。

## 个人使用记录

- 2026-11-25：已全局安装至 `~/.gemini/config/skills/find-skills` 与 `~/.agents/skills/find-skills`。
