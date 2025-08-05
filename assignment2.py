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
