import logging
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application
from wsgi_app import app

class MainHandler(RequestHandler):
    def get(self):
        self.write("This message comes from Tornado ^_^")

tr = WSGIContainer(app)

application = Application([
    (r"/tornado", MainHandler),
    (r".*", FallbackHandler, dict(fallback=tr)),
    ])

if __name__ == "__main__":

    logging.getLogger().setLevel(logging.INFO)

    application.listen(5000)
    IOLoop.instance().start()