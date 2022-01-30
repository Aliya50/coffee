import http.server
import socketserver

PORT = 7000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
   print("server is running here", PORT)
   print("To test from dockerrization ,run http://localhost:port ")
   httpd.serve_forever()
