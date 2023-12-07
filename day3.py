import logging
with open('input3.txt', 'r') as f:
    lines = f.readlines()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)

line_details : list = list()
for line in lines:
    # Remove the \n
    line = line[:-1]
    # We have to understand where numbers and symbols are
    concat : str = str()
    list_numbers : list = list()
    list_symbols : list = list()
    number_positions : list = list()
    for index, char in enumerate(line):
        try:
            int(char)
            number_positions.append(index)
            concat += char
        except ValueError:
            # ISSUE WAS THERE : IF IT'S END OF LINE AND CONCAT IS NOT EMPTY
            # IT MEANS THERE IS A NUMBER TO ADD
            # Number is terminated
            if len(concat) > 0:
                list_numbers.append({
                    'number':concat,
                    'start': number_positions[0],
                    'end': number_positions[-1],
                })
                concat : str = str()
                number_positions : list = list()
            if char != '.':
                list_symbols.append({
                    'symbol': char,
                    'position': index,
                })
    # If it's the end of the line and concat is not empty
    if len(concat) > 0:
        list_numbers.append({
            'number':concat,
            'start': number_positions[0],
            'end': number_positions[-1],
        })
    # register line details
    line_details.append({
        'line': line,
        'numbers': list_numbers,
        'symbols': list_symbols,
    })
    

def part1(line_details: list) -> int:
    for above,line,below in zip(line_details,line_details[1:],line_details[2:]):
        # For each number in the line we have to check if
        # There is a symbol on the left
        for number in line['numbers']:
            # Check if there is a symbol on the left
            if number['start']>0:
                if number['start']-1 in [symbol['position'] for symbol in line['symbols']]:
                    number['valid'] = True

            # Check if there is a symbol on the right
            if number['end']+1 in [symbol['position'] for symbol in line['symbols']]:
                number['valid'] = True

            # Check if there is a symbol above (diagonal included)
            for symbol in [symbol['position'] for symbol in above['symbols']]:
                if symbol in range(number['start']-1, number['end']+2):
                    number['valid'] = True

            # Check if there is a symbol above (diagonal included)
            for symbol in [symbol['position'] for symbol in below['symbols']]:
                if symbol in range(number['start']-1, number['end']+2):
                    number['valid'] = True
            
            if number.get('valid'):
                logger.info(f"Number {number['number']} is valid")
                # above
                logger.info(f"A: {above['line']}")
                # line
                logger.info(f"L: {line['line']}")
                # below
                logger.info(f"B: {below['line']}")

    # Remember to check the first line
    line = line_details[0]
    below = line_details[1]
    for number in line_details[0]['numbers']:
        # Check if there is a symbol on the left
        if number['start']-1 in [symbol['position'] for symbol in line['symbols']]:
            number['valid'] = True

        # Check if there is a symbol on the right
        if number['end']+1 in [symbol['position'] for symbol in line['symbols']]:
            number['valid'] = True

        # Check if there is a symbol below (diagonal included)
        for symbol in [symbol['position'] for symbol in below['symbols']]:
            if symbol in range(number['start']-1, number['end']+2):
                number['valid'] = True

        if number.get('valid'):
            logger.info(f"Number {number['number']} is valid")
            # line
            logger.info(f"L: {line['line']}")
            # below
            logger.info(f"B: {below['line']}")

    # Remember to check the last line
    above = line_details[-2]
    line = line_details[-1]
    for number in line_details[-1]['numbers']:
        # Check if there is a symbol on the left
        if number['start']-1 in [symbol['position'] for symbol in line['symbols']]:
            number['valid'] = True

        # Check if there is a symbol on the right
        if number['end']+1 in [symbol['position'] for symbol in line['symbols']]:
            number['valid'] = True

        # Check if there is a symbol above (diagonal included)
        for symbol in [symbol['position'] for symbol in above['symbols']]:
            if symbol in range(number['start']-1, number['end']+2):
                number['valid'] = True

        if number.get('valid'):
            logger.info(f"Number {number['number']} is valid")
            # above
            logger.info(f"A: {above['line']}")
            # line
            logger.info(f"L: {line['line']}")

    # Now we sum each valid number
    counter : int = 0
    for details in line_details:
        for number in details['numbers']:
            if number.get('valid'):
                counter += int(number['number'])

    logger.info(f"The final counter is {counter}")
    return counter

## Part 2
# We have to check for gears multiplier
# If there is a * which is adjacent to TWO numbers and no more
# Then it means that the two numbers are multiplied

GEAR_SYMBOL : str = '*'
def part2(line_details: list) -> int:
    counter : int = 0 
    # Figure out how to understand if a number is multiplied
    # by another one
    # For each gear we will list all numbers that are adjacent
    # to it
    # If there is more than two, then it's not a gear
    # If there is two, then it's a gear
    for above,line,below in zip(line_details,line_details[1:],line_details[2:]):
        for symbol in line['symbols']:
            if symbol['symbol'] == GEAR_SYMBOL:
                symbol['gear'] = list()
                for number in line['numbers']:
                    # Check if there is a number on the left
                    if number['end']+1 == symbol['position']:
                        # Number could be part of a gear
                        symbol['gear'].append(number)
                    # Check if there is a number on the right
                    if number['start']-1 == symbol['position']:
                        # Number could be part of a gear
                        symbol['gear'].append(number)
                # Check if there is a number adjacent on the upper line
                for number in above['numbers']:
                    if  symbol['position'] in range(number['start']-1, number['end']+2):
                        # Number could be part of a gear
                        symbol['gear'].append(number)
                # Check if there is a number adjacent on the lower line
                for number in below['numbers']:
                    if  symbol['position'] in range(number['start']-1, number['end']+2):
                        # Number could be part of a gear
                        symbol['gear'].append(number)

    # Check the first line
    line = line_details[0]
    below = line_details[1]
    for symbol in line_details[0]['symbols']:
        if symbol['symbol'] == GEAR_SYMBOL:
            symbol['gear'] = list()
            for number in line['numbers']:
                # Check if there is a number on the left
                if number['end']+1 == symbol['position']:
                    # Number could be part of a gear
                    symbol['gear'].append(number)
                # Check if there is a number on the right
                if number['start']-1 == symbol['position']:
                    # Number could be part of a gear
                    symbol['gear'].append(number)
            # Check if there is a number adjacent on the lower line
            for number in below['numbers']:
                if  symbol['position'] in range(number['start']-1, number['end']+2):
                    # Number could be part of a gear
                    symbol['gear'].append(number)

    # Check the last line
    above = line_details[-2]
    line = line_details[-1]
    for symbol in line_details[-1]['symbols']:
        if symbol['symbol'] == GEAR_SYMBOL:
            symbol['gear'] = list()
            for number in line['numbers']:
                # Check if there is a number on the left
                if number['end']+1 == symbol['position']:
                    # Number could be part of a gear
                    symbol['gear'].append(number)
                # Check if there is a number on the right
                if number['start']-1 == symbol['position']:
                    # Number could be part of a gear
                    symbol['gear'].append(number)
            # Check if there is a number adjacent on the upper line
            for number in above['numbers']:
                if  symbol['position'] in range(number['start']-1, number['end']+2):
                    # Number could be part of a gear
                    symbol['gear'].append(number)

    # Now we have to check if the gear is valid
    # If there is two numbers, then it's valid
    # Else, it's not
    for details in line_details:
        for symbol in details['symbols']:
            if symbol['symbol'] == GEAR_SYMBOL:
                if len(symbol['gear']) == 2:
                    logger.error(f"Gear {symbol['gear'][0]['number']} * {symbol['gear'][1]['number']} is valid")
                    # Instead of computing again, we can just remove the numbers
                    # and add the multiplier
                    symbol['multiplier'] = int(symbol['gear'][0]['number']) * int(symbol['gear'][1]['number'])
                    # Remove the numbers
                    counter += symbol['multiplier'] 
    return counter 

print(f'Part 2: {part2(line_details)}')
