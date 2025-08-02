# File Type Categorization by Chanho Lee
def get_file_type_breakdown(path):
    ext_count = {} # count by extension + display as dict
    for root, dirs, files in os.walk(path): # Walk all directories starting from whichever path
        for f in files:
            ext = os.path.splitext(f)[1].lower() # get the extension and convert into lowercase
            ext_count[ext] = ext_count.get(ext, 0) + 1 # increase count for the same extension type in the dict
        return ext_count