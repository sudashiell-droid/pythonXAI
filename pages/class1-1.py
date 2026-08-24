print("蘇楚軒")
print("806")
print("不要低頭\n雙下巴會出來")
"""
這多行註解
"""

#這是單行註解
print("Hello, World!")   # print是在終端機顯示文字指令
#  ctrl+? 可以快速註解/取消註解


# 基本型態
print(1)        # int這是整數, -1,0,1,2
print(1.0)      # float這是浮點數
print(1.234)    # float這是浮點數
print("apple")  # str這是字串 "sa57", '1'
print(True)     # bool這是布林值  True/False
print(False)    # bool這是布林值  True/False


# 變數
a = 10          # 新增一個儲空間並取名為a, "="的功能是將右邊的值10存入左邊的a
print(a)        # 在終端機顯示a所的值
a = "apple"     # 將a的值改為"apple"
print(a)        # 在終端機顯示a所存的值


# 運算子
print(1+1)      #  加法
print(1-1)      #  減法
print(1*1)      #  乘法
print(1/1)      #  除法
print(1%1)      #  取餘數
print(1**1)     #  次方
print(1//1)     #  取商


# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減


#  字串運算
print("apple" + "pen")  # 字串相加
print("apple" * 3)      # 字串相乘


num = 30
item = "書" 
print(f"一本{item}賣{num}元")


#  字串格式化
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")  # f-string
#  可以將變數或其他型態的資料放到f字串裡面的{}，這樣就可以在字串中顯示


print(len("apple"))  # len()是一個函式，可以計算字串的長度
print(len("，"))     # len()是一個函式，可以計算字串的長度
# type()  # 可以查看變數的型態
print(type(1))       #  <class 'int'>
print(type(1.0))     #  <class 'float'>
print(type("apple")) #  <class 'str'>
print(type(True))    #  <class 'bool'>

# 型態轉換
print(int(1.0))      #  float轉int
print(float(1))      #  int轉float
print(str(1))        #  int轉str
print(bool(1))       #  int轉bool
print(int(1.234))    #  float轉int
print(float("1.234"))#  str轉float
print(str(1.234))    #  float轉str
print(bool(1.234))   #  float轉bool
#  print(int("hello"))  # 這行會報錯，因為字串裡面如果有非數字的字元，無法轉換成數字