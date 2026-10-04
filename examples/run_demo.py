"""运行完整流程的示例脚本。

需要真实的环境变量 DASHSCOPE_API_KEY 和 TAVILY_API_KEY，不在 pytest 中运行。

用法::

    python examples/run_demo.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import graph  # noqa: E402


def main() -> None:
    """运行工作流并把报告写入当前目录下的 report.md。"""
    state = graph.run("Notion", "Southeast Asia")

    Path("report.md").write_text(state["report"], encoding="utf-8")
    print("Report saved to report.md")


if __name__ == "__main__":
    main()
