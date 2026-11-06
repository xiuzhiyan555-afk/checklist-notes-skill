# 清单体笔记Skill

把口述、文章和工作材料整理成主次清楚、便于阅读的 Obsidian 笔记。按内容选择清单或表格，主动标记关键词重点。

## 怎么用

前提：你已有 Obsidian 笔记库，以及能访问本地文件的 Agent，例如 WorkBuddy 或 Codex。

把本仓库链接发给 Agent，再复制这句话：

> 请下载这个仓库，读取 `checklist-notes/SKILL.md` 和 `checklist-notes/references/安装与兼容.md`，帮我安装清单体笔记Skill，并在我的 Obsidian 库中启用配套样式、放入样例检查效果。请自动完成可以执行的步骤，需要我授权或操作时，只告诉我当前必需的一步。我的 Obsidian 库位置是：［填入或拖入库文件夹］。

安装后说：

> 请用清单体笔记Skill整理这份材料，保存到我的 Obsidian Inbox。

## 下载

如果 Agent 无法直接访问 GitHub，下载并解压[纯技能包](checklist-notes-skill-v0.6.zip)，把解压后的 `checklist-notes` 文件夹交给 Agent，再发送上面的指令。

[了解整理规则](清单体笔记Skill.md) · [安装指引](checklist-notes/references/安装与兼容.md)

## 文件说明

只有一个 Skill：`checklist-notes/SKILL.md` 是 AI 规则入口，`清单体笔记Skill.md` 是给人看的说明。`checklist-notes/assets/checklist-notes.css` 是配套样式，`checklist-notes/scripts/install_obsidian.py` 是一键安装脚本，`checklist-notes-skill-v0.6.zip` 是 WorkBuddy 可上传的纯技能包。

## 环境说明

样式以 Obsidian 默认主题（无第三方主题）为基准设计，无法保证在每台电脑上完全一致——电脑与系统、Obsidian 版本、启用的主题、库里已有的 CSS 片段都可能影响显示。发现颜色、表格等样式不规范时，直接请 AI 针对性调整即可，不必自己排查。

## 使用边界

只整理已有材料，不代写尚未形成的思考。绿色关键词效果需要启用配套 CSS；不同主题及编辑模式需用样例检查。安装可能需要文件访问授权或重启 Agent；不能把文件复制成功当作显示验收完成。
