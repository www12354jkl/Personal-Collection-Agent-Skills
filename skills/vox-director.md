---
name: vox-director
description: "把主题、口播素材或参考照片制作成带旁白、字幕与音乐的动态纸质拼贴视频。"
tags:
  - skill
  - video
  - motion
  - ffmpeg
repo: "https://github.com/Alisa0808/vox-director"
subpath: "."
ref: "6a85a7c341610442a6a5b1885e6e0217ab82a11f"
version: "1.0.0"
install_cmd: "git clone https://github.com/Alisa0808/vox-director.git"
requires:
  - "ffmpeg、ffprobe 与 Atlas Cloud API Key"
  - "Python 3 与 Pillow（字幕和叠加层）"
reviewed: false
added: 2026-11-23
---

# vox-director

> 仓库来源 · [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) · [上游 SKILL.md](https://github.com/Alisa0808/vox-director/blob/6a85a7c341610442a6a5b1885e6e0217ab82a11f/SKILL.md)（MIT）

把主题、口播素材或参考照片制作成带旁白、字幕与音乐的动态纸质拼贴视频。

## 适用场景与核心能力

- 用分段脚本和镜头清单管理旁白、画面、节奏与素材。
- 通过 Atlas Cloud 生成分镜所需素材，再用本地 ffmpeg 合成成片。

## 下载与安装（给其他项目 / Agent 用）

技能目录位于仓库根目录。

```bash
git clone https://github.com/Alisa0808/vox-director.git
```

克隆仓库后，把完整的技能目录放入目标 Agent 的技能目录。上游也提供 `.skill` 归档。

## 依赖与安全提示

- ffmpeg、ffprobe 与 Atlas Cloud API Key。
- Python 3 与 Pillow（字幕和叠加层）。

## 个人使用记录

-
