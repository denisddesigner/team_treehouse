dict_teachers = {"Kenneth": "Python", "Nick": "CSS", "Carson": "HTML"}

list_courses = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],'Kenneth Love': ['Python Basics', 'Python Collections']}


def num_teachers(dict_teachers):

	return len(dict_teachers)
    
print(num_teachers(dict_teachers))




def num_courses(teachers_dict):
    
    count = 0
    for values in teachers_dict.values():
    	for value in values:
    		count += 1
    return count
    
    
print(num_courses(list_courses))   


def courses(teachers_dict):
    
    courses = []
    for values in teachers_dict.values():
    	for value in values:
    		courses.append(value)
    return courses
    
    
print(courses(list_courses))


def most_courses(teachers_dict):
    
    courses = []
    for values in teachers_dict.values():
    	for value in values:
    		courses.append(value)
    return courses
    
    
print(most_courses(dict_teachers))