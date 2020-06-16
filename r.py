data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 5000 == 0:
			print(count)
print("檔案讀取完畢!總共有", len(data), "筆資料!") 

# 計算平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print("每筆留言的平均長度是", sum_len / len(data), "個字!")

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆長度小於100')
print(new[0])

good = [d for d in data if 'good' in d]
damn = [d for d in data if 'damn' in d]

print('有good的留言共', len(good), '筆')
print('有damn的留言共', len(damn), '筆')
print(damn[2])