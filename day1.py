
with open("./input.txt", "r") as f:
    lines = f.readlines()

def part1(line: str, counter: int):
    # Concat the first and last digit of line
    value : str = str()
    values : list = list()
    for char in line:
        try:
            int(char)
            values.append(char)
            print(f'Value: {char}')
        except ValueError:
            print(f'Error: {char} is not a number')
    try:
        if len(values) > 1:
            value = str(values[0]) + str(values[-1])
        else: 
            value = str(values[0]) + str(values[0])
        print(f"The value of {line} is {value}")
        counter += int(value)
    except IndexError:
        print(f"Error: {line} doesn't contain number")
    return counter

### Part 1
counter : int = 0
for line in lines:
    line = line[:-1]
    counter = part1(line, counter)
print(f"The final counter for part 1 is {counter}")

### Part 2
### There are also digits spelled with letters
NUMBERRS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six", 
    "seven",
    "eight",
    "nine",
]
counter : int = 0
for line in lines:
    # Remove the next line character
    line = line[:-1]
    print(f"Line: {line}")
    # Try every combination of letters and see if it's a number
    # Be careful because oneight refers to 18
    line_number : str = str()
    for i in range(len(line)):
        for j in range(len(line)+1):
            # Get the substring
            substring = line[i:j]
            if len(substring) == 1:
                try:
                    int(substring)
                    # It's a number
                    # Produce a new line with the numbers
                    line_number+=substring
                    break
                except ValueError:
                    # It's not a number
                    continue
            # Check if it's a number
            if substring in NUMBERRS:
                # Can't replace
                # Produce a new line with the numbers
                line_number+=str(NUMBERRS.index(substring) + 1)
                break
    # Can repeat the previous algorithm
    counter = part1(line_number, counter)

print(f"The final counter for part 2 is {counter}")
