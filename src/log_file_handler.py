import time


def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()


def monitor_file(filename):
    last_read_position = 0

    while True:
        with open(filename, 'r') as file:
            file.seek(last_read_position)
            new_lines = file.readlines()
            last_read_position = file.tell()

            if new_lines:
                for line in new_lines:
                    yield line.strip()

        time.sleep(1)


if __name__ == "__main__":
    filename = 'seu_arquivo.txt'
    monitor_file(filename)
