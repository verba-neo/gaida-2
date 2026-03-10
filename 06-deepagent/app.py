# app.py
from dotenv import load_dotenv
load_dotenv()

from langgraph.checkpoint.memory import InMemorySaver
from deepagents import create_deep_agent

from tools import send_slack_message
from backend import dt_backend

agent = create_deep_agent(
    model='openai:gpt-5-mini',
    tools=[send_slack_message],
    backend=dt_backend,
)