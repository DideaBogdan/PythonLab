import math
def is_prime(numar):
	if numar < 2:
		return False
	if numar == 2:
		return True
	if numar % 2 == 0:
		return False
	max = int(math.sqrt(numar))
	#max = numar ** 0.5 +1 #sqrt
	#i = 3
	#while i < max:
	#	if numar % i == 0:
	#		return False
	#	i = i + 2

	for it in range(3, max + 1, 2):
		if numar % it == 0:
			return False
	return True

n = int(input("Numarul: "))
print(is_prime(n))


def is_triangle(number1, number2, number3):
	if number1 > number2:
		if number1>number3:
			if number2+number3 >= number1: #1 e cea mai mare
				return True
			return False
		else:
			if number2+number1 >= number3: #3 e cea mai mare
				return True
			return False
	elif number2 > number3:
		if number1+number3 >= number2: #2 e cea mai mare
			return True
		return False
	elif number1+number2 >= number3:
		return True
	return False
#print(is_triangle(2,4,8))