import random
#done by Ari
flip = True
nums = []
index = 0

while flip == True:
  i = random.randint(1, 20)
  power = random.randint(2, 3)
  num = i ** power
  nums.append(num)
  print(f"Loop {index+1}: {i}^{power} = {num}")
  if (nums[index] % nums[index - 1] == 0) and (index != 0) and (nums[index - 1] != 1):
    flip = False
  else:
    index += 1

nums_sorted = sorted(nums)

# output data
print(f"The largest result is {nums_sorted[-1]}")
print(f"The smallest result is {nums_sorted[0]}")
print(f"{nums[-1]} is divisible by {nums[-2]}.")
print(f"We completed {index+1} loops.")