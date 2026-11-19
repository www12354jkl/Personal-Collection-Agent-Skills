---
name: drawio-skill
description: 将自然语言、代码、Terraform/K8s、SQL、OpenAPI/AsyncAPI、Protobuf、GraphQL 等转换为可编辑的 .drawio 架构图，支持增量同步、多视图投影、CI 架构规则测试、白板转图及导出 HTML/PPTX/Mermaid。当需要生成或维护可编辑的 draw.io / diagrams.net 图表时使用。
tags:
  - skill
  - diagram
  - drawio
  - architecture
  - visualization
repo: https://github.com/Agents365-ai/drawio-skill
subpath: skills/drawio-skill
ref: 6550495129d9a42eff7e71434d15bfc9846b6202
version: 3.4.4
install_cmd: npx skills add Agents365-ai/drawio-skill
requires:
  - python3
  - draw.io desktop CLI (>=30 推荐, Windows 为 draw.io.exe)
  - graphviz (可选)
reviewed: false
added: 2026-11-19
---

# drawio-skill

> 仓库地址：[Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill)（License: MIT）

把自然语言描述和真实工程源码转换成可持续维护的 `.drawio` 图表模型（而非一次性静态图片），仅在需要轻量纯文本图（Mermaid/PlantUML 足够解决）时才优先用代码画图。

## 适用场景与核心能力

- **自然语言作图 & 自检**：规划布局并输出 `.drawio` XML，导出后可自检 PNG 修复节点重叠、连线交叉和标签截断；支持 11 种图表预设（C4、ER、UML、序列图、架构图、泳道图、网络拓扑等）。
- **从真实工程源生成**：
  - 代码依赖/类图：Python、JS/TS、Go、Rust
  - 基础设施与实时状态：Terraform、Kubernetes、docker-compose（支持 `terraform show -json`、`kubectl get -o json`、`docker inspect`）
  - Schema 与流水线：SQL DDL、OpenAPI/Swagger、AsyncAPI、Protobuf、GraphQL、GitHub Actions / GitLab CI
- **长期演进与交付**：`diagramctl` 支持不丢人工布局的增量 `sync`、多视图投影（系统/部署/数据流/安全）、架构规则测试（CI Gate）、白板/截图转 `.drawio`、导出交互式 HTML / PPTX / 动画 SVG / Mermaid。

## 下载与安装（给其他项目 / Agent 用）

> [!WARNING] 注意子目录位置
> 该仓库根目录包含文档、测试和示例，**真正的 Skill 包位于 `skills/drawio-skill/`**。安装时只能把该子目录放进目标项目的 `.agents/skills/drawio-skill/`，不要把整个仓库根目录克隆进去。

### 方式一：使用 skills CLI

```bash
# 安装到当前项目
npx skills add Agents365-ai/drawio-skill

# 或全局安装
npx skills add Agents365-ai/drawio-skill -g
```

### 方式二：Git 稀疏检出（只拉取所需子目录）

```powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/Agents365-ai/drawio-skill.git _tmp_drawio
git -C _tmp_drawio sparse-checkout set skills/drawio-skill
New-Item -ItemType Directory -Force -Path .agents/skills | Out-Null
Copy-Item -Recurse -Force _tmp_drawio/skills/drawio-skill .agents/skills/drawio-skill
Remove-Item -Recurse -Force _tmp_drawio
```

> 如需严格锁定收录时的版本，可在复制前先核对或切换至记录的 `ref`（`6550495129d9a42eff7e71434d15bfc9846b6202`）。

## 依赖与使用提示

- **Python 3**：核心 IR、XML 生成、sync、query、test 等工作流仅依赖 Python 3 标准库，默认离线可用。
- **draw.io 桌面版 CLI**：导出图片、Mermaid 原生转 `.drawio` 以及 ELK 自动布局需要本机安装 draw.io 桌面版（Windows 下为 `draw.io.exe`，推荐 `>= 30` 版本）。
- **Graphviz（可选）**：部分代码库自动布局使用 `dot`。
- **安全说明**：该 Skill 包含大量 `scripts/` 工具脚本（入口为 `scripts/diagramctl.py`，也提供 `scripts/diagramctl_mcp.py`），当前标记 `reviewed: false`，首次在重要项目执行前建议先快速过一眼脚本内容。

## 个人使用记录

- 
