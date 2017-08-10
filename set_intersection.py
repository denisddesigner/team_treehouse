COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

word = {"loops"}

def covers(topic):
  courses_on_topic = []
  for course_name in set(COURSES.keys()):
    if len(topic.intersection(COURSES[course_name])) > 0:
      courses_on_topic.append(course_name)

  return courses_on_topic


print(covers(word))