# graph.py
from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from nodes import generate_answer, rewrite_question, generate_query_or_respond
from tools import retrieve_blog_posts
from routers import grade_document, route_after_rewrite
from state import CustomMessagesState


workflow = StateGraph(CustomMessagesState)

workflow.add_node('generate_query_or_respond', generate_query_or_respond)
workflow.add_node('rewrite_question', rewrite_question)
workflow.add_node('generate_answer', generate_answer)
workflow.add_node('retrieve', ToolNode([retrieve_blog_posts]))

workflow.add_edge(START, 'generate_query_or_respond')
workflow.add_conditional_edges(
    'generate_query_or_respond',
    tools_condition,
    {
        'tools': 'retrieve',
        '__end__': END,
    }
)
workflow.add_conditional_edges(
    'retrieve',
    grade_document,
    {
        'generate_answer': 'generate_answer',
        'rewrite_question': 'rewrite_question'
    }
)
workflow.add_conditional_edges(
    'rewrite_question',
    route_after_rewrite,
    {
        'generate_query_or_respond': 'generate_query_or_respond',
        'generate_answer': 'generate_answer'
    }
)
workflow.add_edge('generate_answer', END)
graph = workflow.compile()