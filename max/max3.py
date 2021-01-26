nums = [6, 8, 9, 7]

max = nums[0]

for x in range(1,4):
    if max < nums[x]:
            max = nums[x]
print(max)
