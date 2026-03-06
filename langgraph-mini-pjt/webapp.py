import os
import aiohttp
from fastapi import FastAPI, Request
from langchain.messages import HumanMessage
from app import agent


app = FastAPI()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    # 1. 텔레그램에서 보낸 JSON 데이터 읽기
    payload = await request.json()
    
    # 2. payload에서 메시지 추출 후 LangGraph 에이전트 호출 로직 작성
    message = payload.get('message')
    result = await agent.ainvoke(HumanMessage(content=message))
    
    # 3. Telegram API 로 bot에게 메시지 보내기
    answer = result['messages'][-1].content
    data = {'chat_id': 765946187, 'text': answer}
    await aiohttp.ClientSession().post(
        f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
        json=data
    )

    # 4. 텔레그램 서버에 정상 알림
    return {"ok": True}