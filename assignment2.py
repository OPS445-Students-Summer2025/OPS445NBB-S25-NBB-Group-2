def get_total_size(path):
    return sum(
        os.path.getsize(os.path.join(root, f))
        for root, _, files in os.walk(path)
        for f in files
        if os.path.isfile(os.path.join(root, f))
    )

def get_top_n_files(path, n):
    files_with_size = []
    for root, _, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            try:
                files_with_size.append((fp, os.path.getsize(fp)))
            except (OSError, PermissionError):
                continue
    return sorted(files_with_size, key=lambda x: x[1], reverse=True)[:n]