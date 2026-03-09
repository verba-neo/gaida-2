# state.py
from typing import TypedDict, Annotated
from langgraph.graph import MessagesState

# `rewrite_count` 를 추가하기 위해 상태를 정의합니다.
class CustomMessagesState(MessagesState):
    rewrite_count: int
