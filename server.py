#!/usr/bin/env python3
"""Simple HTTP server for serving the CCSE quiz page locally."""

import http.server
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Clean, minimal logging
        try:
            print(f"[{self.log_date_time_string()}] {format % args}")
        except Exception:
            super().log_message(format, *args)

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    server = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"\n  CCSE Quiz Server running at:")
    print(f"  -> http://localhost:{PORT}/index.html")
    print(f"  -> http://localhost:{PORT}/allqs.json")
    print(f"\n  Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Shutting down...")
        server.server_close()