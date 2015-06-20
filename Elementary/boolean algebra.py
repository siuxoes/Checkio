__author__ = 'Siuxoes'

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == OPERATION_NAMES[0]:
    	return x & y
    elif operation == OPERATION_NAMES[1]:
    	return x | y
    elif operation == OPERATION_NAMES[2]:
    	if x == 0:
    		return 1
    	else:
    		return y
    elif operation == OPERATION_NAMES[3]:
    	return x ^ y
    else:
    	if x == y:
    		return 1
    	else:
    		return 0