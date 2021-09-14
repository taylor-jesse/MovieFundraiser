
# +++ Functions +++
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
def int_check(question):
    error = "Please enter a full number between 12 and 130"

    valid = False
    while not valid:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print(error)

# ******* Main Routine *******
name = ""
profit = 0
ticket_count = 0
ticket_sales = 0
MAX_TICKETS = 5
while name != "xxx" and ticket_count < MAX_TICKETS:
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))
    else:
        print("you have one place left")
    # Get details
    name = not_blank("Name: ")

    # check that the age is valid
    age = int_check("Age: ")
    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 130:
        print("This is very old - it looks like a mistake")
        continue
    # calculate ticket price based on age
    if age <16:
        ticket_price = 7.5
    elif age <65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5


#ask the user if they have used the program before or show

#loop into net ticket details


    ticket_count += 1
    ticket_sales += ticket_price
    print ()

ticket_profit = ticket_sales - (5 * ticket_count)
print("Profit from Tickets: ${:.2f}".format(profit))
if ticket_count == MAX_TICKETS:
        print("We have sold out of tickets!")
else:
        print("you have sold {} tickets.    \n")
        "there are {} places still availble" .format(ticket_count, MAX_TICKETS-ticket_count)


    #calculate ticket price

    #loop to ask for snacks

    #calculate snack price

    #ask for payment method and apply surcharge for cards
