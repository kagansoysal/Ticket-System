import sys
input_file = sys.argv[1]
opening_the_file = open(input_file, "r")
categories = {} # our dictionary where we keep all the data
rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
current_category_names = [] # to keep information of available categories
writing_output = open("output.txt", "w")

# we use this function to create a new category according to its dimensions
def create_category():
    measurements = infos_of_input[2].split("x")
    if infos_of_input[1] not in current_category_names:
        categories[infos_of_input[1]] = {}
        for i in range(int(measurements[0]), 0, -1):
            number_rows = str(rows[i - 1])
            categories[infos_of_input[1]][number_rows] = {}
            for k in range(0, int(measurements[1])):
                categories[infos_of_input[1]][number_rows][k] = "X"
        current_category_names.append(infos_of_input[1])
        number_of_seats_in_category = int(measurements[0]) * int(measurements[1])
        output(f"The category '{infos_of_input[1]}' having {number_of_seats_in_category} seats has been created")
    else:
        output(f"Warning: Cannot create the category for the second time. The stadium has already {infos_of_input[1]}")

# When someone wants to buy a ticket, we check the availability of that seat and, if it is, we sell that ticket to that person.
def sell_ticket():
    lenght_of_infos_of_input = len(infos_of_input)
    if infos_of_input[3] in current_category_names:
        for infos_of_seats in range(4, lenght_of_infos_of_input):
            if "-" in infos_of_input[infos_of_seats]:
                index_of_score = infos_of_input[infos_of_seats].index("-")
                row_name = infos_of_input[infos_of_seats][0]
                first_seat_in_interval = int(infos_of_input[infos_of_seats][1:index_of_score])
                last_seat_in_interval = int(infos_of_input[infos_of_seats][index_of_score+1:])
                control_list = []

                if row_name not in categories[infos_of_input[3]] and last_seat_in_interval > len(categories[infos_of_input[3]][row_name]):
                    output(f"Error: The category '{infos_of_input[3]}' has less row and column than the specified index {infos_of_input[infos_of_seats]}!")
                elif row_name not in categories[infos_of_input[3]]:
                    output(f"Error: The category '{infos_of_input[3]}' has less row than the specified index {infos_of_input[infos_of_seats]}!")
                elif last_seat_in_interval > len(categories[infos_of_input[3]][row_name]):
                    output(f"Error: The category '{infos_of_input[3]}' has less column than the specified index {infos_of_input[infos_of_seats]}!")
                else:
                    for numbers_of_seats in range(first_seat_in_interval, last_seat_in_interval+1):
                        for p in categories[infos_of_input[3]][row_name][numbers_of_seats]:
                            control_list.append(p)

                        if "S" in control_list or "F" in control_list or "T" in control_list:
                            output(f"Warning: The seats {infos_of_input[infos_of_seats]} cannot be sold to {infos_of_input[1]} due some of them have already been sold")
                            break
                        else:
                            if infos_of_input[2] == "student":
                                categories[infos_of_input[3]][row_name][numbers_of_seats] = "S"
                            elif infos_of_input[2] == "full":
                                categories[infos_of_input[3]][row_name][numbers_of_seats] = "F"
                            elif infos_of_input[2] == "season":
                                categories[infos_of_input[3]][row_name][numbers_of_seats] = "T"

                            if numbers_of_seats < last_seat_in_interval:
                                continue
                            else:
                                output(f"Success: {infos_of_input[1]} has bought {infos_of_input[infos_of_seats]} at {infos_of_input[3]}")
            else:
                row_name = infos_of_input[infos_of_seats][0]
                number_of_seat = int(infos_of_input[infos_of_seats][1:])
                if row_name not in categories[infos_of_input[3]] and number_of_seat > len(categories[infos_of_input[3]][row_name]):
                    output(f"Error: The category '{infos_of_input[3]}' has less row and column than the specified index {infos_of_input[infos_of_seats]}!")
                elif row_name not in categories[infos_of_input[3]]:
                    output(f"Error: The category '{infos_of_input[3]}' has less row than the specified index {infos_of_input[infos_of_seats]}!")
                elif number_of_seat > len(categories[infos_of_input[3]][row_name]):
                    output(f"Error: The category '{infos_of_input[3]}' has less column than the specified index {infos_of_input[infos_of_seats]}!")
                else:
                    if categories[infos_of_input[3]][row_name][number_of_seat] == "X":
                        if infos_of_input[2] == "student":
                            categories[infos_of_input[3]][row_name][number_of_seat] = "S"
                        elif infos_of_input[2] == "full":
                            categories[infos_of_input[3]][row_name][number_of_seat] = "F"
                        elif infos_of_input[2] == "season":
                            categories[infos_of_input[3]][row_name][number_of_seat] = "T"

                        output(f"Success: {infos_of_input[1]} has bought {infos_of_input[infos_of_seats]} at {infos_of_input[3]}")
                    else:
                        output(f"Warning: The seat {infos_of_input[i]} cannot be sold to {infos_of_input[1]} since it was already sold!")
    else:
        output(f"{infos_of_input[3]} is not exist in that stadium.")

# we use this function to make a sold ticket resalable
def cancel_ticket():
    lenght_of_infos_of_input = len(infos_of_input)
    for seat_name in range(2, lenght_of_infos_of_input):
        row_name = infos_of_input[seat_name][0]
        column_name = int(infos_of_input[seat_name][1:])
        the_category_name = infos_of_input[1]
        if row_name not in categories[the_category_name] and column_name > len(categories[the_category_name]["A"]):
            output(f"Error: The category '{infos_of_input[1]}' has less row and column than the specified index {infos_of_input[seat_name]}!")
        elif row_name not in categories[the_category_name]:
            output(f"Error: The category '{infos_of_input[1]}' has less row than the specified index {infos_of_input[seat_name]}!")
        elif column_name > len(categories[the_category_name][row_name]):
            output(f"Error: The category '{infos_of_input[1]}' has less column than the specified index {infos_of_input[seat_name]}!")
        else:
            if categories[the_category_name][row_name][column_name] == "X":
                output(f"Error: The seat {infos_of_input[seat_name]} at '{infos_of_input[1]}' has already been free! Nothing to cancel")
            else:
                categories[the_category_name][row_name][column_name] = "X"
                output(f"Success: The seat {infos_of_input[seat_name]} at '{infos_of_input[1]}' has been canceled and now ready to sell again")

# we calculate how many of which type of ticket are sold in a category and the total revenue obtained from that category
def balance():
    sum_of_students = 0
    sum_of_full_pay = 0
    sum_of_season_ticket = 0

    for row_name in categories[infos_of_input[1]]:
        for column_name in categories[infos_of_input[1]][row_name]:
            if categories[infos_of_input[1]][row_name][column_name] == "S":
                sum_of_students += 1
            elif categories[infos_of_input[1]][row_name][column_name] == "F":
                sum_of_full_pay += 1
            elif categories[infos_of_input[1]][row_name][column_name] == "T":
                sum_of_season_ticket += 1

    revenue = sum_of_students*10 + sum_of_full_pay*20 + sum_of_season_ticket*250

    output(f"category report of '{infos_of_input[1]}'\n------------------------------")
    output(f"Sum of students = {sum_of_students}, Sum of full pay = {sum_of_full_pay}, Sum of season ticket = {sum_of_season_ticket}, and Revenues = {revenue} Dollars")

# we use this function to visually see which seats are sold from a category
def show_category():
    print(f"Printing category layout of {infos_of_input[1]}")
    writing_output.write(f"Printing category layout of {infos_of_input[1]}\n")
    for row_name in categories[infos_of_input[1]]:
        print(row_name, end = " ")
        writing_output.write(row_name + " " )
        for column_name in categories[infos_of_input[1]][row_name]:
            print(categories[infos_of_input[1]][row_name][column_name], end = "  ")
            writing_output.write(categories[infos_of_input[1]][row_name][column_name] + "  ")
        print()
        writing_output.write("\n")

    print("  ", end = "")
    writing_output.write("  ")

    for row_name2 in categories[infos_of_input[1]]:
        for column_name2 in categories[infos_of_input[1]][row_name]:
            if column_name2 < 9:
                print(column_name2, end = "  ")
                writing_output.write(str(column_name2) + "  ")
            else:
                print(column_name2, end = " ")
                writing_output.write(str(column_name2) + " ")
        print()
        writing_output.write("\n")
        break

# We use this function to print the output that we will print to the output file
def output(x):
    print(x)
    writing_output.write(x + "\n")

lenght_of_file = open(input_file, "r").readlines()

# We use this loop to read the information in the input.txt file line by line, respectively.
for i in range(len(lenght_of_file)):
    infos_of_input = opening_the_file.readline().split()
    if infos_of_input[0] == "CREATECATEGORY":
        create_category()
    if infos_of_input[0] == "SELLTICKET":
        sell_ticket()
    if infos_of_input[0] == "CANCELTICKET":
        cancel_ticket()
    if infos_of_input[0] == "BALANCE":
        balance()
    if infos_of_input[0] == "SHOWCATEGORY":
        show_category()