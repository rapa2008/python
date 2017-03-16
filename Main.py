import Palindrome
import prime

n=input('What do you want to do?\n 1. Check for palindrome \n 2. Print prime numbers\n')
print(n)

if int(n) == 1:
	Palindrome.palindrome()
else:
	prime.printprime()
