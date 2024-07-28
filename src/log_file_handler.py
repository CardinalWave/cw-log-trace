import time


def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()


def filter_file(filename, log_param):
    last_read_position = 0
    while True:
        with open(filename, 'r') as file:
            file.seek(last_read_position)
            new_lines = file.readlines()
            last_read_position = file.tell()
            if new_lines:
                log_filter = [log for log in new_lines if log_param in log]
                for line in log_filter:
                    yield line.strip()

        time.sleep(1)


def count_status(filename) -> tuple[int, int]:
    last_read_position = 0
    error_count = 0
    non_error_count = 0

    while True:
        with open(filename, 'r') as file:
            file.seek(last_read_position)
            new_lines = file.readlines()
            last_read_position = file.tell()
            if new_lines:
                for line in new_lines:
                    if "error".lower() in line.lower():
                        error_count += 1
                    else:
                        non_error_count += 1
                    return error_count, non_error_count
        time.sleep(1)
