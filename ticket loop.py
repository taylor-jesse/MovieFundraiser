# not blank function
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)

        while response != "":
            return response

        else:
            print("This can't be blank please enter a name")

# ***** Main routine ****
name = not_blank("What is your name? ")
