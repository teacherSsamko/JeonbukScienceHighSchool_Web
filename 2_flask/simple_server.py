from http.server import SimpleHTTPRequestHandler, HTTPServer

# 서버 설정
HOST = "localhost"
PORT = 8000


# 요청 핸들러 클래스 정의
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")
        elif self.path == "/about":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"<html><body><h1>About Page</h1><p>This is the about page.</p></body></html>"
            )
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><body><h1>404 Not Found</h1></body></html>")


# 서버 초기화 및 실행
def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {HOST}:{PORT}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
