print("\n~~Square Completer~~")
print("Enter your terms in")
print("this form:")
print("aX**2 bX c\n")

user_in = input("> ")

def extract_variable(expression):
	letters = [char for char in expression if char.isalpha()]
	if all(letter.upper() == letters[0].upper() for letter in letters):
		return letters[0]
	else:
		raise ValueError("Only use one kind of single-letter variable in the whole expression.")

variable = extract_variable(user_in)
variable_low = variable.lower()

def split_into_terms(expression):
	terms = [str(eval(term)) if '(' in term and ')' in term else term for term in expression.split(' ')]
	print("\nWorking with:\n{}\n".format(' + '.join(terms)))
	return terms

terms = split_into_terms(user_in)

def bin_terms(terms):
	squareds, x_es, constants = [], [], []
	for term in terms:
		term = term.strip().lower()
		if term.endswith('**2'):
			squareds.append(term[:-3])
		elif term.endswith(variable_low):
			x_es.append(term)
		elif term.replace('.', '', 1).isdigit() or term.replace('-', '', 1).replace('.', '', 1).isdigit():
			constants.append(term)
	return squareds, x_es, constants

squareds, x_es, constants = bin_terms(terms)

def sum_bins(squareds, x_es, constants):
	squareds = [squared[:-1] for squared in squareds if squared.endswith(variable_low)]
	squareds = ['1' if squared == variable_low else squared for squared in squareds]
	constant = sum(float(c) for c in constants)
	x = sum(float(el[:-1]) for el in x_es)
	squared = sum(float(el) for el in squareds)
	return squared, x, constant

squared, x, constant = sum_bins(squareds, x_es, constants)

def complete_square(a,b,c):
	p = b/(2*a)
	q = c - (b**2)/(4*a)
	return p, q

p, q = complete_square(squared, x, constant)
a = squared
print('Result is:\n{}({} + ({}))^2 + ({})'.format(a, variable, p, q))