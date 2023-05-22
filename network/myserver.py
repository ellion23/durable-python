#!/usr/bin/python3
import socketserver
from hashlib import sha256
from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import json


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>This is Python server for TUSUR case.</h1></body></html>")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        # post_data = ''
        # for i in self.rfile.readlines():
        #     post_data += i.decode()
        post_data = {}
        for i in self.rfile.read(content_length).decode().split(sep='&'):
            i = i.split(sep='=')
            post_data[i[0]] = i[1]

        response = process_data(post_data)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        # Response content
        self.wfile.write(response.encode())


class MyServer(socketserver.ThreadingMixIn, HTTPServer):
    pass


def process_data(post_data):
    code = post_data['code']
    match code:
        case 'register':
            return register_user(post_data['username'], post_data['password'])
        case 'login':
            return 'void'
        case _:
            return "That code doesn't exist."


# Function to create database and tables if they don't exist
def create_tables():
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            balance
        )
    """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                note TEXT,
                cost INTEGER
            )
        """)

    conn.commit()
    conn.close()


# Function to register a new user
def register_user(username, password):
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    # Hash the password with SHA-256
    hashed_password = sha256(password.encode()).hexdigest()

    # Insert user into database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))

    conn.commit()
    conn.close()
    return 'Sing up success'


# Function to authenticate a user
def authenticate_user(username, password):
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    # Hash the password with SHA-256
    hashed_password = sha256(password.encode()).hexdigest()

    # Check if user exists in database
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = cursor.fetchone()

    conn.close()

    # If user exists, return True, else return False
    if user:
        # calculate count of notes and return it to get then all of them
        return True
    else:
        return False


if __name__ == "__main__":
    PORT = 8000
    create_tables()
    server = MyServer(("", PORT), MyHTTPRequestHandler)
    print(f"Server listening on port {PORT}...")
    server.serve_forever()
