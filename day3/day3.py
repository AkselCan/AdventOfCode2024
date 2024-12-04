import re

# Read input text from a file
with open('C:/Users/aksel/OneDrive/Masaüstü/personal_projects/adventofcode/2024/day3/input.txt', 'r') as file:
    text = file.read()

def find_mul_expressions(text):
    # Regular expression to find all occurrences of 'mul(int, int)'
    pattern = r'mul\((\d+),(\d+)\)'
    return re.findall(pattern, text)


# Split text by instructions
instructions = re.findall(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)', text)

mul_enabled = True
count = 0

for instruction in instructions:
    instruction = instruction.strip()
    if instruction == 'do()':
        mul_enabled = True
    elif instruction == "don't()":
        mul_enabled = False
    elif mul_enabled and instruction.startswith('mul'):
        match = re.match(r'mul\((\d+),(\d+)\)', instruction)
        if match:
            a, b = map(int, match.groups())
            count += a * b

print(f"Total sum of products: {count}")
