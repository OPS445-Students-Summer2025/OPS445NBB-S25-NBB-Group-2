#!/usr/bin/env python3
# Author: Ricky Tang
# ID: rtang41
# Student No. : 104448246

import argparse

def parse_args():
    """
    Function for parsing input arguments for analyzer tool
    """
    parser = argparse.ArgumentParser(description = "Directory analyzer tool")
    #dir path argument
    parser.add_argument(
        "directory", type = str,
        help = "path to directory to analyze")
    #largest files argument
    parser.add_argument(
        "--top", "-t", type = int, default = 0,
        help = "Show top N largest files")
    #filetype sort argument
    parser.add_argument(
        "--sort", "-s", type = str, default = "name",
        help = "sort by <size>, <name>, or <filetype>"
    )
    #write output file argument
    parser.add_argument(
        "--output", "-o", type = str,
        help = "path to output file"
    )

    return parser.parse_args()