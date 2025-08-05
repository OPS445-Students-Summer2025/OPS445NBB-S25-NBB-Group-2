import os
import argparse

parser = argparse.ArgumentParser(
    description = "Directory size report tool"
)

#dir path argument
parser.add_argument(
    "--dir",
    required = True,
    help = "Directory path to scan"
)

#largest files argument
parser.add_argument(
    "--top", "-t",
    type = int,
    help = "Show top N largest files"
)

#filetype sort argument
parser.add_argument(
    "--sort", "-s",
    choices = ["size","name","type"],
    help = "sort by <size>|<name>|<type>"
)

#write output file argument
parser.add_argument(
    "--output", "-o",
    help = "path to output file (optional)"
)

args = parser.parse_args()

#Kris
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
