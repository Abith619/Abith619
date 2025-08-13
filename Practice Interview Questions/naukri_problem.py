from os import *

from sys import *
from collections import *
from math import *

def goodSubarrays(arr, n, b):
	def goodSubarrays(K):
		if K == 0:
			return 0
		count = 0
		left = 0
		freq = defaultdict(int)

		for right in range(n):
			freq[arr[right]] += 1
			while len(freq) > K:
				freq[arr[left]] -= 1
				if freq[arr[left]] == 0:
					del freq[arr[left]]
				left += 1
			count += (right - left + 1)
		return count
	return goodSubarrays(b) - goodSubarrays(b - 1)


#

from sys import stdin


def getMaximumProfit(values, n) :
    profit = 0
    for i in range(1, n):
        if values[i] > values[i - 1]:
            profit += values[i] - values[i-1]
    return profit

#

def numFollowingPattern(s):
    n = len(s)
    result = []
    stack = []

    # We need to use digits from 1 to n+1 (or n+1 digits)
    for i in range(1, n + 2):
        stack.append(i)  # push the current number to the stack
        # If we are at the end of the string or the current character is 'I'
        if i == n + 1 or s[i - 1] == 'I':
            # Pop all elements from the stack to form the resulting number
            while stack:
                result.append(str(stack.pop()))

    # Join the result list to form the final number string
    return ''.join(result)

i = 0
while i < 5:
    if i == 2:
        i += 1
        continue
    else:
        print(i,end = " ")
        i += 1



i = 0
while(i < 5):
    i += 1
    print(i,end = " ")