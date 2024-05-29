def mul(x,y):
	res = []
	for i in x:
		if i+"`" in y or (len(i)==2 and i[0] in y):
			return []
		else:
			res.append(i)
	for i in y:
		if i not in res:
			res.append(i)
	return res

def multiply(x,y):
	res = []
	for i in x:
		for j in y:
			tmp = mul(i,j)
			res.append(tmp) if len(tmp) != 0 else None
	return res

def refine(my_list,dc_list):
	res = []
	for i in my_list:
		if int(i) not in dc_list:
			res.append(i)
	return res

def findEPI(x):
	res = []
	for i in x:
		if len(x[i]) == 1:
			res.append(x[i][0]) if x[i][0] not in res else None
	return res

def findVariables(x):
	var_list = []
	for i in range(len(x)):
		if x[i] == '0':
			var_list.append(chr(i+65)+"`")
		elif x[i] == '1':
			var_list.append(chr(i+65))
	return var_list

def padWithZeros(input_string, desired_length):
	while len(input_string) < desired_length:
		input_string = '0' + input_string
	return input_string

def flatten(x):
	flattened_items = []
	for i in x:
		flattened_items.extend(x[i])
	return flattened_items

def findMinterms(a):
	gaps = a.count('-')
	if gaps == 0:
		return [str(int(a,2))]
	max_value_binary_len = len(bin(pow(2, gaps) - 1)[2:])
	x = [padWithZeros(bin(i)[2:], max_value_binary_len) for i in range(pow(2, gaps))]

	temp = []
	for i in range(pow(2,gaps)):
		temp2,ind = a[:],-1
		for j in x[0]:
			if ind != -1:
				ind = ind+temp2[ind+1:].find('-')+1
			else:
				ind = temp2[ind+1:].find('-')
			temp2 = temp2[:ind]+j+temp2[ind+1:]
		temp.append(str(int(temp2,2)))
		x.pop(0)
	return temp

def compare(a,b):
	c = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			mismatch_index = i
			c += 1
			if c>1:
				return (False,None)
	return (True,mismatch_index)

def removeTerms(_chart,terms):
	for i in terms:
		for j in findMinterms(i):
			try:
				del _chart[j]
			except KeyError:
				pass

print('Enter the minterms')
print('seperated by commas:')
mt = input().strip().split(',')
mt = [int(i) for i in mt]

print("Enter don't cares (if any)")
print("seperated by commas: ")
dc = input()

if dc:
	dc = [int(i) for i in dc.strip().split(',')]
else:
	dc = []

mt.sort()
minterms = mt+dc
minterms.sort()
size = len(bin(minterms[-1]))-2
groups,all_pi = {},set()

for minterm in minterms:
	try:
		groups[bin(minterm).count('1')].append(padWithZeros(bin(minterm)[2:], size))
	except KeyError:
		groups[bin(minterm).count('1')] = [padWithZeros(bin(minterm)[2:], size)]

while True:
	tmp = groups.copy()
	groups,m,marked,should_stop = {},0,set(),True
	l = sorted(list(tmp.keys()))
	for i in range(len(l)-1):
		for j in tmp[l[i]]:
			for k in tmp[l[i+1]]:
				res = compare(j,k)
				if res[0]:
					try:
						groups[m].append(j[:res[1]]+'-'+j[res[1]+1:]) if j[:res[1]]+'-'+j[res[1]+1:] not in groups[m] else None # type: ignore
					except KeyError:
						groups[m] = [j[:res[1]]+'-'+j[res[1]+1:]] # type: ignore
					should_stop = False
					marked.add(j)
					marked.add(k)
		m += 1
	local_unmarked = set(flatten(tmp)).difference(marked)
	all_pi = all_pi.union(local_unmarked)
	if should_stop:
		break

sz = len(str(mt[-1]))
chart = {}
for i in all_pi:
	merged_minterms,y = findMinterms(i),0
	for j in refine(merged_minterms,dc):
		x = mt.index(int(j))*(sz+1)
		y = x+sz
		try:
			chart[j].append(i) if i not in chart[j] else None
		except KeyError:
			chart[j] = [i]

EPI = findEPI(chart)
removeTerms(chart,EPI)

if(len(chart) == 0):
	final_result = [findVariables(i) for i in EPI]
else:
	P = [[findVariables(j) for j in chart[i]] for i in chart]
	while len(P)>1:
		P[1] = multiply(P[0],P[1])
		P.pop(0)
	final_result = [min(P[0],key=len)]
	final_result.extend(findVariables(i) for i in EPI)
print('\nSolution: F = '+' + '.join(''.join(i) for i in final_result))