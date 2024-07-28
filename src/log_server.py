import socketserver
import pickle
import struct


LOG_FILE = "log_service.txt"

class LoggingStreamHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            log_file = open(LOG_FILE, "a")
            chunk = self.connection.recv(4)
            if len(chunk) < 4:
                break
            slen = struct.unpack('>L', chunk)[0]
            chunk = self.connection.recv(slen)
            while len(chunk) < slen:
                chunk = chunk + self.connection.recv(slen - len(chunk))
            record = pickle.loads(chunk)
            print(record)
            try:
                log_file.write(f"{record['message']}\n")
            except Exception:
                log_file.write("Failed to write mesage")

def start_server(host='localhost', port=9999):
    server = socketserver.TCPServer((host, port), LoggingStreamHandler)
    print(f"Servidor de log iniciado em {host}:{port}")
    server.serve_forever()
