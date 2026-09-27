from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # The HTML page that will display when someone visits your server
        html = """
        <html>
            <head><title>DevOps Web App</title></head>
            <body style="text-align: center; font-family: sans-serif; margin-top: 50px;">
                <h1>🚀 DevOps Portfolio Web App Live!</h1>
                <p>Managed via Terraform & Containerized with Docker.</p>
            </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf8"))

# Run the server on port 80
server = HTTPServer(("0.0.0.0", 80), MyHandler)
print("Server started on port 80...")
server.serve_forever()

