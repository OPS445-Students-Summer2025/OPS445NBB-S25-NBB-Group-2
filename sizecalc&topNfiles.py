#!/usr/bin/env python3

def get_file_size_human_readable(size_bytes: int) -> str:
    """
    Converts a file size from bytes to a human-readable format (B, KB, MB, GB).
    """
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024**2:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024**3:
        return f"{size_bytes / (1024**2):.2f} MB"
    else:
        return f"{size_bytes / (1024**3):.2f} GB"

def get_top_n_files_by_size(file_info_list: list, n: int) -> list:
    """
    Sorts the list of file information by size in descending order
    and returns the top N files.
    
    Args:
        file_info_list (list): A list of dictionaries with 'path' and 'size_bytes' keys.
        n (int): The number of top files to return.

    Returns:
        list: A sorted list of the top N largest files.
    """
    if not file_info_list:
        return []
    sorted_files = sorted(file_info_list, key=lambda x: x['size_bytes'], reverse=True)
    return sorted_files[:n]
