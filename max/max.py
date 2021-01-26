nums = [8, 9, 7, 10, 8]

max = nums[0]

for x in range(1,5):
    if max < nums[x]:
            max = nums[x]
print(max)
