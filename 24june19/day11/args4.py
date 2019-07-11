#positional args
import sys
import argparse

print('command line args')

parser = argparse.ArgumentParser()
parser.add_argument('company')
parser.add_argument('place')
args = parser.parse_args()

print(args.company)
