# create a function that accepts a string
# return a dictionary - key = word in string in LOWERCASE
# key = word , value = word frequency


word = "This is a string yes this is"

def word_count(string):
	word_dict = {}
	lower_string = string.lower()
	split_string = lower_string.split()
	
	for word in split_string:
		if word in word_dict:
			word_dict[word] += 1
		else:
			word_dict[word] = 1

	return word_dict


print(word_count(word))


