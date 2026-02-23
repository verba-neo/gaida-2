# 파일명: server.py

# (ctrl + `) 으로 터미널 열기
# 터미널에 pip install flask 입력

from flask import Flask

app = Flask(__name__) 


@app.route("/")
def main():
    # 응답
    return "<p>Hello, World!</p>"


@app.route("/qwer")  # URL
def about():
    # 응답
    return "<p>HAHAHA</p>"


if __name__ == '__main__':
    app.run(port=3000, debug=True)
