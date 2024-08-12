1. Flask 설치 및 환경 설정

`pip install flask`

2. 폴더 세팅

`mkdir hello_flask`
`touch app.py`

3. app.py


4. Flask 기본 구조 설명

	•	Flask: Flask 클래스는 현재 모듈(__name__)을 인자로 받아 Flask 애플리케이션 객체를 생성합니다.
	•	@app.route("/"): 데코레이터를 사용하여 특정 URL 경로와 함수를 연결합니다. 여기서는 홈 경로(”/”)에 home 함수를 연결했습니다.
	•	def home(): 이 함수는 해당 경로로 요청이 들어왔을 때 실행됩니다. 간단한 “Hello, World!” 문자열을 반환합니다.
	•	if __name__ == "__main__":: 이 조건문은 해당 스크립트가 직접 실행될 때만 app.run()을 호출하여 웹 서버를 실행합니다.
	•	app.run(debug=True): 애플리케이션을 디버그 모드로 실행하여 코드 변경 시 자동으로 재시작하고, 오류 메시지를 자세히 볼 수 있습니다.

5. run server

`python app.py`

`127.0.0.1:5000`
`127.0.0.1:5000/about`

