import os

def count_files_and_folders(directory):
    """
    Count the number of files and folders inside the given directory recursively.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        tuple: (number_of_files, number_of_folders)
    """
        num_files = 0
    num_dirs = 0

    for root, dirs, files in os.walk(directory):
        num_dirs += len(dirs)
        num_files += len(files)

    return num_files, num_dirs

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Count files and folders in a directory")
    parser.add_argument('--dir', required=True, help='Directory path to scan')

    args = parser.parse_args()

    files, folders = count_files_and_folders(args.dir)
    print(f"Total files: {files}")
    print(f"Total folders: {folders}")
