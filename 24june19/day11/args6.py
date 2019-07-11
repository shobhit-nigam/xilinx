#positional args
import sys
import argparse

print('command line args')

parser = argparse.ArgumentParser()
parser.add_argument('company')
parser.add_argument('place', nargs='?' , default='hyderabad', help='write your area of residence')
args = parser.parse_args()

print(args.company)
print(args.place)
