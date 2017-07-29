word = "hippopotamusi"

def first_4(iterate):
    return iterate[:4]

print(first_4(word))


def first_and_last_4(iterate):
    return iterate[:4] + iterate[-4:]
    
    
print(first_and_last_4(word))


def odds(iterate):
    return iterate[1::2]
    
print(odds(word))


def reverse_evens(iterate):
    
    return iterate[-1::-2]
    
    
print(reverse_evens(word))