from custom_types import Idk
from os import stat

MAX_FILE_SIZE = 1024 * 1024 * 1024 # 1mb

def get_graph_string(filename: str) -> str:
    err_msg = "The provided file is too big"
    assert stat(filename).st_size < MAX_FILE_SIZE, err_msg

    with open(filename, "r") as file:
        return file.read()
