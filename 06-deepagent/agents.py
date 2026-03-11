from deepagents import create_deep_agent

from state import State
from tools import send_slack_message
from backend import dt_backend


SYSTEM_PROMPT="""You are an expert assistant. Your job is to conduct thorough research and then write a polished report.

Slack channel is set. Always Respond to slack channel using tool.

## send_slack_message
"""


def run_deep_agent(state: State):
    deep_agent = create_deep_agent(
        model='openai:gpt-5-mini',
        tools=[send_slack_message],
        backend=dt_backend,
        system_prompt=SYSTEM_PROMPT
    )

    messages = state["messages"]

    if state.get("upload_paths"):
        file_msg = {
            "role": "system",
            "content": f"Uploaded files are located at: {state['upload_paths']}"
        }

        messages = messages + [file_msg]

    result = deep_agent.invoke({
        "messages": messages
    })

    return {
        "messages": result["messages"]
    }

