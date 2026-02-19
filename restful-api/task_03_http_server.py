#!/usr/bin/python3
"""A simple HTTP server providing basic HTML and JSON endpoints."""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class BaseHTTP(BaseHTTPRequestHandler):
    """Handles GET requests for predefined API endpoints."""

    def do_GET(self):
        """Respond to GET requests with HTML or JSON depending on path."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            text = "Hello, this is a simple API!"

            self.wfile.write(text.encode("utf-8"))
            return

        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(data).encode("utf-8")

            self.wfile.write(response)
            return

        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        if self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            response = json.dumps(data).encode("utf-8")

            self.wfile.write(response)
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"Endpoint not found")


def main():
    """Start the HTTP server on localhost:8000."""
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, BaseHTTP)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
