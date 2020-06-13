data = []
count = 0

with open('read.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 == 0:
			print(len(data))

print('檔案讀取完了， 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
average = (sum_len/len(data))
print('平均有', average, '個字元')


new = []
for d in data:
	if len(d) < 100:
		new.append(d.strip())
print('一共有', len(new), '筆留言 < 100 個字元')