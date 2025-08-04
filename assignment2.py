# === Mark Jordan's Section: File/Folder Counter ===
def count_files_and_dirs(path):
    file_count = 0
    dir_count = 0
    for root, dirs, files in os.walk(path):
        file_count += len(files)
        dir_count += len(dirs)
    return file_count, dir_count
