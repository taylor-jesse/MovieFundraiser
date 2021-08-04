error_age = ("Please enter a full number between 12 and 130")
def int_check(question, low_num, high_num):

    valid = False
    while not valid:

        try:
            response = int(input(question))

        if low_num < response < high_num:
           return response
        else:
            print (error_age)

except ValueError
    print(error_age)

age = int_check("Age: ", 12, 130)
