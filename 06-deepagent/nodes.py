# nodes.py
import os
from dotenv import load_dotenv
from state import State
from backend import dt_backend
import requests

load_dotenv()

def upload(state: State):
    upload_paths = []
    
    files = state['files']
    for file in files:
        # 다운로드
        token = os.getenv('SLACK_BOT_TOKEN')
        headers = {
            "Authorization": f"Bearer {token}"
        }
        res = requests.get(file['link'], headers=headers)
        local_path = f'./tmp/{file['name']}'

        with open(local_path, 'wb') as f:
            f.write(res.content)
        
        # 다운받은 파일 열기
        with open(local_path, 'rb') as f:
            file_bytes = f.read()

        # 파일 업로드 이후 파일 저장된 위치를 state에 upload_paths 에 저장함
        sandbox_path = f'/home/daytona/data/{file['name']}'
        dt_backend.upload_files(
            [
                (sandbox_path, file_bytes)
            ]
        )
        upload_paths.append(sandbox_path)

    return {'upload_paths': upload_paths}


