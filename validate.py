# putative solution to modified Luhn solution to credit card validation
# https://www.hackerrank.com/challenges/validating-credit-card-number/problem
# tnason 2019

import re
import sys
from itertools import groupby

def geterrors(line):

	error="Valid"  # assume it's valid
	initialdigits=[4,5,6] # set the list of valid initial digits

	# invalid 1st digit
	if int(line[0]) not in initialdigits:
		#print(line[0])
		error="Invalid: bad 1st digit"
		return line, error

	# non-dash non-numerics
	for item in line:
		#print(item, '\t', item.isnumeric())
		if not item.isnumeric() and item !='-':
			error="Invalid: non-dash non-numeric"
			#print(item, '\t', error)
			return line, error

	# there are dashes but no spaces and we know the first digit is a number
	# so determine if there are any sequences of integers with count other than 4
	if '-' in line:
		splitt=line.split('-')
		#print(splitt)
		for itemm in splitt:
			if len(itemm) !=4:
				error='Invalid: grouping other than 4'
				return line, error
			else:
				line=re.sub('-','',line)

	if len(line) !=16:
			error='Invalid: not 16 digits'
			return line, error

	# test if any 4 repeats of same integer

	groups = groupby(line)
	resultt = [(label, sum(1 for _ in group)) for label, group in groups]
	#print(resultt)
	for el in resultt:
		if el[1]>3:
			error='Invalid: 4 consecutive identical digits'
			return line, error

	# if it failed none of the tests it will still be Valid so return that
	return line, error

def main():
	# validate the constraint 0<n<100 is satisfied
	totallines=0
	with open("valmin.txt") as f:
		for line in f:
			#print(line.strip('\n'))
			totallines+=1

	#print(totallines)
	if totallines==0 or totallines>99:
		print("number of lines constraint is violated: ", totallines, " lines")
		sys.exit()

	with open("valmin.txt") as f:
		for line in f:
			if len(line.strip('\n'))>0: # strip the newline char and pass to function
				result=geterrors(line.strip('\n'))
				print(result)

main()