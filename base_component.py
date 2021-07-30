
# ***** Main routine ****
#set up directories
# not blank function
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)

        while response != "":
            return response

        else:
            print("This can't be blank please enter a name")
#Int checker
name = ""
count = 0
max_tickets = 5
while name != "xxx" and count < max_tickets:
    print("You have {} seats "
          "left".format(max_tickets - count))

    # Get details
    name = input ("Name: ")
    count += 1
    print ()

    if count == max_tickets:
        print("We have sold out of tickets!")
else:
    print("you have sold {} tickets.    \n")
    "there are {} places still availble" .format(count, max_tickets - count)

#ask the user if they have used the program before or show

#loop into net ticket details
    #Get name
name = not_blank("What is your name? ")
    #get age
age = not_blank("How old are you? ")

    #calculate ticket price

    #loop to ask for snacks

    #calculate snack price

    #ask for payment method and apply surcharge for cards
