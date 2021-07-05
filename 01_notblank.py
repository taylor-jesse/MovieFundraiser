# not blank function
def not_blank(name)
    valid = False
    while not valid:
        response = input(name)

        while response != "":
            return response

        else:
            print("This can't be blank please enter a name")

def not_blank(age)
    valid = False
    while not valid:
        response = input(age)

        while response != "":
            return response

        else:
            print("This can't be blank please enter Your age")
