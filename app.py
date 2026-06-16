import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = os.environ.get('RESPONSE', 'variable not set')
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.encode())

HTTPServer(('', 8080), Handler).serve_forever()
