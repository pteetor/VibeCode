#!/usr/bin/python3

import http.server
import socketserver
import os

# --- Configuration ---
# Set the port number you want the server to listen on.
PORT = 8000
# Define the handler. SimpleHTTPRequestHandler serves files from the current directory.
Handler = http.server.SimpleHTTPRequestHandler

# --- Server Setup ---
try:
    # Use socketserver.TCPServer to create a server instance.
    # The server will listen on all interfaces (empty string) on the specified port.
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("-" * 50)
        print(f"Serving files from directory: {os.getcwd()}")
        print(f"Access the server at: http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server.")
        print("-" * 50)

        # Start the server and serve requests indefinitely.
        httpd.serve_forever()

except KeyboardInterrupt:
    print("\nServer stopped successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

# --- Instructions for the User ---
# 1. Save this script as 'server.py'.
# 2. Make sure you have some HTML files (e.g., 'index.html') in the same directory.
# 3. Run it from your terminal: python server.py
# 4. Open your web browser and go to http://localhost:8000
# 5. The server will automatically look for an 'index.html' file first.
