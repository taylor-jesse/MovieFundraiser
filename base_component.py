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
age = not_blank("How old are you? ")



#set up directories

#ask the user if they have used the program before or show

#loop into net ticket details
    #Get name

    #get age

    #calculate ticket price

    #loop to ask for snacks

    #calculate snack price

    #ask for payment method and apply surcharge for cards
