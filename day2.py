
with open('input2.txt', 'r') as f:
    lines = f.readlines()

list_games : list = list()
for line in lines:
    line = line[:-1]
    # Get the id of the line
    id = line.split('Game ')[1].split(':')[0]
    games : list = list()
    # Get the games
    games = line.split(id+': ')[1].split('; ')
    # For each game we just have to remember the max number of cubes
    cubes_counter : dict = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for game in games:
        # Count the number of cubes depending on the color
        cubes = game.split(', ')
        for cube in cubes:
            if 'red' in cube:
                if cubes_counter['red'] < int(cube.split(' red')[0]): 
                    cubes_counter['red'] = int(cube.split(' red')[0])
            elif 'green' in cube:
                if cubes_counter['green'] < int(cube.split(' green')[0]): 
                    cubes_counter['green'] = int(cube.split(' green')[0])
            elif 'blue' in cube:
                if cubes_counter['blue'] < int(cube.split(' blue')[0]): 
                    cubes_counter['blue'] = int(cube.split(' blue')[0])
    #print(f"For the games : {games} the counter is {cubes_counter}")
    # Register values
    cubes_counter['id'] = id
    list_games.append(cubes_counter)

counter : int = 0
power_counter : int = 0
# Now checks all possible games
for games in list_games:
    if games['red'] <= 12 and games['green'] <= 13 and games['blue'] <= 14:
        counter += int(games['id'])
        print(f"Game {games['id']} is valid: {games}")
    # computer the power of sets
    power = games['red'] * games['green'] * games['blue']
    power_counter += power

print(f"The final counter is {counter}")
print(f"The final power counter is {power_counter}")
