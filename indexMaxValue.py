 #coding = utf-8
import sys
#滴滴打车2017年秋招笔试题  （2017-08-26 15:00-17:00）
#输入一串数如11 -7 17 -32 23 45
#输入一个数index，值范围在0与一串数的长度之间
#输出：对这一串数排序，输出第index大的值
if __name__ == "__main__":
	myList=map(int,list(sys.stdin.readline().strip().split()))
	resList=[]
	lens=len(myList)
	index=int(sys.stdin.readline().strip())
	for i in range(lens):
		maxNum=max(myList)
		resList.append(maxNum)
		if(i==(index-1)):
			print maxNum
		myList.remove(maxNum)
	#myList.sort()
