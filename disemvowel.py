word = "helloAh"

def disemvowel(word):
    
    list_word = list(word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_list = []

    for letter in list_word:
    	if letter.lower() not in vowels:
    		new_list.append(letter)

    return ''.join(new_list)
    	

    
    
print(disemvowel(word))