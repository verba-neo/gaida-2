# routers.py
from pydantic import BaseModel, Field
from langchain.messages import HumanMessage
from langchain.chat_models import init_chat_model

from prompts import GRADE_PROMPT
from state import CustomMessagesState


grader_llm = init_chat_model('gpt-4.1', temperature=0)


class GradeDocuments(BaseModel):
    """문서를 yes/no 로 질문과 연관있는지 평가"""
    binary_score: str = Field(description='연관성 점수: 연관 있으면 "yes", 연관 없으면 "no"')


def grade_document(state: CustomMessagesState):
    """검색해온 문서가 사용자 질문과 관련이 있는지 체크 후 다음 노드 결정"""
    messages = state['messages']
    # tool 호출이 아닌 메시지만을 필터링합니다.
    conversation_history = [
        msg for msg in messages if not (hasattr(msg, 'tool_calls') and msg.tool_calls)
    ]
    # 마지막 사용자 질문을 가져옵니다.
    question = ""
    for msg in reversed(conversation_history):
        if isinstance(msg, HumanMessage):
            question = msg.content
            break

    docs = state['messages'][-1].content

    prompt = GRADE_PROMPT.format(question=question, docs=docs)
    ollm = grader_llm.with_structured_output(GradeDocuments)
    res = ollm.invoke([{'role': 'user', 'content': prompt}])

    score = res.binary_score

    if score == 'yes':
        return 'generate_answer'
    else:
        return 'rewrite_question'


def route_after_rewrite(state: CustomMessagesState):
    """질문 재작성 후 다음 노드를 결정합니다."""
    rewrite_count = state.get('rewrite_count', 0)
    if rewrite_count >= 2:
        return 'generate_answer'
    return 'generate_query_or_respond'
