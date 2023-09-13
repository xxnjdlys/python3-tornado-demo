import tornado
from tornado import httpserver
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

from config import CONFIG
from common import commonService as CS
from service import demoService

logger = CS.get_logger(1)


class ApiGroupHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("API GROUP")


def handle_request(func):
    def wrapper(self):
        try:
            req = CS.get_post_data(self)
            msg = CS.ResultMap(func(self, req))
        except Exception as e:
            msg = CS.ResultMap(str(e), 500)
            logger.exception(e)
        self.write(msg)

    return wrapper


class GetAllUser(RequestHandler):
    @handle_request
    def get(self, req):
        return demoService.get_all_user()


class GetUserById(RequestHandler):
    @handle_request
    def get(self, req):
        return demoService.get_user_by_id(req['uid'])


def make_app():
    app = tornado.web.Application([
        (r"/api", ApiGroupHandler),
        (r"/api/", ApiGroupHandler),
        (r"/api/getAllUser", GetAllUser),  # 将 /api/getAllUser 映射到 GetAllUser 处理函数
        (r"/api/getUserById", GetUserById),  # 可以添加其他路由
    ])
    return app


if __name__ == "__main__":
    app = make_app()

    # 中间件，重写请求路径
    # class ApiMiddleware(tornado.web.RequestHandler):
    #     def prepare(self):
    #         # 重写请求路径，将 /api/ 后的路径提取并设置为请求路径
    #         self.request.path = '/' + '/'.join(self.request.uri.split('/')[2:])
    # app.add_handlers(r".*", [("/api/.*", ApiMiddleware)])

    server = CONFIG['server']

    # 启动端口
    port = server['port']

    # 单线程启动
    app.listen(port)
    IOLoop.current().start()

    # 多线程启动（必须Linux系统下启动）
    # 线程数
    # thread = server['thread']
    # http_server = httpserver.HTTPServer(app)
    # http_server.bind(port)
    # http_server.start(thread)
    # IOLoop.instance().start()
