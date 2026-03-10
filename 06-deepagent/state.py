from langgraph.graph import MessagesState


class State(MessagesState):
    # messages
    files: list
    upload_paths: list


'''
{
    'files': ['a.csv', 'b.py'],
    'upload_paths': [
        '/home/daytona/data/a.csv',
        '/home/daytona/data/b.py',
    ],
    'messages': [
        HumanMessage(content='hi'),
        AIMessage(content='hello')
    ]
}
'''
