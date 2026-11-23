---
name: remotion
aliases:
  - remotion-best-practices
  - remotion-skills
category: 图像与视频
description: Remotion 官方视频编程生态与 13 个 Agent Skills 合集（含 remotion-best-practices、create、markup、studio、render、maps、captions、saas 等），帮助 Agent 用 React 代码编程式生成、预览与渲染视频、字幕和地图动画。需要在项目中用 React/Remotion 制作或渲染程序化视频时使用。
tags:
  - skill
  - video
  - react
  - animation
  - remotion
  - multimedia
repo: https://github.com/remotion-dev/remotion
subpath: packages/skills/skills
ref: 3fcd5ae3eb8b30f40037983410217183ce3ddb81
version: 4.0.545
install_cmd: npx skills add remotion-dev/skills
requires:
  - Node.js
  - React >= 16.8.0 (项目使用 Remotion 渲染视频时)
reviewed: true
added: 2026-11-19
---

# Remotion (Agent Skills + Framework)

> 仓库地址：[remotion-dev/remotion](https://github.com/remotion-dev/remotion) · Skills 文档：[remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills)

用 React 和 Web 技术以代码形式制作、预览与批量渲染视频的框架，并在仓库 `packages/skills/skills/` 中维护了一套官方 Agent Skills。

## 包含的官方 Skills（共 13 个）

- **`remotion-best-practices`**：总控 Skill，涵盖其余核心规范（不确定选哪个时用它）。
- **创作与编码**：`remotion-create`（新建项目/合成）、`remotion-markup`（动画、布局、排版、音视频、字体、时间轴最佳实践）、`remotion-maps`（Mapbox/MapLibre/GeoJSON/CesiumJS 地图路径动画）、`remotion-captions`（字幕）、`remotion-multimedia`（Mediabunny 多媒体元数据处理）。
- **预览、渲染与维护**：`remotion-studio`、`remotion-render`（含 OpenTimelineIO 导出）、`remotion-interactivity`、`remotion-saas`、`remotion-docs`、`remotion-license`、`remotion-upgrade`。

## 下载与安装（给其他项目 / Agent 用）

> [!WARNING] 仓库体积很大，切勿整库克隆进项目
> `remotion-dev/remotion` 是完整的 Monorepo。安装 Skill 请优先用官方 CLI 或稀疏检出 `packages/skills/skills/`。

### 方式一：官方 CLI（推荐）

```bash
# 未安装 Remotion 的项目 / 通用安装
npx skills add remotion-dev/skills

# 或使用 GitHub CLI
gh skill install remotion-dev/skills

# 若项目已安装 remotion 依赖
npx remotion skills add

# 新建 Remotion 视频项目并自动带入全部 Skills
npx create-video@latest --skills
```

### 方式二：Git 稀疏检出指定 Skill（如 `remotion-best-practices`）

```powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/remotion-dev/remotion.git _tmp_remotion
git -C _tmp_remotion sparse-checkout set packages/skills/skills/remotion-best-practices
New-Item -ItemType Directory -Force -Path .agents/skills | Out-Null
Copy-Item -Recurse -Force _tmp_remotion/packages/skills/skills/remotion-best-practices .agents/skills/remotion-best-practices
Remove-Item -Recurse -Force _tmp_remotion
```

> 注：`.agents/skills/` 中对应的 `remotion-*` 目录是指向 `packages/skills/skills/` 的符号链接，直接拉取 `packages/skills/skills/` 最稳妥（尤其在 Windows 上）。

## 依赖与许可证提示

- **特殊许可证**：Remotion 采用定制开源协议（见仓库 `LICENSE.md`），**商业公司在特定规模/场景下需要购买企业授权**，生产使用前务必先核对条款。
- **审核状态**：当前 `reviewed: false`。

## 个人使用记录

- 
