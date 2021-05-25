from custom_types import Idk
from os import stat

MAX_FILE_SIZE = 1024 * 1024 * 1024 # 1mb

def get_graph_file(filename: str) -> str:
    assert stat(filename).st_size < MAX_FILE_SIZE, "File is too big"

    with open(filename, "r") as file:
        return file.read()
