# -*-coding:utf-8 -*-
#code=utf-8
#code:utf-8
#-*- coding: UTF-8 -*-
# 森林举行运动会，小伙伴们身上每个都印着一个字符标记，排成一列，委员会要挑出每列里相邻小伙伴身上没有重复字符标记的，最多能挑出几个？
# 比如：小伙伴们的字符标记串起来是“ccccccbc” 那相邻的小伙伴身上没有重复的字符标记是cb或者bc，那这个人数就是2
# 已输入字数: 225 / 10000   运行 编程说明 -
# 编译器版本: gcc 4.8.4
# 请使用标准输入输出(stdin，stdout) ；请把所有程序写在一个文件里，勿使用已禁用图形、文件、网络、系统相关的头文件和操作，如sys/stat.h , unistd.h , curl/curl.h , process.h
# 时间限制: 3S (C/C++以外的语言为: 5 S)   内存限制: 128M (C/C++以外的语言为: 640 M)
# 输入:
# 输入：小伙伴们的字符标记串起来的字符串
# 输出:
# 输出：相邻的小伙伴身上 没有重复的字符标记是cb或者bc，那这个人数就是2
# 输入范例:
# “ccccccbc”
# 输出范例:
# 2
def lengthOfLongestSubstring(str):
	arr=list(str)  #将字符串转换成list格式
	myList=[]
	#print arr
	count=0
	for index in range(len(arr)):
		#print ("index:%s value:%s" %(index,arr[index])) 
		if((int(index)+1)<len(arr)):
			myList.append(arr[index]+arr[index+1])     #将arr的字母组成相邻字母的myList
			#print ("arr[%s]+arr[%s+1]:%s" %(index,index,arr[index]+arr[index+1]) )
	#print myList
	myset=set(myList)    #set类型是没有重复项
	for i in myset:
		#print(i,myList.count(i))
		if(myList.count(i)==1):
			count=count+1
	return count
myStr=input()
print lengthOfLongestSubstring(myStr)
