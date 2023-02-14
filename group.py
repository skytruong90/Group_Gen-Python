import random

def generate_groups(names, group_size):
    """
    This function takes in a list of names and the desired group size, and
    randomly generates groups of people based on the given size.
    """
    random.shuffle(names) # shuffle the list of names
    groups = []
    for i in range(0, len(names), group_size):
        groups.append(names[i:i+group_size])
    return groups

# get input from user
names = input("Enter names separated by commas: ").split(",")
group_size = int(input("Enter group size: "))

# generate groups
groups = generate_groups(names, group_size)

# print groups
print("Groups:")
for i, group in enumerate(groups):
    print(f"Group {i+1}: {', '.join(group)}")
