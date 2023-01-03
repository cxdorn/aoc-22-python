f = open("input.in")
reading = True
nums = []
moves = {}
n = 0
key = 811589153


while reading:
	line = f.readline().strip()
	if line == '':
		reading = False
		break
	moves[n] = int(line)*key
	nums += [n]
	n += 1

m = len(nums)

for p in range(10):
	print('mix', p)
	for i in range(m):
		k = nums.index(i)
		new_index = (k + moves[i]) % (m - 1)
		del nums[k]
		nums.insert(new_index, i)

res = [moves[x] for x in nums]
j = res.index(0)
print(res[(j + 1000) % m] + res[(j + 2000) % m] + res[(j + 3000) % m])
	
