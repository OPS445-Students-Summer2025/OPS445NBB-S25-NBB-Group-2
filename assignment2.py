#!/usr/bin/env python3

def human_readable_size(size_bytes):
    # Convert bytes to a human-readable format
    for unit in ['B','KB','MB','GB','TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"

# ---------------- Main Block ---------------- #
if __name__ == '__main__':
    # Sample data for testing
    sample_path = "/home/student/testdir"
    sample_file_count = 8
    sample_dir_count = 2
    sample_total_size = 3145728  # 3 MB
    sample_top_files = [
        ("/home/student/testdir/file1.txt", 2048000),
        ("/home/student/testdir/file2.jpg", 512000),
        ("/home/student/testdir/big.iso", 1024000)
    ]
    sample_type_breakdown = {
        ".txt": 2,
        ".jpg": 3,
        ".iso": 1
    }

    