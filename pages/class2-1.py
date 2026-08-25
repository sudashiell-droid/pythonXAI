#  比較運算子，只能同樣類行做比較
print(1==1) #   True
print(1!=1) #   False
print(1>1)  #   False
print(1<1)  #   False
print(1>=1) #   True
print(1<=1) #   True


#  邏輯運算子
#  and 運算子，只要有一個條件為False，結果就是False
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# or 運算子，只要有一個條件為True結果就是True
print(True or True)   # True
print(True or False)  # False
print(False or True)  # False
print(False or False) # False

# not 運算子，只要條件為True結果就是False，為False結果就是True
print(not True)  # False
print(not False) # True

#  邏輯運算子的優先順序
print(True and False or True) # True
print(True and (False or True)) # True
print(True and (False or True) and False) # True
print(True and (False or True) and False or True) # True


# 密碼門檢查
password = input("請輸入密碼：")
if password == "1234":
    print("歡迎Jeffrey")
elif password == "5678":
    print("歡迎Tim")
elif password == "0000":
    print("歡迎Chioe")
else:
    print("密碼錯誤👎(ㆆ_ㆆ)👎")

# 連續使用if跟使用if elif else的差別
# elif可以排除前面有判斷過的條件，所以縮短判斷條件的複雜度，也節省了時間
# 但是如果是使用多個if 來做獨立判斷，則每個if都會執行一次，所以效率較低