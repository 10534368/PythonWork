nums = list(input())
cnt = int(input())
n, j, i = len(nums), cnt, 0
while j > 0 and i < n - 1:
    if nums[i] >= nums[i + 1]:
        i += 1
    else:
        nums.pop(i)
        j -= 1
        n -= 1
        i = i - 1 if i > 0 else 0
if j > 0:
    nums = nums[:-j]
print(''.join(nums))
