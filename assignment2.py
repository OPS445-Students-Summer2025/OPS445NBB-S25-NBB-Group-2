def get_total_size(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size

def get_top_n_files(path, n):
    all_files = []
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            try:
                size = os.path.getsize(fp)
                all_files.append((fp, size))
            except:
                continue
    all_files.sort(key=lambda x: x[1], reverse=True)
    return all_files[:n]