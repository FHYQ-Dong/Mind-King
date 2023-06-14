from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time

host = ('127.0.0.1', 16677)


class Resquest(BaseHTTPRequestHandler):

    def checkClient(self):
        UA = self.headers.get('User-Agent')
        res = bool(UA == 'MindKingClient')
        if not res: self.send_error(403, 'FORBIDDEN')
        return res

    def do_GET(self):
        print(self.path)
        if not self.checkClient():
            return
        
        if self.path == "/conn":
            self.send_conn()
        else:
            self.send_error(403, 'FORBIDDEN')

    def send_conn(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write('Success'.encode('utf-8'))

    def do_POST(self):
        datas = self.rfile.read(int(self.headers['content-length']))

        print('headers', self.headers)
        print("do post:", self.path, self.client_address, datas)


if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()