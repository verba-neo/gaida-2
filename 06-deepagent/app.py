# app.py
from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import START, END, StateGraph

from state import State
from nodes import upload
from routers import check_files
from agents import run_deep_agent


workflow = StateGraph(State)
workflow.add_node('run_deep_agent', run_deep_agent)
workflow.add_node('upload', upload)

workflow.add_conditional_edges(
    START,
    check_files,
    {
        'upload': 'upload',
        'run_deep_agent': 'run_deep_agent'
    }
)
workflow.add_edge('upload', 'run_deep_agent')
workflow.add_edge('run_deep_agent', END)

graph = workflow.compile()