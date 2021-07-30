def int_check(question):

    error = "please enter whole number that is more than 12 and less than 130"

    valid = False
    while not valid:

            #ask user for a number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)



age = int_check("Age: ", 12, 130)
