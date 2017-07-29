word = "treehouse"


def sillycase(string):
    
    string_len = len(string) // 2 
    
    
    return string[:string_len].lower() + string[string_len:].upper()


print(sillycase(word))