list1, list2 = [], []
file_path = 'C:/Users/aksel/OneDrive/Masaüstü/personal_projects/adventofcode/2024/day1/input.txt'
difference = 0
sum = 0

with open(file_path, 'r') as file:
    
    for line in file:
        # Split each line by whitespace and convert to integers
        col1, col2 = map(int, line.split())
        
        # Append the integers to the respective lists
        list1.append(col1)
        list2.append(col2)

# Sort the lists
list1.sort()
list2.sort()

for val1, val2 in zip(list1, list2):
    count = list2.count(val1)
    count = val1 * count
    sum += count
    print(sum)

