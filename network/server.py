import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>GET request received</h1></body></html>")


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'POST request received: ' + post_data)


class MyServer(socketserver.ThreadingMixIn, HTTPServer):
    pass


if __name__ == "__main__":
    PORT = 8000
    server = MyServer(("", PORT), MyHTTPRequestHandler)
    print(f"Server listening on port {PORT}...")
    server.serve_forever()
