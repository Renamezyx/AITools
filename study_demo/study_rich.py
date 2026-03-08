# main.py
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.progress import track
from time import sleep

# 强制终端显示 ANSI（PyCharm 内终端也尽量显示颜色）
console = Console(force_terminal=True)

# 1️⃣ 加粗 + 彩色文字
console.print("[bold magenta]=== Nanobot Rich Demo ===[/bold magenta]\n")

# 2️⃣ Markdown 演示
md_text = """
# Nanobot Project Demo

这是一个演示 **Rich** 库功能的小程序：

- 彩色文字
- 表格显示
- Markdown 渲染
- 动态进度条
"""

console.print(Markdown(md_text))

# 3️⃣ 表格演示
table = Table(title="Agent Tools Status")
table.add_column("Tool Name", style="cyan", no_wrap=True)
table.add_column("Status", style="green", justify="center")
table.add_row("weather_api", "✅ Running")
table.add_row("file_read", "⏳ Loading")
table.add_row("ai_inference", "⚡ Ready")
console.print(table)

# 4️⃣ 动态进度条
console.print("\n[bold yellow]Processing Tasks:[/bold yellow]")
for i in track(range(10), description="Processing..."):
    sleep(0.3)  # 模拟任务执行

# 5️⃣ 结束提示
console.print("\n[bold green]All tasks completed! 🎉[/bold green]")