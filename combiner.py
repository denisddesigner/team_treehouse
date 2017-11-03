# return a string with list items together
# check if item in list is integer or string
# add numbers and add strings
# concatenate the two results together


list1 = ["apple", 5.2, "dog", 8 ]


def combiner(list2):

	sum1 = 0
	string = ""

	for item in list2:
		if isinstance(item, int):
			sum1 += item
		elif isinstance(item, float):
			sum1 += item
		else:
			string += item

	return string + str(sum1)


print(combiner(list1))


