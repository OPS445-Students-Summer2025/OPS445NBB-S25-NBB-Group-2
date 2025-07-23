#!/usr/bin/env python3
# Author: Ricky Tang
# ID: rtang41
# Student No. : 104448246

import argparse

# messing around with argparse to start/practice
# script to echo the argument parsed
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
