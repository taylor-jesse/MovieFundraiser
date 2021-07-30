#initilize loop so it runs at least once

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

