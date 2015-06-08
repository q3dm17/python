import os

__author__ = 'q3dm17'


import BaseHTTPServer
import SimpleHTTPServer
import shutil

class PingHttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        """Serve a GET request."""
        print self.path
        try:
            self.send_response(200)
            self.send_header("Content-Length", '5')
            self.end_headers()
            self.wfile.write(0+os.urandom(4))
        finally:
            self.wfile.close()


def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=PingHttpHandler):
    server_address = ('', 8001)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
run()