from operator import pow, add, sub, mul, truediv

operators = {
	'+' : add,
	'-' : sub,
	'*' : mul,
	'/' : truediv
	}
#print(operators)

def calculate(s):
	if s.isdigit():
		return float(s)
	for k in operators.keys():
		left, operator, right = s.partition(k)
		if operator in operators:
			return operators[operator](calculate(left), calculate(right))

calc = input("Enter required Calculation:\n")
#type(calculate(calc))
print("Answer is: " + str(calculate(str(calc))))
		
