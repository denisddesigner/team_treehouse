template = "Hi, I'm {name} and I love to eat {food}!"

dicts_list = [{"name":"Denis", "food":"Pizza"}, {"name":"Thomas", "food":"Pork"} ]

def string_factory(list_of_dicts):
    li = []
    for dictionary in list_of_dicts:
        li.append(template.format(**dictionary))
    return li

print(string_factory(dicts_list))