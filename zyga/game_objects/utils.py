import random

def create_attribute_list(attributes):
    attribute_list = {}

    for k, v in attributes.items():
        for key, value in v.items():
            if type(value) is dict:
                attribute_list[key] = random.randint(value['min'], value['max'])
            else:
                attribute_list[key] = value

    return attribute_list
