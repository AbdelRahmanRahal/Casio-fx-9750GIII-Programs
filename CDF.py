from math import sin, cos, tan, sinh, cosh, tanh

def is_balanced(expression):
	stack = []

	for char in expression:
		if char == '(':
			stack.append(char)
		elif char == ')':
			if not stack:
				return False
			stack.pop()

	return not stack


def is_legal(expression):
	illegal_characters = 'ABCDEFGHIJKLMNOPQRSTUVWYZbdefgjklmpqruvwxyz!#$^&\\,[]'
	for char in expression:
		if char in illegal_characters:
			return False
	
	return True


def tokenizer(expression):
	tokens = []
	operators = '+-*/'

	for char in expression:
		if char == '(' or char == ')':
			tokens.append(('paren', char))
		elif char == ' ':
			tokens.append(('space', char))
		elif char in operators:
			tokens.append(('op', char))
		elif char == '.':
			tokens.append(('dec', char))
		elif char.isdigit():
			tokens.append(('digit', char))
		elif char == 'X':
			tokens.append(('var', char))
		elif char.isalpha():
			tokens.append(('letter', char))
		else:
			tokens.append(('other', char))

	return tokens


def parse(tokens):
	expression = ''

	for i in range(len(tokens)):
		token, char = tokens[i]
		p_token, p_char = tokens[i - 1] if i > 0 else (None, None)
		n_token, n_char = tokens[i + 1] if i < len(tokens) - 1 else (None, None)

		if token == 'paren':
			if char == '(' and (p_token == 'digit' or p_token == 'var' or p_char == ')'):
				expression += '*' + char
			else:
				expression += char
		
		elif token == 'space' or token == 'op' or token == 'dec':
			expression += char
		
		elif token == 'digit':
			if n_token == 'letter':
				expression += char + '*'
			else:
				expression += char
		
		elif token == 'var':
			if p_token == 'digit':
				expression += '*' + char
			else:
				expression += char
			
			if n_token == 'letter':
				expression += '*'
		
		elif token == 'letter':
			if char == 's':
				if n_char == 'i':
					expression += char
				elif p_char == 'o':
					expression += char
				else:
					raise ValueError('Invalid/Unknown function.')
			elif char == 'i':
				if p_char == 's' and n_char == 'n':
					expression += char
				else:
					raise ValueError('Invalid/Unknown function.')
			elif char == 'n':
				if p_char == 'i' or p_char == 'o' or p_char == 'a':
					expression += char
				else:
					raise ValueError('Invalid/Unknown function.')
				
				if n_char != 'h' and n_char != '(':
					raise ValueError('Add parentheses after trig or hyperbolic functions.')

			elif char == 'h':
				if n_char != '(':
					raise ValueError('Add parentheses after trig or hyperbolic functions.')
				elif p_char == 'n' or p_char == 's':
					expression += char
				else:
					raise ValueError('Invalid/Unknown function.')
				
			elif char == 'c':
				if p_token == 'letter':
					raise ValueError('Invalid/Unknown function.')
				elif n_char == 'o':
					expression += char
				else:
					raise ValueError('Invalid/Unknown function.')
			
			elif char == 'o':
				if p_char == 'c' and n_char == 's':
					expression += char
				else:
					raise ValueError('Invalid/Unknown function.')
			
			elif char == 't':
				if p_token == 'letter':
					raise ValueError('Invalid/Unknown function.')
				elif n_char == 'a':
					expression += char
				else:
					raise ValueError('Invalid/Unknown function.')
			
			elif char == 'a':
				if p_char == 't' and n_char == 'n':
					expression += char
				else:
					raise ValueError('Invalid/Unknown function.')
		
		elif token == 'other':
			raise ValueError('Unrecognised character/function "{}".'.format(char))
		
	return expression


def substitute(expression, X):
	return expression.replace('X', X)


print("\n\n~~CDF Calculator~~\n\n\n")
choice = input('Provide:\ns: start and end of X\nv: values of X\n> ')
X = [] # To suppress type-check warnings

if choice.lower() == 's':
	start = int(input('X-start = '))
	end = int(input('X-end = '))
	X = [str(_) for _ in range(start, end + 1)]

elif choice.lower() == 'v':
	N = int(input('N(X) = '))
	X = []
	for i in range(1, N + 1):
		x = str(eval(input('X{} = '.format(i))))
		X.append(x)

else:
	raise ValueError('Invalid choice. Please enter either s or v.')


choice = input('Provide:\nf: a function f(x)\nv: values of f(x)\n> ')

if choice.lower() == 'f':
	function = input('f(x) = ')

	if not is_balanced(function):
		raise ValueError('Expressions\'s parentheses are unbalanced.')

	if not is_legal(function):
		raise ValueError('Unsupported operations, functions, or expression.')

	function = parse(tokenizer(function))

	Y = [eval(substitute(function, x)) for x in X]

elif choice.lower() == 'v':
	Y = []
	for x in X:
		y = eval(input('f({}) = '.format(x)))
		Y.append(y)

else:
	raise ValueError('Invalid choice. Please enter either f or v.')

cumulative_Y = [sum(Y[:i+1]) for i in range(len(Y))]
if cumulative_Y[-1] != 1:
	raise ValueError('Cumulative sum of X in f(x) does not add up to 1.')

print('\nCDF of f(x) = {}\nat X = {}:'.format(function if choice.lower() == 'f' else Y, X))
print('      / 0;    x < {}'.format(X[0]))
for i in range(len(X[:-1])):
	x = X[i]
	if i == (len(cumulative_Y) // 2) - 1:
		print('F(x)= | {:.2f}; {} <= x < {}'.format(cumulative_Y[i], x, X[i+1]))
	else:
		print('      | {:.2f}; {} <= x < {}'.format(cumulative_Y[i], x, X[i+1]))

print('      \\ 1;    x >= {}'.format(X[-1]))