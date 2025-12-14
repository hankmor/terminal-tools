#!/usr/bin/env python3
"""
自动统计 terminal_tools.md 中的工具数量并更新 README.md
"""

import re
from pathlib import Path


def count_tools_in_section(content: str, section_name: str) -> int:
    """统计指定章节中的工具数量"""
    # 匹配章节开始到下一个章节或文件结束
    pattern = rf"^## {re.escape(section_name)}$.*?(?=^## |\Z)"
    section_match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    
    if not section_match:
        return 0
    
    section_content = section_match.group(0)
    # 统计 ### [工具名称] 的数量
    tools = re.findall(r"^### \[.+?\]", section_content, re.MULTILINE)
    return len(tools)


def update_readme_stats(tools_file: Path, readme_file: Path) -> None:
    """更新 README 中的统计数据"""
    
    # 读取文件
    tools_content = tools_file.read_text(encoding="utf-8")
    readme_content = readme_file.read_text(encoding="utf-8")
    
    # 定义分类映射
    categories = {
        "编辑器": "🎨 [编辑器]",
        "开发工具": "💻 [开发工具]",
        "文件管理": "📁 [文件管理]",
        "系统工具": "🖥️ [系统工具]",
        "网络工具": "🌐 [网络工具]",
        "数据库工具": "🗄️ [数据库工具]",
        "图片处理": "🎨 [图片处理]",
        "阅读工具": "📖 [阅读工具]",
        "TUI 开发库": "🛠️ [TUI 开发库]",
    }
    
    print("📊 工具统计结果：")
    
    # 统计并更新每个分类
    for section_name, display_name in categories.items():
        count = count_tools_in_section(tools_content, section_name)
        print(f"  {section_name}: {count}")
        
        # 更新 README 中对应行的数量
        # 匹配表格行，例如：| 🎨 [编辑器](...) | ... | 4+ |
        pattern = rf"(\| {re.escape(display_name)}\(.*?\) \| .*? \| )\d+(\+ \|)"
        replacement = rf"\g<1>{count}\g<2>"
        readme_content = re.sub(pattern, replacement, readme_content)
    
    # 写回文件
    readme_file.write_text(readme_content, encoding="utf-8")
    print("\n✅ README.md 已更新！")


def main():
    # 获取项目根目录
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    tools_file = project_root / "terminal_tools.md"
    readme_file = project_root / "README.md"
    
    # 检查文件是否存在
    if not tools_file.exists():
        print(f"❌ 错误: {tools_file} 不存在")
        return 1
    
    if not readme_file.exists():
        print(f"❌ 错误: {readme_file} 不存在")
        return 1
    
    # 更新统计
    update_readme_stats(tools_file, readme_file)
    return 0


if __name__ == "__main__":
    exit(main())
