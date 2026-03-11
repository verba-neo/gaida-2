# nodes.py
from state import State
from backend import dt_backend
import requests

def upload(state: State):
    files = state['files']

    for file in files:
        # 다운로드
        d = requests.get(file['link'])
        # 파일 업로드 이후 파일 저장된 위치를 state에 upload_paths 에 저장함
        dt_backend.upload_files(
            [
                (f'/home/daytona/data/{file['name']}.csv', '파일')
            ]
        )

    return {'upload_paths': '샌드박스에 저장된 파일 위치 목록'}


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