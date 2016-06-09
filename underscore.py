

def _map(arr, callback):
	return_array = []
	for element in arr:
		transformed = callback(element)
		return_array.append(transformed)
	return return_array

def _filter(arr, callback):
	return_array = [];
	for element in arr:
		if callback(element):
			return_array.append(element)
	return return_array

def _any(arr, callback):
	for element in arr:
		if (callback(element)):
			return True
	return False

def _every(arr, callback):
	for element in arr:
		if callback(element) == False:
			return False
	return True

def _contains(arr, value):
	if value in arr:
		return True
	return False

def _reduce(arr, callback, start_value):
	for element in arr:
		start_value = callback(element, start_value)
	return start_value


