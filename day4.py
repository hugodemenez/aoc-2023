
with (open('input4.txt', 'r')) as f:
    lines = f.readlines()

# The file is a table
# In the table, we first have the number of the game
# Then we have list of two digits winning numbers 
# (but one digit numbers are possible and take two char spaces)
# Then we have a delimiter |
# Then we have a list of 2 digits numbers

def part1(lines: list) -> list:
    total_counter : int = 0
    compute : list = list()
    for line in lines:
        line = line[:-1] # remove the \n
        # Get number of the game
        game_number = line.split(':')[0].split(' ')[-1]
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
        total_counter += game_counter
    
        compute.append((game_number, winning_numbers, numbers))
    return compute


def part2(compute : list) -> int:
    ### Part 2
    # We have to count the number of winning numbers
    # Then we earn the X next games 
    # At the end we count the number of games
    # We can go beyond the initial game list
    cards : list = [1 for i in range(len(compute))]
    for index, (game_number, winning_numbers, numbers) in enumerate(compute):
        # Will do recusrive function the create a new compute list
        number_new_cards : int = 0
        for number in numbers:
            if number in winning_numbers:
                number_new_cards += 1
        # Count how many cards I have for the same game
        # We count how many cards we have for the same game
        for y in range(cards[index]):
            for i in range(index+1, index+number_new_cards+1):
                # Don't go beyond the list
                if i < len(cards):
                    cards[i] += 1

    return sum(cards)


print(part2(part1(lines)))
