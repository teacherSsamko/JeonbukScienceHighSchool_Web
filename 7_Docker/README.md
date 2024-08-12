# Docker로 서버 실행하기

1. `docker run --name python312 python:3.12`

2. `docker run --name python312 -it python:3.12 python`
    
    1) `print("hello, world")`
    2) `from flask import Flask`

3. `docker run --name python312 -it --rm python:3.12 python`

4. Dockerfile1 작성

5. `docker build -t flask .`

6. `docker run --name flask --rm -it flask python`

    ```
    >>> from flask import Flask
    >>> app = Flask(__name__)
    >>> @app.route('/')
    >>> def hello():
    >>> return "hello"
    >>> app.run()
    ```

7. `docker run --name flask --rm -it -p 5001:5000 flask python`

    ```
    >>> from flask import Flask
    >>> app = Flask(__name__)
    >>> @app.route('/')
    >>> def hello():
    >>> return "hello"
    >>> app.run(host="0.0.0.0")
    ```

8. Dockerfile 2 작성
