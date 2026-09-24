# my-first-server

리눅스/서버 학습용 연습 프로젝트입니다.
정적 웹페이지(HTML), 살아있는 서버(Flask), Docker 컨테이너, AWS 배포까지 담고 있어요.

## 구성
- `index.html` : 정적 홈 페이지
- `about.html` : 정적 소개 페이지 (홈과 링크 연결)
- `app.py` : Flask 서버 (요청마다 현재 시각을 새로 만들어 응답)
- `requirements.txt` : 파이썬 의존성 목록
- `Dockerfile` : 이미지 빌드 레시피

## 실행 방법
### 1) 정적 페이지 (죽은 서버)
`python3 -m http.server 8888` → http://localhost:8888

### 2) Flask 서버 (살아있는 서버)
`source venv/bin/activate` 후 `python app.py` → http://localhost:5000

### 3) Docker로 실행 (venv 불필요)
`docker build -t my-flask-app .` 후 `docker run -p 5000:5000 my-flask-app` → http://localhost:5000

### 4) AWS EC2에 배포 (인터넷 공개)
Ubuntu 서버에 Docker Engine(`docker.io`)을 설치한 뒤, 서버에서:
1. `git clone https://github.com/sc8556/my-first-server.git` → `cd my-first-server`
2. `sudo docker build -t my-flask-app .`
3. `sudo docker run -d -p 5000:5000 --name my-flask my-flask-app`
4. 브라우저에서 `http://<서버 퍼블릭 IP>:5000` (AWS 보안 그룹에서 5000번 허용 필요)

## 학습 기록
- 2026-09-19: 첫 웹서버 + 미니 웹사이트(여러 페이지 링크)
- 2026-09-20: Git 버전관리 + GitHub 업로드
- 2026-09-20: Flask로 "살아있는 서버" 제작
- 2026-09-21: Docker로 서버를 이미지로 포장하고 컨테이너로 실행
- 2026-09-24: AWS EC2(Ubuntu)에 Docker Engine 설치 후 배포 → 인터넷 공개
