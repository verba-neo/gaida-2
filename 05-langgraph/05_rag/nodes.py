# nodes.py
from langchain.messages import HumanMessage
from langchain.chat_models import init_chat_model

from tools import retrieve_blog_posts
from prompts import REWRITE_QUESTION_PROMPT, GENERATE_ANSWER_PROMPT
from state import CustomMessagesState


res_llm = init_chat_model('gpt-4.1', temperature=0)


def generate_query_or_respond(state: CustomMessagesState):
    """llm이 사용자 대화를 기반으로 바로 답변을 생성하거나
    RAG를 위한 query 를 결정한다."""
    tllm = res_llm.bind_tools([retrieve_blog_posts])
    res = tllm.invoke(state['messages'])
    return {'messages': [res]}


def rewrite_question(state: CustomMessagesState):
    """사용자 질문을 재작성합니다. tool 호출이 아닌 메시지만을 대화 기록으로 사용합니다."""
    # rewrite_count를 1 증가시킵니다.
    rewrite_count = state.get('rewrite_count', 0) + 1

    messages = state['messages']
    # tool 호출이 아닌 메시지만을 필터링합니다.
    conversation_history = [
        msg for msg in messages if not (hasattr(msg, 'tool_calls') and msg.tool_calls)
    ]

    # 대화 기록을 문자열로 변환합니다.
    history_str = ""
    for msg in conversation_history:
        if isinstance(msg, HumanMessage):
            history_str += f"Human: {msg.content}\n"
        else:
            history_str += f"AI: {msg.content}\n"

    # 마지막 사용자 질문을 가져옵니다.
    last_human_message = ""
    for msg in reversed(conversation_history):
        if isinstance(msg, HumanMessage):
            last_human_message = msg.content
            break

    prompt = REWRITE_QUESTION_PROMPT.format(
        history=history_str, original_question=last_human_message
    )
    response = res_llm.invoke(prompt)
    return {'messages': [HumanMessage(content=response.content)], "rewrite_count": rewrite_count}


def generate_answer(state: CustomMessagesState):
    """최종 답변 생성"""
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

    docs = state['messages'][-1].content  # 마지막 RAG docs
    prompt = GENERATE_ANSWER_PROMPT.format(question=question, docs=docs)
    res = res_llm.invoke(prompt)
    return {'messages': [res]}
