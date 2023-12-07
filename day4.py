
with (open('input4.txt', 'r')) as f:
    lines = f.readlines()

# The file is a table
# In the table, we first have the number of the game
# Then we have list of two digits winning numbers 
# (but one digit numbers are possible and take two char spaces)
# Then we have a delimiter |
# Then we have a list of 2 digits numbers

total_counter : int = 0
for line in lines:
    line = line[:-1] # remove the \n
    # Get number of the game
    game_number = line.split(':')[0].split(' ')[1]
    winning_numbers_string = line.split(': ')[1].split(' |')[0]
    numbers_string = line.split(': ')[1].split('| ')[1]
    # We have to split the winning numbers
    winning_numbers = list()
    for i in range(0,len(winning_numbers_string),3):
        winning_numbers.append(int(winning_numbers_string[i:i+2]))

    # We have to split the numbers we got
    numbers = list()
    for i in range(0,len(numbers_string),3):
        numbers.append(int(numbers_string[i:i+2]))

    # Now we have to check if the numbers are winning numbers
    game_counter : int = 0
    for number in numbers:
        if number in winning_numbers:
            if game_counter >= 1:
                game_counter = game_counter*2
            else:
                game_counter = 1
    print(f'Game {line} counter: {game_counter}')
    total_counter += game_counter

print(f'Part 2: {total_counter}')



