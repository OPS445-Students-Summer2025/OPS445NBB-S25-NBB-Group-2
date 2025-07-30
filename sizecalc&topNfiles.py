#!/usr/bin/env python3

import sys  # Used for parsing command line arguments and exiting the script
import os   # Used for interacting with the operating system, specifically for file and directory operations

#def usage():
    """
    Prints a helpful usage message to the user and then exits the script.
    """
    print(f"Usage: {sys.argv} <directory_path> <N>")
    print("  <directory_path>: The path to the directory to scan.")
    print("  <N>: The number of top largest files to display.")
    sys.exit(1)

def human_readable_size(size_bytes: int) -> str:
    """
    Converts a file size in bytes to a human-readable format (e.g., KB, MB, GB).
    """
    if size_bytes < 0:
        return "Invalid Size"

    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    threshold = 1024

    for i, unit in enumerate(units):
        if size_bytes < threshold**(i + 1):
            return f"{size_bytes / (threshold**i):.2f} {unit}"
    
    return f"{size_bytes / (threshold**(len(units)-1)):.2f} {units[-1]}"

#def scan_directory(directory_path: str) -> list:
    """
    Scans the specified directory and collects information about files.
    Returns a list of tuples: (file_size_in_bytes, file_name).
    """
    files_info = []
    try:
        if not os.path.isdir(directory_path):
            print(f"Error: Directory '{directory_path}' does not exist or is not a directory.")
            return []

        for item_name in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item_name)
            
            if os.path.isfile(item_path):
                try:
                    size = os.path.getsize(item_path)
                    files_info.append((size, item_name))
                except OSError as e:
                    print(f"Warning: Could not get size for '{item_path}': {e}")
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access directory '{directory_path}'.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred during directory scan: {e}")
        return []
    return files_info

def sort_and_get_top_n(files_data: list, n: int) -> list:
    """
    Sorts a list of (size, name) tuples by file size in descending order
    and returns the top N largest files.
    """
    if not isinstance(files_data, list):
        print("Error: Invalid data format for sorting. Expected a list.")
        return []
    
    files_data.sort(key=lambda x: x, reverse=True)
    return files_data[:n]

#if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    directory_path = sys.argv[1]
    
    try:
        n_files_to_display = int(sys.argv[2])
        if n_files_to_display < 1:
            print("Error: N must be a positive integer.")
            usage()
    except ValueError:
        print(f"Error: Invalid number '{sys.argv[2]}' for N. N must be an integer.")
        usage()

    all_files_data = scan_directory(directory_path)

    if not all_files_data:
        sys.exit(1)

    top_n_largest_files = sort_and_get_top_n(all_files_data, n_files_to_display)

    print(f"\nTop {n_files_to_display} largest files in '{directory_path}':")
    if not top_n_largest_files:
        print("No files found or specified N is too high.")
    else:
        for size_bytes, file_name in top_n_largest_files:
            readable_size = human_readable_size(size_bytes)
            print(f"- {file_name}: {readable_size}")