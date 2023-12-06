import logging
with open('input3.txt', 'r') as f:
    lines = f.readlines()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

line_details : list = list()
for line in lines:
    # Remove the \n
    line = line[:-1]
    # We have to understand where numbers and symbols are
    concat : str = str()
    list_numbers : list = list()
    number_positions : list = list()
    symbol_positions : list = list()
    symbol : list = list()
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
                symbol_positions.append(index)
                symbol.append(char)
    # If it's the end of the line and concat is not empty
    if len(concat) > 0:
        logger.error(f"Concat is not empty {concat}")
        list_numbers.append({
            'number':concat,
            'start': number_positions[0],
            'end': number_positions[-1],
        })



    # register line details
    line_details.append({
        'line': line,
        'numbers': list_numbers,
        'symbols': symbol_positions,
        'symbols_char': symbol,
    })
    

for above,line,below in zip(line_details,line_details[1:],line_details[2:]):
    # For each number in the line we have to check if
    # There is a symbol on the left
    for number in line['numbers']:
        # Check if there is a symbol on the left
        if number['start']>0:
            if number['start']-1 in line['symbols']:
                number['valid'] = True

        # Check if there is a symbol on the right
        if number['end']+1 in line['symbols']:
            number['valid'] = True

        # Check if there is a symbol above (diagonal included)
        for symbol in above['symbols']:
            if symbol in range(number['start']-1, number['end']+2):
                number['valid'] = True

        # Check if there is a symbol above (diagonal included)
        for symbol in below['symbols']:
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
    if number['start']-1 in line['symbols']:
        number['valid'] = True

    # Check if there is a symbol on the right
    if number['end']+1 in line['symbols']:
        number['valid'] = True

    # Check if there is a symbol below (diagonal included)
    for symbol in below['symbols']:
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
    if number['start']-1 in line['symbols']:
        number['valid'] = True

    # Check if there is a symbol on the right
    if number['end']+1 in line['symbols']:
        number['valid'] = True

    # Check if there is a symbol above (diagonal included)
    for symbol in above['symbols']:
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

