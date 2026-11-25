---
name: asu-skills
aliases:
  - ASu-skills
  - 求职工作流
  - 简历制作
  - 面试准备
category: 写作与教学
description: 中文求职与开发提效 AI Skills 套件（9 个独立入口），覆盖开源贡献（/contributor）、AI 编程对话证据复盘（/evidence-recap）、项目导学面经（/project-guide）、简历提升（/great-resume）、可编辑 HTML/PDF/LaTeX 简历制作（/make-resume）、岗位匹配（/job-match）、浏览器投递填写（/job-apply）、简历深挖面试模拟（/interview）与校招进度及 Offer 决策（/offer）。准备求职、改写制作简历、梳理项目面经或跟踪校招进度时使用。
tags:
  - skill
  - career
  - resume
  - interview
  - job-search
  - open-source
  - chinese
  - workflow
repo: https://github.com/Hisn00w/ASu-skills
subpath: skills
ref: 5d6592acadcd77385a884c1de042986486cfe2bc
version: 0.4.0
install_cmd: npx github:Hisn00w/ASu-skills install --codex
requires:
  - Node.js ^22.19.0 或 >=24.0.0（运行 CLI 与简历构建/PDF 导出脚本）
  - 可选：Kimi WebBridge 或 Edge ChatGPT 浏览器扩展（仅 /job-apply 填表时需要）
reviewed: false
added: 2026-11-25
---

# ASu-skills（中文求职与开发提效技能套件）

> 仓库地址：[Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) · 官网：[hisn00w.github.io/ASu-skills](https://hisn00w.github.io/ASu-skills/)（License: MIT）

面向中文技术求职与开发复盘的一体化 Agent Skills 套件（`skills.registry.json` 统一管理），包含 **9 个可单独调用、也可串联配合的斜杠入口**，强调真实经历与可核验证据链（禁止编造经历或批量骚扰海投）。

## 包含的 9 个核心入口（`skills/`）

| 入口 | 定位 | 主要交付 |
| :--- | :--- | :--- |
| `/contributor` | 开源贡献 | 匹配目标岗位筛选真实 Issue、展示 diff，经确认后提交 PR 并转交 `/great-resume` |
| `/evidence-recap` | 证据复盘 | 将 AI 编程对话与交付记录还原为可核验的九段证据链（自动泛化密钥/敏感路径） |
| `/project-guide` | 项目导学面经 | 基于代码库生成 `tutorial.md` / `practice.md` 源码课程，或 `导学`/`面经` 与 STAR 口播 |
| `/great-resume` | 简历提升 | 岗位定位、项目经历改写、成果证据补强清单与 HR 中文开场白 |
| `/make-resume` | 简历制作 | 内置 18 套中文可编辑 HTML 模板（默认 ASu 单栏高密度模板），支持 PDF 导出与可选 LaTeX `.tex` |
| `/job-match` | 岗位匹配 | 对照目标 JD 与真实经历输出要求—证据矩阵、硬性门槛和投递建议 |
| `/job-apply` | 简历投递填写 | 连接已登录浏览器填写单个职位申请表并上传附件，默认停在提交按钮前核对 |
| `/interview` | 面试准备 | 简历 Claim 预测、契约化连续追问（`/interview grill`）与薄弱点变体复练（`/interview retry`） |
| `/offer` | 校招进度 & Offer 决策 | 生成本地 `application-tracker.html` 跟踪投递邮件，并支持多 Offer 五维加权对比与谈判要点 |

## 下载与安装（给其他项目 / Agent 用）

> [!WARNING] 注意共享资源依赖
> 9 个 Skill 入口共用仓库根目录的 `assets/`（18 套简历模板、图标、进度表模板）、`references/` 和 `scripts/`（含 PDF 导出与 `kimi-webbridge.mjs`）。**建议使用官方一键安装 CLI 或平台插件安装**，不要只拷贝单个子目录而漏掉共享资源。

### 方式一：npm 一键安装 CLI（支持多 Agent，推荐）

```bash
# 从 GitHub 直接运行安装全部 9 个技能及共享资源（默认安装到 ~/.agents/skills）
npx github:Hisn00w/ASu-skills install --codex

# 也支持按目标平台与作用域指定参数：
# --claude-code | --cursor | --opencode | --workbuddy | --project | --dry-run
# 健康检查：npx github:Hisn00w/ASu-skills doctor
```

> 仓库在正式发布到 npm 后可改用 `npx asu-skills install --codex`；遇到非 ASu-skills 同名目录时安装会主动中止，确认备份后再加 `--force`。

### 方式二：Claude Code 插件市场 / 其他平台桥接

```text
# Claude Code
/plugin marketplace add Hisn00w/ASu-skills
/plugin install asu-skills@asu
```

- **DeepSeek Harness Desktop**：在插件面板选择“添加插件”，粘贴 `https://github.com/Hisn00w/ASu-skills.git` 安装。
- **Cursor / OpenCode / WorkBuddy / Qoder / TraeWork**：分别参见仓库根目录对应目录（`.cursor-skills/`、`.opencode-plugin/`、`.workbuddy-plugin/`、`.qoder-plugin/`、`.trae-plugin/`）内的安装说明。

## 依赖与安全提示

- **Node.js 版本**：`package.json` 要求 `^22.19.0 || >=24.0.0`；可选 LaTeX `.tex` 导出推荐在 Overleaf 选择 XeLaTeX 编译，无需本地装 TeX。
- **浏览器自动填表约束（`/job-apply`）**：需先本机安装并连接 [Kimi WebBridge](https://www.kimi.com/products/kimi-webbridge) 或 Edge ChatGPT 扩展；登录、密码、验证码、MFA 与 CAPTCHA 均须人工完成，不会绕过访问控制。
- **隐私提醒**：使用过程中切勿将真实姓名、手机号、邮箱、Cookie、密钥等个人隐私提交进公开仓库或公开 Skill 文件。
- **审核状态**：当前 `reviewed: false`。

## 个人使用记录

- 
