# routers.py
from state import State

def check_files(state: State):
    files = state.get('files', [])

    if files:
        return 'upload'
    else:
        return 'run_deep_agent'