from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import json
import tornado.ioloop
import tornado.web
import pyautogui

def printAndWebWrite(rh:tornado.web.RequestHandler, something: any):
    print(something)
    rh.write(something)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            x = self.get_argument("x")
            y = self.get_argument("y")
            jsonstr = json.dumps({"x":x,"y":y})
            pyautogui.click(int(x), int(y))
            printAndWebWrite(self, jsonstr)
        except:
            printAndWebWrite(self, "need x and y")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

class Webserver:

    def __init__(self):
        pass

    def start(self):
        ip = "127.0.0.1"
        port = "6727"
        app = make_app()
        app.listen(port)
        print(f"web server start at {ip}:{port}")
        tornado.ioloop.IOLoop.current().start()