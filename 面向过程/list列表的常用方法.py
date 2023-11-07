# 列表(list)
name_list=['张楚岚',123,True]
print(name_list)
print(type(name_list))
##嵌套列表
my_list=[[1,2,3],[4,5,6],[7,8,9,]]
print(my_list)
print(type(my_list))
##列表的下表索引 +为从第一位开始为0/——从最后一个为-1
me_list=[[1,2,3],[4,5,6],[7,8,9,]]
print(me_list[2])
print(me_list[-2])
print(me_list[1][1])
print(type(me_list))
###列表的查询方法
my_sqlst=['a','b','c','d']
index=my_sqlst.index('c')
print({index})
####查询不存在  ValueError: 'hello' is not in list
# my_sqlst=['a','b','c','d']
# index=my_sqlst.index('hello')
# print({index})
#列表的修改功能
my_sqlst[0]='123'
print(my_sqlst)
#列表元素插入/追加元素(追加元素，在尾部加入)
my_sqlst.insert(0,'abc')
print(my_sqlst)
my_sqlst.append('zcl')
print(my_sqlst)
##在列表尾部追加一批新元素
mylist2=[1,2,3]
my_sqlst.extend(mylist2)
print(my_sqlst)
#删除元素
my_sqlst.remove('zcl')
print(my_sqlst)
#指定下标元素的删除
my_sqlst.pop(1)
print(my_sqlst)
#删除指定的匹配值
mysilt=['abc', '123', 'b', 'c', 'd', 1, 2, 3]
mysilt.remove('b')
print(mysilt)
#清空列表
mysilt.clear()
print(mysilt)
#统计列表内的某个元素个数
mysilt=['abc', '123', '123','123','123','123','b', 'c', 'd', 1, 2, 3]
count=mysilt.count("123")
print(count)
#统计列表中所以元素的个数
mysilt=['abc', '123', '123','123','123','123','b', 'c', 'd', 1, 2, 3]
count=len(mysilt)
print(count)
