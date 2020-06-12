data = []
count = 0
with open('read.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 == 0:
			print(len(data))
print(line)
print('123' in data)
print(data [0])
print('-------------------')
print(data [1])
print(len(data))	