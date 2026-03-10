from langgraph.graph import MessagesState


class State(MessagesState):
    files: list


'''
{
    'files': ['/a/b/c.csv', '/x/y/z.py'],
    'messages': [
        HumanMessage(content='hi'),
        AIMessage(content='hello')
    ]
}
'''
