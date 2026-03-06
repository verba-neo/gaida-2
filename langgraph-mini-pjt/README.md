# 실습 플젝 최소 조건
## 오전 세팅은 youtube 업로드 완

1. 텔레그램 봇과 대화 시작
2. 날씨를 물어봄
    1. ngrok 서버로 webhook 날라감
    2. ngrok -> langgraph dev 서버로 요청 보냄 (localhost:2024 뒤에 routing 존재)
    3. langgraph dev 서버가 llm 으로 답변 생성
        1. OpenWeatherAPI로 날씨정도는 답변할 수 있도록 tool 세팅   
    4. telegram API로 메세지 전송
3. 날씨를 알려줌


1. 텔레그램 메시지 보내기
1. `ngrok http 2024` 로 서버 실행
2. webhook 이 <ngrok-URL>/telegram/webhook 으로 요청 보냄
3. ngrok 이 localhost:2024/telegram/webhook 으로 요청 보냄
4. `webapp.py` 에서 `telegram_webhook` 함수 실행
5. 함수 내부에서 agent 호출 및 텔레그램 메시지 보내기