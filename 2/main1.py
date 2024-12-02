import copy

filename="input.txt"

def genMuts(nums):
    for x in range(len(nums)):
        yield nums[:x] + nums[x+1:]

def check_list(numbers, max_step):
    ascending = all(numbers[i] < numbers[i+1] for i in range(len(numbers) -1))
    descending = all(numbers[i] > numbers[i+1] for i in range(len(numbers) -1))
    valid = all(abs(numbers[i+1]-numbers[i]) <= max_step for i in range(len(numbers) -1))

    return (ascending or descending) and valid

sum = 0
with open(filename, 'r') as file:
    for line in file:
        parts=line.strip().split(" ")
        nums = []
        for x in parts:
            nums.append(int(x))
        if check_list(nums, 3):
            sum = sum + 1
            print(nums)
            continue
        else:
            for listc in genMuts(nums):
                if check_list(listc, 3):
                    sum = sum + 1
                    print(nums)
                    break
            

print(sum)