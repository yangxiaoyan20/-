#coding = utf-8
import sys
#滴滴打车2017年秋招编程题  2017/08/26 15:00-17:00
#输入一串数字如11 -7 17 -32 23 45，求子串和最大的值是多少
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
