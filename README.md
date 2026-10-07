# market-research-agent

用 **LangGraph** 编排多个 LLM Agent，自动生成市场调研报告。

输入「产品 + 地区」，输出结构化 markdown 调研报告。

4 个节点共享 `AgentState`（LangGraph `StateGraph`），顺序执行：

- **planner**：把「产品 + 地区」拆成调研问题列表
- **retriever**：对每个问题调 Tavily 搜索
- **analyzer**：整理搜索结果，提炼要点
- **writer**：生成最终 markdown 报告

## 快速开始

```bash
pip install -r requirements.txt
export DASHSCOPE_API_KEY=...
export TAVILY_API_KEY=...

# 端到端（真调 LLM + Tavily）
python examples/run_demo.py
cat report.md

# 测试（全 mock，不调 API）
pytest
