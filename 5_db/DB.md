2. 데이터베이스 개념 소개

	•	RDBMS: 관계형 데이터베이스 관리 시스템, 테이블 형식으로 데이터를 저장합니다.
	•	SQL: Structured Query Language, 데이터베이스에서 데이터를 생성, 읽기, 업데이트, 삭제하는 데 사용하는 언어입니다.

3. SQLite 설치 및 기본 사용법

SQLite는 파이썬에 기본 내장되어 있어 별도의 설치가 필요 없습니다. sqlite3 모듈을 사용하여 데이터베이스에 접근할 수 있습니다.

1. `CREATE TABLE feedbacks (id INTEGER PRIMARY KEY AUTOINCREMENT, author TEXT, message TEXT)`

1. `SELECT * FROM feedbacks`

1. `INSERT INTO feedbacks (author, message) VALUES ('이은섭', '좋아요');`

1. `SELECT * FROM feedbacks`

1. `UPDATE feedbacks SET message='재밌어요' WHERE id=1`

1. `DELETE FROM feedbacks WHERE id=1`
