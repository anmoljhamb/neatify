import argparse
import os

from utils import get_extension, get_file_type, list_files, valid_folder


def organize_folder(folder_path: str):
    print(f"Using folder: {folder_path}")
    files = list_files(folder_path)

    unknowns = []
    track = {}

    for file in files:
        file_name = os.path.basename(file)
        ext = get_extension(file_name)
        file_type = get_file_type(ext)

        if not file_type:
            unknowns.append(file)
            continue

        if file_type not in track:
            track[file_type] = 1
        else:
            track[file_type] += 1

        organised_folder_path = os.path.join(
            folder_path,
            f"{file_type}s",
        )
        os.makedirs(
            organised_folder_path,
            exist_ok=True,
        )

        new_file_name = os.path.join(
            organised_folder_path,
            file_name,
        )

        os.rename(
            file,
            new_file_name,
        )

    total_files_moved = 0
    for x in track.values():
        total_files_moved += x

    print(f"A total of {total_files_moved} were moved.")
    if total_files_moved > 0:
        print(f"Summary: ")
        for file_type in track:
            print(f"There were {track[file_type]} {file_type}(s)")
    if len(unknowns) > 0:
        print(f"There were {len(unknowns)} unknowns.")


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
