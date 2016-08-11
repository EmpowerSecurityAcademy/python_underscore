

def p_map(func, lst):

	return_list = []

	for element in lst:
		transformed = func(element)
		return_list.append(transformed)

	return return_list


def p_filter(func, lst):

	return_list = []

	for element in lst:
		if func(element) == True:
			return_list.append(element)

	return return_list



def p_any(func, lst):

	for element in lst:
		if func(element) == True:
			return True
	return False


def p_every(func, lst):

	for element in lst:
		if func(element) == False:
			return False

	return True


def p_contains(lst, value):

	if value in lst:
		return True

	return False


def p_reduce(func, lst, start_value):

	for element in lst:
		start_value = func(start_value, element)

	return start_value

