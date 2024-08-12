2. RESTful API 개념 소개

	•	HTTP 메소드: GET, POST, PUT, DELETE 등 각 메소드는 CRUD 작업과 대응됩니다.
	•	GET: 리소스 조회
	•	POST: 리소스 생성
	•	PUT: 리소스 업데이트
	•	DELETE: 리소스 삭제
	•	엔드포인트 설계: 각 리소스는 고유의 URL로 접근할 수 있습니다. 예를 들어, /books는 도서 목록을 나타냅니다.

3. Flask로 RESTful API 만들기

Flask와 Flask-RESTful을 사용하여 간단한 도서 관리 API를 구축합니다.

4. JSON 데이터 처리

API는 주로 JSON 형식으로 데이터를 주고받습니다. Flask에서 flask.jsonify를 사용하여 JSON 응답을 쉽게 생성할 수 있습니다.


4.	간단한 API 예제 구현
	•	GET /books: 모든 도서 목록을 조회합니다.
	•	GET /books/int:book_id: 특정 ID의 도서를 조회합니다.
	•	POST /books: 새로운 도서를 추가합니다.
	•	PUT /books/int:book_id: 특정 ID의 도서를 업데이트합니다.
	•	DELETE /books/int:book_id: 특정 ID의 도서를 삭제합니다.