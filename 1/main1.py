filename="AoC24/1/input.txt"
column1 = []
column2 = []

with open(filename, 'r') as file:
    for line in file:
        parts=line.strip().split("   ")
        if len(parts) == 2:
            column1.append(int(parts[0]))
            column2.append(int(parts[1]))

sorted1 = sorted(column1)
sorted2 = sorted(column2)

sum = 0
for x,y in zip(sorted1, sorted2):
    sum = sum + abs(x - y)

print(sum)