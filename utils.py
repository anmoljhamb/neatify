import argparse
import os


def valid_folder(path: str):
    """Validate that the given path is an existing directory."""
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"'{path}' is not a valid directory path.")
    return os.path.abspath(path)
