from http.server import SimpleHTTPRequestHandler, HTTPServer

class CTFHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/login":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            print("[+] Login attempt:", post_data.decode())

            # realistic response
            response = b"Login successful. Redirecting..."

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()

            self.wfile.write(response)

        else:
            self.send_error(404, "Not Found")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), CTFHandler)
    print("[+] Server running on port 8080")
    server.serve_forever()
