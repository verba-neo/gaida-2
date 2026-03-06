# app.py

# 노드 import
# 엣지 import
# 라우터 import
# graph 조립

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langgraph.graph import START, END, StateGraph, MessagesState
from typing import TypedDict
from dotenv import load_dotenv

from tools import get_weather

load_dotenv()

llm = init_chat_model('gpt-4.1-mini')

agent = create_agent(
    llm,
    tools=[get_weather],
    system_prompt='뭐든 잘 하는 에이전트'
)
