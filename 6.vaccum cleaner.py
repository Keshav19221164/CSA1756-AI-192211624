import random

# Define the grid (house)
house = [
    ['Dirty', 'Dirty', 'Dirty'],
    ['Dirty', 'Dirty', 'Dirty'],
    ['Dirty', 'Dirty', 'Dirty']
]

# Function to display the grid
def display_house(house):
    for row in house:
        print(row)
    print()

# Function to simulate the vacuum cleaner's movement and cleaning
def vacuum_cleaner(house):
    for i in range(len(house)):
        for j in range(len(house[i])):
            if house[i][j] == 'Dirty':
                print(f"Vacuum cleaner is at position ({i}, {j}) - Cleaning")
                house[i][j] = 'Clean'
            else:
                print(f"Vacuum cleaner is at position ({i}, {j}) - Already clean")
            display_house(house)

# Initial display of the house
print("Initial state of the house:")
display_house(house)

# Start the vacuum cleaner
vacuum_cleaner(house)

print("Final state of the house:")
display_house(house)
