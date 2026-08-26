# list列表
# 建立列表
a = [10,20,30,]

# 建立空列表
b = []

# 列表可以儲存任何資料型態
c = [10,"apple",True,'hello','1000']


me = ["張三","李四","王五","蔡六","陳七","吳八","黃九","周十",True ,False,67,]


fruits=['apple','banana','orange']
# 取單一值
print(fruits[1]) # banana
# 印出整個列表
print(fruits) # ['apple', 'banana', 'orange']

a=[90,80,70,50,20]
print(a[0]) 


a=[1,2,3,4]
a.append(5) # append() # 將元素新增到列表最前面
print(a)

number=[2,4,6,8]
number.remove(4) # remove是指定元素刪除
print(number) # [2,6,8]

# sort:將list中的元素進行排序，預設是由小到大(升序排列)
# 注意:這個方法會直接修改原本的list，不會產生新的list
L=[1,3,2,4,5]
L.sort()
print(L)

# list 取長度，也就是list中有幾個元素，不是index的最大值
L=[1,2,3,'a','b','c']
print(len(L))  #6

# 使用pop，可以移除指定的index的元素
L=['a','b','c','d','a']
L.pop(0)  # 移除index 0的元素
# 代表pop會移除指定的index的元素
# 如果沒有指定index，就會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)

# list 走訪元素
# 可以透過取得index的方式來找到list中的資料
# 也可以直接把list當作一個範圍來取得資料
# 這兩種方法都可以，但是看使用的情境是否會需要index來決定要用哪一種方式
L=[1,2,3,'a','b','c']
for i in range(0,len(L),2):
    print(L[i])

for i in L:
    print(i)

L=['a','b','c','d','a']
# 如果想要移除所有符合的元素，可以使用迴圈
for i in L:
    if i=='a':
        L.remove(i)