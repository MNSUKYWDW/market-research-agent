import os


def call_llm(prompt: str, system: str = "") -> str:
    if os.environ.get("MOCK_LLM") == "1":
        return "MOCK_LLM_RESPONSE"

    from openai import OpenAI

    client = OpenAI(
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        api_key=os.environ["DASHSCOPE_API_KEY"],
    )
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=os.environ.get("AGENT_LLM_MODEL", "qwen-turbo"),
        messages=messages,
    )
    return response.choices[0].message.content
