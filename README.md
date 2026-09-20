# my-first-server

리눅스/서버 학습용 연습 프로젝트입니다.
정적 웹페이지(HTML)와, 코드로 응답하는 살아있는 서버(Flask)를 담고 있어요.

## 구성
- `index.html` : 정적 홈 페이지
- `about.html` : 정적 소개 페이지 (홈과 링크 연결)
- `app.py` : Flask 서버 (요청마다 현재 시각을 새로 만들어 응답)

## 실행 방법
### 정적 페이지 (죽은 서버)
`python3 -m http.server 8888` → http://localhost:8888

### Flask 서버 (살아있는 서버)
`source venv/bin/activate` 후 `python app.py` → http://localhost:5000 (F5 누르면 시각이 바뀜)

## 학습 기록
- 2026-09-19: 첫 웹서버 + 미니 웹사이트(여러 페이지 링크)
- 2026-09-20: Git 버전관리 + GitHub 업로드
- 2026-09-20: Flask로 "살아있는 서버" 제작 (요청마다 현재 시각 생성)
