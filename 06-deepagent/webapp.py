from fastapi import FastAPI, Request, BackgroundTasks
from app import graph
from langchain.messages import HumanMessage
import re

app = FastAPI()


async def run_agent(text, files):
    text = re.sub(r"<@[^>]+>", "", text).strip()

    await graph.ainvoke({
        "messages": [HumanMessage(content=text)],
        "files": files
    })


@app.post("/slack/webhook")
async def slack_webhook(req: Request, background_tasks: BackgroundTasks):

    payload = await req.json()

    # 1️⃣ Slack URL verification (제일 먼저)
    if payload.get("type") == "url_verification":
        return {"challenge": payload["challenge"]}

    # 2️⃣ Slack retry 방지
    if req.headers.get("x-slack-retry-num"):
        return {"ok": True}

    event = payload.get("event", {})

    # 3️⃣ 쓸데없는 이벤트 컷
    if event.get("type") != "app_mention":
        return {"ok": True}

    text = event.get("text", "")
    files_info = event.get("files", [])

    files = []

    for file in files_info:
        files.append({
            "name": file["name"],
            "link": file["url_private_download"]
        })

    # 4️⃣ agent 실행
    background_tasks.add_task(run_agent, text, files)

    return {"ok": True}