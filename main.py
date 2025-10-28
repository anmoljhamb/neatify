import argparse

from utils import valid_folder


def organize_folder(folder_path: str):
    print(f"Using folder: {folder_path}")


def main():
    parser = argparse.ArgumentParser(description="Process a folder path.")
    parser.add_argument(
        "folder",
        type=valid_folder,
        help="Path to the target folder.",
    )

    args = parser.parse_args()

    organize_folder(
        folder_path=args.folder,
    )


if __name__ == "__main__":
    main()
