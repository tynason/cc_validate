Solution to a challenge for a comcast position, to solve this:

https://www.hackerrank.com/challenges/validating-credit-card-number/problem 

For the credit card validation, the pseudocode I used is:

	assume it's valid
	test if it starts with a 4,5, or 6
	   if not, it's invalid
	test if there are any non-integers (including space) other than dashes
	   if so, it's invalid
	if it contains dashes, determine if there are any sequences of integers with count other than 4
		if so it's invalid
	take out the dashes
		test if there are 16 characters
		if not, it's invalid
	test if any 4 repeats of same integer
		if so, it's invalid
	if none of the invalid conditions applies, it remains valid, so return that value

I included extra commentary on the Invalid status but it will return Invalid on the first condition that fails.