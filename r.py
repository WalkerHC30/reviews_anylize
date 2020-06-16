data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 5000 == 0:
			print(count)
print("檔案讀取完畢!總共有", len(data), "筆資料!") 

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print("每筆留言的平均長度是", sum_len / len(data), "個字!")