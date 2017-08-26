# -*-coding:utf-8 -*-
#code=utf-8
#code:utf-8
import sys
#阿里巴巴2017年测试开发工程师编程题
#第一个人a与第二个b是朋友，值表示为M[0][1]=1
#第一个人a与自身是朋友，值表示为M[0][0]=1
#第一个人a与第三个人c不是朋友，值表示M[0][2]=0
#若第二个人b与第四个人d是朋友，则值表示M[1][3]=1 因a和b、b和d是直接朋友，故a和d是间接朋友
#直接朋友或间接朋友可以组队，求可以分成几组
#输入：
     #输入二维数组的行数 如6
     #输入二维数组的列数 （其实行数和列数是相同的，因为关系是一一对应的，并且二位数组是对称数组）
     #输入第一行人对应的关系 如1 1 0 0 0 0
	 #输入第二行人对应的关系 如1 1 0 0 0 0
#输出：
      #输出分的组数
#例子
#[[1,1,0],[1,1,0],[0,0,1]]  输出：2
#[[1,1,0,0,0,0],[1,1,0,0,0,0],[0,0,1,0, 0, 0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,1,0,1]]输出：4
def CaculatePeopleGroup():
	res=0
	data_row= input()     #raw_input()输入二维数组的行数
	data_col = input()  #raw_input()输入二维数组的列数
	dataList=[]  ##[[1,1,0,0],[1,1,1,0],[0,1,0,1],[0,0,0,1]]
	resList=[]
	if(data_row==data_col):
		for i in xrange(data_row):#循环输入行数次 0,1,2，data_row-1停
			data_i=list(sys.stdin.readline().strip().split()) #1,1,0,0       # 1 1 0 0 0 0     
			dataList.append(data_i)  #如何输入1 1 0 0 0 0
			#print ("value:%s data_i:%s" %(dataList,data_i))
			stmList=[]
			for col in xrange(i,len(data_i)):
				#print("data_i[i]:%s data_i[col]):%s" % (data_i[i], data_i[col]))
				if(data_i[i]==data_i[col]) and (int(data_i[col])==1) :
					stmList.append(col+1)   #得到和自己是朋友的有哪些人
					#print("stmList:%s col:%s" %(stmList,col))
			resList.append(stmList)  #[[1,2],[2],[3],[4,6],[5],[6]] 第一个list表示1只与2是朋友，第二list表示2没有与2后面的人是朋友，第四个list表示4与后面的6是朋友
		#print("resList:%s" % resList)
	else:
		print "Error:输入的数据有问题"
	delList=[]
	for i in xrange(len(resList)):  #len(resList)为6  index为0 resList[index]为[1,2]
		#print ("reslist[i]:%s len(resList):%d  resList:%s" %(resList[i],len(resList),resList))
		for j in xrange(i+1,len(resList)):#循环resList[index]后面的值
				#print ("reslist[j]:%s len(resList):%d  resList:%s  j:%s" % (resList[j], len(resList),resList,j))
				for i_i in xrange(len(resList[i])):
					for j_j in xrange(len(resList[j])):
						#print("resList[%s][%s]:%s resList[%s][%s]):%s" % (i,i_i,resList[i][i_i],j,j_j, resList[j][j_j]))
						if(resList[i][i_i]==resList[j][j_j]):
							if(len(resList[j])>1):
								resList[i].append(resList[j])
							#print resList[j]  #打印有相同朋友
							delList.append(resList[j]) #删除后面重复的数
							break
	for del_i in delList:
		if(del_i in resList):
			#print del_i
			resList.remove(del_i)
	#print("resList222222222:%s" % resList)
	res=len(resList)
	return res

if __name__ == "__main__":
	result=CaculatePeopleGroup()
	print str(result)+"\n"
