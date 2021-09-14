def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower().strip()

        if response in to_check:
            return response
        else:
            for item in to_check:
                # checks if response is the first letter of an item in the list
                if response == item [0]:
                    #note: returns the entire response
                    return item

        print("sorry that is not a valid response")

for item in range (0, 6):
    want_snacks = string_checker("Do you want snacks? ", ["yes", "no"])
    print("Answer ok, you said: {}".format(want_snacks))
    print()
