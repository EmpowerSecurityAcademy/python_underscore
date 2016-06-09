import unittest
from underscore import _map, _filter, _any, _every, _contains, _reduce

class TestUnderscore(unittest.TestCase):

	def test_map(self):
		def multiply_2(num):
			return num * 2

		input_array = [3, 4, 5, 6, 7]
		res = _map(input_array, multiply_2)

		self.assertEqual(res, [6, 8, 10, 12, 14])

	def test_filter(self):
	    def start_with_a(word):
	    	if word[0] == "a":
	    		return True 
	    	return False

	    input_array = ["artichoke", "orangatang", "kiwi", "orange"]
	    res = _filter(input_array, start_with_a)

	    self.assertEqual(res, ["artichoke"])

	def test_any(self):
		def greater_than_10(number):
			if number > 10:
				return True
			return False

		input_array = [8, 5, 9, 11]
		res = _any(input_array, greater_than_10)
		self.assertEqual(res, True)

	def test_every(self):
		def greater_than_10(number):
			if number > 10:
				return True
			return False

		input_array = [11, 15, 19, 21]
		res = _any(input_array, greater_than_10)
		self.assertEqual(res, True)

	def test_contains(self):
		input_array = [3, 4, 5, 6]
		res = _contains(input_array, 6)
		self.assertEqual(res, True)

	def test_reduce(self):

		def summer(num_1, num_2):
			return num_1 + num_2

		input_array = [8, 5, 9, 11]
		res = _reduce(input_array, summer, 0)
		self.assertEqual(res, 33)




if __name__ == '__main__':
    unittest.main()