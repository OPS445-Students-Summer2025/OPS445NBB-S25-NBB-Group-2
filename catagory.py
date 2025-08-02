import os

def get_file_type_breakdown(path):
    ext_count = {}
    for root, dirs, files in os.walk(path):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            ext_count[ext] = ext_count.get(ext, 0) + 1
        return ext_count