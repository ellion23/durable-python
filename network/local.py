#!/usr/bin/python3
from socketserver import ForkingTCPServer
from socketserver import ThreadingTCPServer
import socketserver
import types
from datetime import datetime
import json


class ConnectionHandler(socketserver.BaseRequestHandler):
    def handle(self):
        f = open('log.txt', "a")
        f.write(f"\nConnected by {self.client_address} at {datetime.now()}\n")
        while True:
            try:
                data = self.request.recv(1024)
            except ConnectionError:
                f.write(f"Client suddenly closed while receiving at {datetime.now()}\n")
                break
            if not data:
                break

            x = json.loads(data)

            f.write(f"Received: [{x}]\n")

            try:
                f.write("Sended data")
                self.request.sendall(b"Does it work?")
            except ConnectionError:
                f.write(f"Client suddenly closed, cannot send at {datetime.now()}\n")
                break
        f.write(f"Disconnected by {self.client_address} at {datetime.now()}\n")
        f.close()


if __name__ == "__main__":
    f = open('log.txt', "a")
    f.write(f"\nSTART SERVER at {datetime.now()}\n")
    f.close()
    HOST, PORT = "81.200.152.79", 5001
    with ThreadingTCPServer((HOST, PORT), ConnectionHandler) as server:
        server.serve_forever()
