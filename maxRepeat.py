def maxRepeat(dic):
	for i in range(0,len(dic)):
		t = 0
		k = 0
		for key in dic:
			if t < dic.get(key):
				t = dic.get(key)
				k = key
		print(k)
		del dic[k]

def main():
	""" Display Max repeated values in descending order"""
	li = [3, 4, 2, 3, 16, 3, 15, 16, 15, 15, 16, 2, 3]
	li.sort()
	dic = dict()
	while(len(li)):
		temp = li[0]
		count = 0
		while(len(li) and (temp == li[0])):
			li.pop(0)
			count +=1
		#print("val {0} count {1}".format(temp,count))
		dic[temp] = count
	maxRepeat(dic)
	
main()