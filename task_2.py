from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080
file_content = "index.html"


class MyServer(BaseHTTPRequestHandler):
    @staticmethod
    def get_content(file_cont):
        with open(file_cont, encoding="utf-8") as f:
            page_content = f.read()
        return page_content


    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)

        page_content = self.get_content(file_content)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
