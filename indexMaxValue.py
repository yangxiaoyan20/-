 #coding = utf-8
import sys
#滴滴打车2017年秋招笔试题  （2017-08-26 15:00-17:00）
#输入一串数如11 -7 17 -32 23 45
#输入一个数index，值范围在0与一串数的长度之间
#输出：对这一串数排序，输出第index大的值
if __name__ == "__main__":
	n = list(sys.stdin.readline().strip().split())
	sumMax=n[0]
	for i in xrange(len(n)):
		sumMax2=0
		for j in xrange(i,len(n)):
			sumMax2=int(sumMax2)+int(n[j])
			if(sumMax<sumMax2):
				sumMax=sumMax2
				
	print("%s" %sumMax)
