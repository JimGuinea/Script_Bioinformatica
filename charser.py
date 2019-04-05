#! /usr/bin/python3

# Python program to check if a line in a text file
# contains any special character and which one is that special
# character

# import required package
import re # regular expression
import argparse

parser = argparse.ArgumentParser(description='This program prints every non chars found in a row of a text file')

parser.add_argument('-i', '--input',help = 'input file', metavar='')

args = parser.parse_args()

input_file = args.input
rr=set()
if __name__ == '__main__':
	with open(input_file,'r') as inp:
		for row in inp:
			r=re.findall(r'[^.a-zA-Z0-9\n]',row)
			for elem in r:
				rr.add(elem)
	print(" ".join(str(e) for e in rr))
