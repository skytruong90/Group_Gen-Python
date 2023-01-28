# Program to randomly generate groups
import re
import random

# List to hold list of names
list_of_people = []

# True as long as there is another member to add
has_new_attendee = True

# Use until there is not another member to add
while has_new_attendee:
    # Prompt for name to add
    new_name = input('Please enter your name: ')
    # Add name
    list_of_people.append(new_name)
    # Ask if there is another name
    add_another = input('Do you want to add another name? Y or N\n')
    # Make sure for valid response
    while not re.fullmatch("Y|N|Yes|No|y|n|yes|no", add_another):
        print('Invalid input. Please enter (Y, Yes, N, or No)')
        add_another = input('Do you want to add another name? Y or N\n')
    # If no, stop getting names
    if (add_another == 'N') or (add_another == 'No') or (add_another == 'n') or (add_another == 'no'):
        has_new_attendee = False
# Get number of names
size_of_list = len(list_of_people)
# Group size
max_group_size = 0
# Determine group size automatically or manually
if size_of_list % 2 == 0 and size_of_list <= 10:
    max_group_size = 2
elif size_of_list % 3 == 0 and size_of_list <= 15:
    max_group_size = 3
else:
    print('Number of people: ', size_of_list)
    max_group_size = int(input('Please enter group size: '))

name = 0
numbers_used = []
while name < size_of_list:
    incr = 0
    print('Group')

    while incr < max_group_size:
        r = random.randint(0, size_of_list)
        if r >= size_of_list:
            print()
        elif r not in numbers_used:
            numbers_used.append(r)
            print(list_of_people[r])
            incr += 1
    name += max_group_size
    print()

print(list_of_people)