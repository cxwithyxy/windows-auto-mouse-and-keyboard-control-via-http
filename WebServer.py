from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import time

class SimpleHTTPServer(ThreadingHTTPServer):
    pass

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    server: SimpleHTTPServer
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("dasdasdasdasd","utf8"))
        # self.wfile.flush()
        # self.wfile.close().encode("utf8")

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, *argus):
        print(argus)
        pass

class Webserver:


    def __init__(self):
        pass

    def start(self):
        ip = "127.0.0.1"
        port = "6727"
        httpd = SimpleHTTPServer((ip, int(port)), SimpleHTTPRequestHandler)
        print(f"web server start at {ip}:{port}")
        httpd.serve_forever()