#pylint: disable=wrong-import-order, import-error
import threading
from log_server import start_server
from concurrent.futures import ThreadPoolExecutor

class Server:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.executor = ThreadPoolExecutor(max_workers=2)


if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server(), daemon=True)
    server_thread.start()
