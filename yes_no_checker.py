def yes_no(question):

    error = "Please answer yes or no"

    valid = False
    while not valid:

        # ask question and put response in lowercase
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print(error)


#main routine goes here

for item in range (0,6):
    want_snacks = yes_no("Do you want snacks? ")
    print("Answer {} ".format(want_snacks))
