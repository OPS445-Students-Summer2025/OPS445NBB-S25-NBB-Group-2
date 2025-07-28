#!/usr/bin/env python3
# Author: Ricky Tang
# ID: rtang41
# Student No. : 104448246
"""
script for argument parsing command for directory analyzer tool
"""

import argparse

# messing around with argparse to start/practice
# script to echo the argument parsed
# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()
# print(args.echo)

def parse_args():
    parser = argparse.ArgumentParser(description = "Directory analyzer tool")
    parser.add_argument(
        "directory", type = str,
        help = "path to directory to analyze")
    parser.add_argument(
        "--top", "-t", type = int, default = 0,
        help = "Show top N largest files")
    parser.add_argument(
        "--sort", "-s", type = str,
        help = "sort by <size>, <name>, or <filetype>"
    parser.add_argument(
        "--output", "-o", type = str,
        help = "path to output file"
    )