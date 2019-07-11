#positional args
import sys
import argparse

print('command line args')

parser = argparse.ArgumentParser()
parser.add_argument('lista', nargs=2, type=int)
args = parser.parse_args()

print(args.lista[0], args.lista[1])
print(type(args.lista))
print(type(args.lista[1]))

