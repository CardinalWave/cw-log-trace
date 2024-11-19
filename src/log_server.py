#pylint: disable=consider-using-with, unspecified-encoding, import-error

import socketserver
import pickle
import struct
from config.ports import Config

LOG_FILE = "log_service.txt"


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

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
            try:
                log_file.write(f"{record['message']}\n")
            except Exception:
                log_file.write("Failed to write mesage")


def start_server(host=Config.CW_LOG_TRACE_IP, port=int(Config.CW_LOG_TRACE_PORT)):
    server = ThreadedTCPServer((host, port), LoggingStreamHandler)
    print(f"Servidor de log iniciado em {host}:{port}")
    server.serve_forever()
