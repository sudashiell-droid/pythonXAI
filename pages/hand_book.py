import streamlit as st 

with st.expander("class1 課堂筆記"):
    st.write(
        """
# 🐍 Python 入門筆記：國小生也看得懂！

今天我們學了很多 Python 的基本指令。你可以把 **Python 想成一種和電腦溝通的語言**，我們寫指令告訴電腦要做什麼，電腦就會照著執行！

---

## 1. `print()`：叫電腦把東西顯示出來

`print()` 就像對電腦說：「把這個東西秀出來！」

```python
print("蘇楚軒")
print("806")
print("Hello, World!")
```

畫面上就會顯示：

```text
蘇楚軒
806
Hello, World!
```

### `\n` 是換行

```python
print("不要低頭\n雙下巴會出來")
```

會顯示：

```text
不要低頭
雙下巴會出來
```

`\n` 的意思就是「換到下一行」。

---

# 2. 註解：寫給人看的小提醒

有些文字我們只是想提醒自己，不想讓 Python 執行，這時候可以使用「註解」。

### 單行註解：`#`

```python
# 這是單行註解
print("Hello")
```

Python 看到 `#` 後面的文字，就會先忽略它。

### 多行註解：三個引號

```python
\"""
這是多行註解
可以寫很多行
\"""
```

💡 小技巧：有些程式編輯器可以按 **Ctrl + ?**，快速註解或取消註解。

---

# 3. Python 的基本資料種類

Python 裡面的資料有不同種類，就像玩具可以分成汽車、積木、娃娃一樣。

## 🔢 `int`：整數

沒有小數點的數字。

```python
print(1)
print(-1)
print(0)
```

例如：

```text
-1、0、1、2、100
```

---

## 🔸 `float`：浮點數

有小數點的數字。

```python
print(1.0)
print(1.234)
```

例如：

```text
3.14
0.5
100.0
```

---

## 📝 `str`：字串

文字就是字串，通常要用引號包起來。

```python
print("apple")
print("蘋果")
print("123")
```

注意：

```python
123
```

是數字。

但是：

```python
"123"
```

是文字！

---

## 👍👎 `bool`：布林值

布林值只有兩種：

```python
True
False
```

意思是：

* `True` → 真、對、是
* `False` → 假、錯、不是

例如：

```python
print(True)
print(False)
```

---

# 4. 變數：幫資料取名字

可以把「變數」想成一個**有名字的盒子**。

```python
a = 10
```

意思是：

> 建立一個叫做 `a` 的盒子，裡面放入 `10`。

```python
print(a)
```

畫面會顯示：

```text
10
```

盒子裡面的東西也可以換掉：

```python
a = "apple"
print(a)
```

現在會顯示：

```text
apple
```

### `=` 的意思

在 Python 裡：

```python
a = 10
```

不是在問「a 等於 10 嗎？」

而是：

> 把右邊的 `10` 放進左邊叫做 `a` 的變數裡。

---

# 5. 數學運算子

Python 可以幫我們算數學！

| 指令   | 意思  |
| ---- | --- |
| `+`  | 加法  |
| `-`  | 減法  |
| `*`  | 乘法  |
| `/`  | 除法  |
| `%`  | 取餘數 |
| `**` | 次方  |
| `//` | 取商  |

例如：

```python
print(1 + 1)
print(5 - 2)
print(3 * 4)
print(10 / 2)
```

## `%`：取餘數

```python
print(10 % 3)
```

答案是：

```text
1
```

因為：

> 10 ÷ 3 = 3，剩下 1

---

## `**`：次方

```python
print(2 ** 3)
```

意思是：

> 2 × 2 × 2

答案是：

```text
8
```

---

## `//`：取商

```python
print(10 // 3)
```

答案是：

```text
3
```

只取整數的商，不要小數。

---

# 6. 運算的優先順序

Python 算數學時，也有先後順序！

1. `()` 括號
2. `**` 次方
3. `*`、`/`、`//`、`%`
4. `+`、`-`

例如：

```python
print(1 + 2 * 3)
```

會先算：

```text
2 × 3 = 6
1 + 6 = 7
```

所以答案是：

```text
7
```

如果想要先算加法，可以加括號：

```python
print((1 + 2) * 3)
```

答案就是：

```text
9
```

---

# 7. 字串也可以運算

## 字串相加

```python
print("apple" + "pen")
```

結果：

```text
applepen
```

---

## 字串重複

```python
print("apple" * 3)
```

結果：

```text
appleappleapple
```

---

# 8. f-string：把變數放進文字裡

假設：

```python
num = 30
item = "書"
```

我們可以這樣寫：

```python
print(f"一本{item}賣{num}元")
```

結果：

```text
一本書賣30元
```

重點是：

* 前面要加 `f`
* 變數放在 `{}` 裡面

例如：

```python
name = "apple"
age = 18

print(f"Hello, my name is {name}, I'm {age} years old.")
```

Python 會把 `{name}` 和 `{age}` 裡的內容換成真正的資料。

---

# 9. `len()`：計算長度

`len()` 可以計算字串有幾個字。

```python
print(len("apple"))
```

答案：

```text
5
```

因為 `apple` 有 5 個英文字母。

中文字也可以：

```python
print(len("，"))
```

答案是：

```text
1
```

---

# 10. `type()`：查看資料的種類

如果不知道一個資料是什麼類型，可以使用 `type()`。

```python
print(type(1))
print(type(1.0))
print(type("apple"))
print(type(True))
```

分別會知道它們是：

* `int` → 整數
* `float` → 小數
* `str` → 字串
* `bool` → 布林值

可以把 `type()` 想成：

> 「這個東西到底是什麼種類？」

---

# 11. 型態轉換：幫資料換種類

有時候我們需要把資料從一種類型變成另一種類型。

## 變成整數：`int()`

```python
print(int(1.0))
```

結果：

```text
1
```

```python
print(int(1.234))
```

結果：

```text
1
```

⚠️ `int()` 轉換小數時，小數部分會被去掉。

---

## 變成小數：`float()`

```python
print(float(1))
```

結果：

```text
1.0
```

---

## 變成文字：`str()`

```python
print(str(1))
```

把數字 `1` 變成文字 `"1"`。

---

## 變成布林值：`bool()`

```python
print(bool(1))
```

結果：

```text
True
```

---

## ⚠️ 不是所有文字都能變成數字

這樣可以：

```python
print(float("1.234"))
```

但是：

```python
int("hello")
```

會發生錯誤！

因為 `"hello"` 不是數字。

---

# 12. `input()`：讓使用者輸入資料

以前我們都是直接把資料寫在程式裡，但是 `input()` 可以讓使用者自己輸入！

```python
print("輸入開始")

a = input("請輸入一些文字: ")

print("輸入結束")
print(a)
```

程式會先顯示：

```text
請輸入一些文字:
```

然後等待使用者輸入。

---

## 很重要：`input()` 輸入的東西預設都是 `str`

例如使用者輸入：

```text
20
```

雖然看起來是數字，但 Python 會把它當成：

```python
"20"
```

也就是文字。

所以如果要拿來做數學，可以轉成整數：

```python
a = input("請輸入數字: ")
print(int(a) + 10)
```

或者直接這樣寫：

```python
a = int(input("請輸入數字: "))
```

---

# 13. 小練習：計算圓形面積

```python
a = int(input("半徑長度?"))
print(a**2 * 3.14)
```

程式會：

### 第一步：詢問半徑

```text
半徑長度?
```

### 第二步：把輸入內容變成整數

```python
int(input(...))
```

### 第三步：計算

公式是：

> 圓面積 = 半徑 × 半徑 × π

Python 寫法：

```python
a**2 * 3.14
```

---

# 14. Streamlit：把 Python 程式做成網頁

最後我們學到了 **Streamlit**！

Streamlit 可以幫我們用 Python 製作簡單的網頁。

首先要先：

```python
import streamlit as st
```

意思是：

> 載入 Streamlit，並且幫它取一個簡短的名字叫 `st`。

之後就可以使用：

```python
st.title()
st.write()
st.text()
st.markdown()
```

---

## `st.title()`：顯示大標題

```python
st.title("這是標題")
```

網頁上會出現一個大大的標題。

---

## `st.write()`：顯示各種內容

```python
st.write("Hello!")
```

`st.write()` 很方便，可以顯示：

* 文字
* 數字
* Markdown
* 表格
* 其他資料

---

## `st.text()`：顯示純文字

```python
st.text("這是一段純文字")
```

`st.text()` 比較單純，主要用來顯示普通文字。

---

# 15. `st.markdown()`：使用 Markdown 美化文字

Markdown 是一種簡單的文字排版方法。

例如：

```python
st.markdown(\"""
# 最大標題
## 第二大標題
### 第三大標題
\""")
```

## 標題大小

```text
# 最大標題
## 第二大標題
### 第三大標題
#### 第四大標題
##### 第五大標題
###### 第六大標題
```

`#` 越少，標題越大。

---

## 粗體

```markdown
**粗體文字**
```

顯示成：

**粗體文字**

## 斜體

```markdown
*斜體文字*
```

顯示成：

*斜體文字*

## 項目清單

```markdown
- 第一個項目
- 第二個項目
- 第三個項目
```

會變成：

* 第一個項目
* 第二個項目
* 第三個項目

## 程式碼

可以使用三個反引號：

````markdown
```python
print("Hello World!")
```
````

就可以漂亮地顯示 Python 程式碼。

---

# 🎯 今天學習重點總整理

```text
print()       → 顯示內容
#             → 單行註解
\""" \"""       → 多行註解

int           → 整數
float         → 小數
str           → 文字
bool          → True 或 False

變數          → 幫資料取名字
=             → 把右邊的資料存到左邊

+             → 加
-             → 減
*             → 乘
/             → 除
%             → 取餘數
**            → 次方
//            → 取商

len()         → 計算長度
type()        → 查看資料型態

int()         → 轉成整數
float()       → 轉成小數
str()         → 轉成文字
bool()        → 轉成布林值

input()       → 讓使用者輸入資料

f"文字{變數}" → 把變數放進文字裡

st.title()    → Streamlit 大標題
st.write()    → 顯示內容
st.text()     → 顯示純文字
st.markdown() → 使用 Markdown 排版
```

🌟 **一句話記住今天的內容：Python 可以幫我們顯示文字、儲存資料、計算數學、接收使用者輸入，還可以用 Streamlit 製作網頁！**

下一步可以試著把這些內容做成「小測驗版筆記」，用題目和答案來複習，會更容易記住。

      """
    )
with st.expander("class2 課堂筆記"):
    st.write(
        """
# 🐍 Python 學習筆記（二）：比較、判斷與 Streamlit 互動網頁

今天我們學到的內容，可以把它想成：**讓電腦學會「比較」、「思考」和「做決定」！**

例如我們可以問電腦：

> 「這個數字有沒有比較大？」
> 「兩個東西是不是一樣？」
> 「如果考試 90 分以上，要給 A 級！」
> 「如果按下按鈕，就放氣球！」

這些就是今天的重點！

---

# 一、比較運算子：比較兩個東西

比較運算子就像是在問問題，最後的答案只有兩種：

* `True` → 是、正確
* `False` → 不是、錯誤

> 💡 比較資料時，要注意資料的型態是否適合拿來比較。

| 運算子  | 意思      | 例子       |
| ---- | ------- | -------- |
| `==` | 是否相等    | `1 == 1` |
| `!=` | 是否不相等   | `1 != 1` |
| `>`  | 是否大於    | `2 > 1`  |
| `<`  | 是否小於    | `1 < 2`  |
| `>=` | 是否大於或等於 | `2 >= 2` |
| `<=` | 是否小於或等於 | `1 <= 2` |

---

## `==`：兩邊一樣嗎？

```python id="zxh2gr"
print(1 == 1)
```

結果：

```text id="9x4csl"
True
```

因為 1 和 1 是一樣的。

---

## `!=`：兩邊不一樣嗎？

```python id="j47jcf"
print(1 != 1)
```

結果：

```text id="lgicrr"
False
```

因為兩邊明明一樣，所以「不一樣」這件事是錯的。

---

## `>`：左邊比較大嗎？

```python id="xly9w7"
print(1 > 1)
```

結果：

```text id="i3pbjz"
False
```

因為 1 沒有比 1 大。

---

## `<`：左邊比較小嗎？

```python id="v9ywxd"
print(1 < 1)
```

結果：

```text id="jsyq8v"
False
```

因為 1 也沒有比 1 小。

---

## `>=`：大於或等於

```python id="6yq0f0"
print(1 >= 1)
```

結果：

```text id="pr0qnc"
True
```

因為兩邊一樣大也可以！

---

## `<=`：小於或等於

```python id="k0atye"
print(1 <= 1)
```

結果：

```text id="cf97b1"
True
```

因為兩邊一樣小也符合條件。

---

# 二、邏輯運算子：一次判斷很多條件

有時候一個條件不夠，我們需要一次判斷兩個或更多條件。

這時候可以使用：

* `and`
* `or`
* `not`

---

# 三、`and`：而且、同時都要成立

`and` 可以想成：

> 「這個也要對，而且那個也要對！」

只要有一個是 `False`，最後就是 `False`。

| 條件一   | 條件二   | 結果    |
| ----- | ----- | ----- |
| True  | True  | True  |
| True  | False | False |
| False | True  | False |
| False | False | False |

例如：

```python id="n7ej1r"
print(True and True)
print(True and False)
print(False and True)
print(False and False)
```

### 生活中的例子

> 「今天要考 100 分，而且要完成作業，才可以得到獎勵。」

兩件事情都完成才行！

---

# 四、`or`：或者，只要有一個成立

`or` 可以想成：

> 「這個可以，或那個可以！」

只要有一個 `True`，結果就是 `True`。

| 條件一   | 條件二   | 結果    |
| ----- | ----- | ----- |
| True  | True  | True  |
| True  | False | True  |
| False | True  | True  |
| False | False | False |

例如：

```python id="umc2zx"
print(True or True)
print(True or False)
print(False or True)
print(False or False)
```

⚠️ 要特別注意：

```python id="tf5txb"
print(True or False)
```

答案是：

```text id="jdttvv"
True
```

因為只要其中一個是 `True` 就可以了。

---

# 五、`not`：把答案反過來

`not` 就像「不是」。

```python id="3pygx4"
print(not True)
```

結果：

```text id="wsj4nc"
False
```

```python id="yv3rbh"
print(not False)
```

結果：

```text id="uiv0fv"
True
```

可以記成：

> `True` 遇到 `not` → 變成 `False`
> `False` 遇到 `not` → 變成 `True`

---

# 六、邏輯運算的順序

當 `and` 和 `or` 同時出現時，Python 也有自己的計算順序。

例如：

```python id="bxaczi"
print(True and False or True)
```

可以把它想成：

```python id="4u9e9p"
(True and False) or True
```

先算：

```text id="a3aav4"
True and False → False
False or True → True
```

所以答案是：

```text id="v9hx9w"
True
```

💡 如果條件很複雜，可以多加括號 `()`，讓程式更容易看懂！

---

# 七、`if`：如果條件成立，就做事情

`if` 就像是在告訴電腦：

> 「如果這件事情是真的，就做某件事！」

例如：

```python id="p8q32x"
score = 100

if score >= 60:
    print("及格！")
```

因為 `100 >= 60` 是 `True`，所以會顯示：

```text id="slcmm5"
及格！
```

⚠️ Python 的 `if` 後面要加冒號 `:`，而且下面的程式碼要縮排。

---

# 八、`if...elif...else`：讓電腦做選擇

如果有很多種不同情況，可以使用：

```python id="zn1a2z"
if 條件:
    做事情
elif 另一個條件:
    做另一件事情
else:
    前面都不符合時要做的事情
```

可以把它想成：

> 如果第一個條件成立，就做第一件事。
> 不然的話，再看看第二個條件。
> 如果前面都不符合，就做最後一件事。

---

# 九、密碼檢查程式 🔐

我們今天做了一個「密碼門」！

```python id="n5hv6l"
password = input("請輸入密碼：")

if password == "1234":
    print("歡迎Jeffrey")
elif password == "5678":
    print("歡迎Tim")
elif password == "0000":
    print("歡迎Chioe")
else:
    print("密碼錯誤👎(ㆆ_ㆆ)👎")
```

程式會這樣思考：

```text id="z1nplm"
輸入密碼
    ↓
是 1234 嗎？
    ↓ 是
歡迎 Jeffrey

    ↓ 不是
是 5678 嗎？
    ↓ 是
歡迎 Tim

    ↓ 不是
是 0000 嗎？
    ↓ 是
歡迎 Chioe

    ↓ 都不是
密碼錯誤！
```

---

# 十、很多個 `if` 和 `if...elif...else` 有什麼不同？

假設我們寫：

```python id="bdl9is"
if 條件1:
    做事情1

if 條件2:
    做事情2

if 條件3:
    做事情3
```

這代表每一個 `if` 都會自己檢查一次。

但是：

```python id="9lzcnp"
if 條件1:
    做事情1
elif 條件2:
    做事情2
elif 條件3:
    做事情3
else:
    做最後一件事情
```

代表：

> 找到符合的答案後，後面的 `elif` 就不用再執行了。

所以當我們是在做「很多選一個」的判斷時，`if...elif...else` 通常比較適合，也可以讓程式更清楚。

---

# 十一、Streamlit：`st.number_input()`

今天我們還學到了讓使用者在網頁上輸入數字！

先匯入 Streamlit：

```python id="xxpn5w"
import streamlit as st
```

然後使用：

```python id="cbkqzw"
number = st.number_input(
    "請輸入一個數字",
    min_value=0,
    max_value=100,
    step=1
)
```

意思是：

* `"請輸入一個數字"` → 顯示提示文字
* `min_value=0` → 最小可以輸入 0
* `max_value=100` → 最大可以輸入 100
* `step=1` → 每次增加或減少 1

---

# 十二、在網頁上顯示使用者輸入的數字

```python id="chqgqb"
st.markdown(f"你輸入的數字是：{number}")
```

如果使用者輸入：

```text id="5l0fzb"
50
```

網頁就會顯示：

> 你輸入的數字是：50

這裡使用了我們之前學過的 **f-string**！

---

# 十三、做一個成績等級判斷器 📚

```python id="w6sc3p"
score = st.number_input(
    "請輸入你的分數",
    min_value=0,
    max_value=100,
    step=1
)

if score >= 90:
    st.write("你的等級是 🫅A")
elif score >= 80:
    st.write("你的等級是 🕵️B")
elif score >= 70:
    st.write("你的等級是 👷C")
elif score >= 60:
    st.write("你的等級是 👩‍🦽D")
else:
    st.write("你的等級是 F")
```

電腦會這樣判斷：

| 分數     | 等級 |
| ------ | -- |
| 90～100 | A  |
| 80～89  | B  |
| 70～79  | C  |
| 60～69  | D  |
| 0～59   | F  |

例如輸入：

```text id="uvkz6x"
85
```

電腦會想：

1. 85 有沒有大於等於 90？❌
2. 85 有沒有大於等於 80？✅
3. 顯示 B！

---

# 十四、`st.button()`：製作按鈕 🔘

在 Streamlit 網頁上，可以使用：

```python id="tvr1ph"
st.button("按我一下")
```

這樣網頁上就會出現一個按鈕。

如果使用者點擊按鈕，`st.button()` 會得到：

```python id="jpdnqr"
True
```

沒有點擊時，通常就是：

```python id="1srq6n"
False
```

---

# 十五、按下按鈕後放氣球 🎈

```python id="qckr0g"
if st.button("按我一下", key="balloons"):
    st.balloons()
```

意思是：

> 如果使用者按下按鈕，就放出氣球！

---

# 十六、按下按鈕後下雪 ❄️

```python id="sdvw9s"
if st.button("按我一下", key="snow"):
    st.snow()
```

意思是：

> 如果使用者按下按鈕，就開始下雪！

---

# 十七、`key`：幫按鈕取身分證名字

如果網頁上有很多按鈕，可以幫它們設定不同的 `key`。

例如：

```python id="9nt3er"
st.button("按我一下", key="button1")
```

另一個：

```python id="t4k2xy"
st.button("按我一下", key="snow")
```

雖然兩個按鈕顯示的文字可以一樣，但 `key` 要用不同的名字，Python 才比較容易分辨它們。

---

# 🎯 今天的重點總整理

| 指令                  | 功能                 |
| ------------------- | ------------------ |
| `==`                | 是否相等               |
| `!=`                | 是否不相等              |
| `>`                 | 大於                 |
| `<`                 | 小於                 |
| `>=`                | 大於或等於              |
| `<=`                | 小於或等於              |
| `and`               | 全部條件都要成立           |
| `or`                | 至少一個條件成立           |
| `not`               | 把 True 和 False 反過來 |
| `if`                | 如果條件成立             |
| `elif`              | 不然如果               |
| `else`              | 前面都不成立             |
| `st.number_input()` | 在網頁輸入數字            |
| `st.markdown()`     | 顯示 Markdown 文字     |
| `st.write()`        | 顯示內容               |
| `st.button()`       | 建立按鈕               |
| `st.balloons()`     | 放氣球                |
| `st.snow()`         | 下雪                 |

## 🌟 今天最重要的觀念

**比較運算子可以讓 Python 判斷對不對，邏輯運算子可以把很多條件放在一起，而 `if`、`elif`、`else` 可以讓電腦根據不同情況做不同的事情。**

💡 下一步可以試著自己做一個「猜數字遊戲」或「成績判斷器」，把 `input()`、比較運算子、`if...elif...else` 和 Streamlit 按鈕全部一起練習。

      """
    )
with st.expander("class3 課堂筆記"):
    st.write(
        """

      """
    )
with st.expander("class4 課堂筆記"):
    st.write(
        """

      """
    )
with st.expander("class5 課堂筆記"):
    st.write(
        """

      """
    )