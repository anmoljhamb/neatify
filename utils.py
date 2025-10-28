import argparse
import os
from typing import Optional

from constants import EXTENSIONS


def valid_folder(path: str):
    """Validate that the given path is an existing directory."""
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"'{path}' is not a valid directory path.")
    return os.path.abspath(path)


def list_files(folder_path: str):
    files = os.listdir(folder_path)
    temp = []
    for f in files:
        file_path = os.path.join(folder_path, f)
        if os.path.isfile(file_path):
            temp.append(file_path)
    return temp


def get_extension(file_name: str):
    ext = file_name.split(".")[-1]
    return ext.lower()


def get_file_type(ext: str) -> Optional[str]:
    for file_type in EXTENSIONS:
        if ext in EXTENSIONS[file_type]:
            return file_type
    return None
