---
name: antigrative-dashboard
aliases:
  - antigravity-pulse
  - Antigrative Dashboard
description: 在 Antigravity 模型选择器旁实时展示生成速率（tok/s）、缓存命中率、上下文占用与 5 小时 / 周共享额度，支持桌面 App、独立 IDE 与 CLI 状态栏，并支持中英文切换。需要监控 Antigravity Token 吞吐量与额度消耗时使用。
tags:
  - plugin
  - antigravity
  - dashboard
  - token
  - quota
  - monitoring
repo: https://github.com/ATtacK030130/antigrative-dashboard
subpath: .
ref: 771ade942a3392a2bfb56bb4c0874168bd69d6f5
version: 0.9.6
install_cmd: python manage.py install
requires:
  - Python 3.10+
  - Antigravity Desktop (2.21.1 - 2.33.0) / 独立 Antigravity IDE / CLI (Node.js 20+)
reviewed: true
added: 2026-11-19
---

# Antigrative Dashboard

> 仓库地址：[ATtacK030130/antigrative-dashboard](https://github.com/ATtacK030130/antigrative-dashboard)（插件 ID：`antigravity-pulse`，License: MIT）

紧凑型 Antigravity Token 吞吐量与额度监控插件：缩略指标常驻在模型选择旁，鼠标悬停展开详情，数据全部通过本地回环接口读取，不向外上传采集数据。

## 核心能力与适配宿主

- **核心监控指标**：当前会话加权与最近一次请求 `tok/s`、缓存读取/命中率、当前上下文占用估计、消耗预测，以及 Gemini / Claude & GPT 分组 5h 与周额度及重置倒计时。
- **支持子代理与多层级**：主对话与子代理（subagent / Teamwork）分别展示统计并做请求去重汇总，切换对话自动刷新统计，跟随宿主深浅主题并持久保存中英文切换。
- **三种宿主模式**：
  - **Antigravity 桌面 App**（Windows / Linux / macOS，2.21.1 – 2.33.0）
  - **独立 Antigravity IDE**（通过 Release 的 `.vsix` 安装；VS Code 等编辑器里的 Antigravity 扩展暂未兼容）
  - **Antigravity CLI 状态栏**（需 Node.js 20+，展示上下文、缓存读取与额度进度，不含 `tok/s`）

## 下载与安装（给后续设备 / Agent 用）

> [!WARNING] 注意事项
> 1. **区分宿主**：安装前先确认目标机器装的是 **桌面 App**、**独立 IDE** 还是 **CLI（`agy`）**，三者安装命令不同。
> 2. **保留目录**：桌面 App / CLI 模式安装后需**保留克隆或解压后的目录**，用于后续启停、升级与卸载。
> 3. **调试端口**：Antigravity Desktop 2.33.0+ 及独立 IDE 需要 `--remote-debugging-port=0 --remote-debugging-address=127.0.0.1`；桌面版 `manage.py install` 会自动配置快捷方式/启动器。

### 方式一：桌面 App（Windows PowerShell）

```powershell
git clone https://github.com/ATtacK030130/antigrative-dashboard.git
cd antigrative-dashboard
python manage.py install
# 或者运行：.\install.ps1
```

> Linux / macOS 将 `python` 换为 `python3`（或运行 `sh install.sh`）；之后完全重启 Antigravity 即可生效。

### 方式二：Antigravity CLI 状态栏

```bash
python manage.py install-cli
# 预览效果：node cli/statusline.mjs --preview --language zh-CN
```

### 方式三：独立 Antigravity IDE

1. 从 [GitHub Releases](https://github.com/ATtacK030130/antigrative-dashboard/releases/latest) 下载对应版本的 `.vsix`（如 `antigrative-dashboard-ide-0.9.6.vsix`），在 IDE 扩展页选择「从 VSIX 安装」（或使用 `ide/manage.py install`）。
2. 为 IDE 启动快捷方式末尾追加参数：`--remote-debugging-port=0 --remote-debugging-address=127.0.0.1` 并重启。

## 依赖与安全提示

- 桌面 App 与 IDE 无第三方 pip / npm 依赖，后台复用应用自带 Node.js；安装器脚本需 **Python 3.10+**。
- 仓库内包含平台适配、sidecar 注入及快捷方式修改脚本（如 `manage.py`、`install.ps1`），当前标记 `reviewed: false`，首次在新环境运行前建议先核对版本与脚本内容。

## 个人使用记录

- 
