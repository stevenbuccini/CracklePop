###############
## Fizz Buzz ##
###############


def fizz_buzz():
	for num in range(1, 101):
		if num %  15 == 0:
			print("FizzBuzz") #catch this case first, since things divisible by 3 and 5 won't make it to the 15 case if it's at the bottom
		elif num % 3 == 0:
			print("Fizz")
		elif num % 5 == 0:
			print("Buzz")
		else:
			print(str(num))