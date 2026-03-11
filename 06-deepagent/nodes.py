# nodes.py
from state import State
from backend import dt_backend


def upload(state: State):
    print('-------------------------')
    print(state)
    print('-------------------------')

    # dt_backend.upload_files(
    #     [
    #         ('/home/daytona/data/sales_data.csv', csv_bytes)
    #     ]
    # )
    return {'messages': [{'role': 'ai', 'content': 'ok'}]}


# def upload(state: State):
#     print('-------------------------')
#     print(state)
#     print('-------------------------')

#     # dt_backend.upload_files(
#     #     [
#     #         ('/home/daytona/data/sales_data.csv', csv_bytes)
#     #     ]
#     # )
#     return {'messages': [{'role': 'AI', 'content': 'ok'}]}