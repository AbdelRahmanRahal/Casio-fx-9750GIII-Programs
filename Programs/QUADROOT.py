from math import sqrt, pi, sin, cos, tan, sinh, cosh, tanh

π = pi

def decimal_point_amount(n):
	return len(str(n).split('.')[-1])

print("\n~~Quadratic Solver~~")
print("Enter your terms in")
print("quadratic form:")
print("aX^2 + bX + c = 0\n")

# Get inputs for coefficients a, b, and c
a = eval(input("a = "))
b = eval(input("b = "))
c = eval(input("c = "))

# Calculate the discriminant
d = b**2 - 4*a*c

# Calculate the two solutions
if d > 0:
	# If the discriminant is positive, the solutions are real and different
	sol1 = (-b - sqrt(d)) / (2*a)
	sol2 = (-b + sqrt(d)) / (2*a)
	if decimal_point_amount(sol1) > 5:
		print(
			'\nX = ({} +/- {}) / {}'.format(
				-b,
				"sqrt({})".format(d) if decimal_point_amount(sqrt(d)) > 5 else sqrt(d),
				2*a
			)
		)
		print('\nOR')
	
	print('\nX = {}\nX = {}'.format(sol1, sol2))
elif d == 0:
	# If the discriminant is zero, the solutions are real and the same
	sol = -b / (2*a)
	print('\nX = {}  x2'.format(sol))
else:
	# If the discriminant is negative, the solutions are imaginary
	sol = (-b / (2*a), -d / (4*a))
	print('\nX = {} +/- sqrt({})i'.format(sol[0], sol[1]))
	print('\nOR')
	print('\nX = {} +/- {}i'.format(sol[0], sqrt(sol[1])))