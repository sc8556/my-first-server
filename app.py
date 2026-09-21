from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>살아있는 서버 🎉 (Docker 컨테이너 안에서 실행 중!)</h1><p>지금 시각: {now}</p><p>새로고침(F5) 해보세요. 시간이 바뀝니다!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
