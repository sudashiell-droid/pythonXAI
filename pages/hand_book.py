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
# 🐍 Python 學習筆記（三）：重複做事情、列表與網頁元件

今天我們學到的內容，可以把它想成讓 Python 學會：

> 🔁 重複做事情
> 📦 把很多資料放進一個盒子
> 🌐 製作更有趣的網頁
> 💾 記住網頁上的資料

---

# 一、`for` 迴圈：叫 Python 重複做事情 🔁

「迴圈」的意思就是：**重複做同一件事情**。

例如，我們想要連續印出 5 個數字，如果一個一個寫：

```python
print(0)
print(1)
print(2)
print(3)
print(4)
```

很麻煩！

所以可以使用 `for` 迴圈：

```python
for i in range(5):
    print(i)
```

結果：

```text
0
1
2
3
4
```

---

## `for` 和 `in`

基本格式：

```python
for 變數名稱 in 範圍:
    要重複做的事情
```

例如：

```python
for i in range(5):
    print(i)
```

可以想成：

> 把 `range(5)` 裡面的數字，一個一個拿出來，放進 `i` 裡面，然後執行一次程式。

### `i` 是什麼？

`i` 是「迴圈變數」。

每一次迴圈，`i` 都會拿到不同的資料。

第一次：

```text
i = 0
```

第二次：

```text
i = 1
```

第三次：

```text
i = 2
```

一直到最後。

💡 `i` 只是名字，你也可以取其他名字，例如：

```python
for number in range(5):
    print(number)
```

---

# 二、`range()`：製造一串數字

## `range(5)`

```python
for i in range(5):
    print(i)
```

會產生：

```text
0
1
2
3
4
```

⚠️ **不包含 5！**

可以記住：

> `range(5)` 從 0 開始，到 5 前面停止。

---

## `range(1, 5)`：設定開始和結束

```python
for i in range(1, 5):
    print(i)
```

結果：

```text
1
2
3
4
```

一樣要記住：

> 最後面的數字不會包含進去！

---

## `range(1, 10, 2)`：設定間隔

```python
for i in range(1, 10, 2):
    print(i)
```

結果：

```text
1
3
5
7
9
```

這裡的 `2` 表示：

> 每次增加 2。

---

# 三、迴圈結束後，變數會留下最後的值

看看這段程式：

```python
for i in range(5):
    a = i * 2

print(a)
```

迴圈中的 `i` 會依序是：

```text
0 → 1 → 2 → 3 → 4
```

所以 `a` 會變成：

```text
0 → 2 → 4 → 6 → 8
```

最後一次迴圈結束後：

```python
a = 8
```

因此：

```python
print(a)
```

會顯示：

```text
8
```

---

# 四、數字金字塔 🔺

我們可以把 `for` 迴圈和 Streamlit 結合！

```python
import streamlit as st

st.title("數字金字塔")

i = st.number_input(
    "請輸入一個整數（1-9）",
    min_value=1,
    max_value=9,
    step=1
)

st.write("數字金字塔：")

for j in range(1, i + 1):
    st.write(str(j) * j)
```

假設輸入：

```text
5
```

就會顯示：

```text
1
22
333
4444
55555
```

### 為什麼是 `i + 1`？

因為 `range()` **不包含最後一個數字**。

如果輸入 5：

```python
range(1, 5)
```

只有：

```text
1、2、3、4
```

所以要寫：

```python
range(1, i + 1)
```

才能把 5 也算進去。

---

# 五、`list` 列表：一個盒子裡放很多資料 📦

可以把 `list`（列表）想成一個大盒子，裡面可以放很多東西。

```python
fruits = ["apple", "banana", "orange"]
```

這個列表裡有：

```text
apple
banana
orange
```

---

## 建立列表

```python
a = [10, 20, 30]
```

---

## 建立空列表

```python
b = []
```

這是一個還沒有放任何東西的盒子。

---

## 列表可以放不同種類的資料

```python
c = [10, "apple", True, "hello", "1000"]
```

裡面可以同時放：

* 數字
* 文字
* True / False

---

# 六、列表的編號：`index`

Python 的列表從 **0** 開始編號！

例如：

```python
fruits = ["apple", "banana", "orange"]
```

可以想成：

| 編號 index | 資料     |
| -------- | ------ |
| 0        | apple  |
| 1        | banana |
| 2        | orange |

所以：

```python
print(fruits[1])
```

結果是：

```text
banana
```

因為 `banana` 的編號是 1。

---

# 七、印出整個列表

```python
fruits = ["apple", "banana", "orange"]

print(fruits)
```

結果：

```text
['apple', 'banana', 'orange']
```

---

# 八、`append()`：在列表最後面新增資料 ➕

```python
a = [1, 2, 3, 4]

a.append(5)

print(a)
```

結果：

```text
[1, 2, 3, 4, 5]
```

📌 注意：`append()` 是把新資料加到**列表最後面**。

---

# 九、`remove()`：刪除指定的資料 ❌

```python
number = [2, 4, 6, 8]

number.remove(4)

print(number)
```

結果：

```text
[2, 6, 8]
```

`remove(4)` 的意思是：

> 找到數字 4，然後把它刪掉。

---

# 十、`sort()`：幫列表排序

```python
L = [1, 3, 2, 4, 5]

L.sort()

print(L)
```

結果：

```text
[1, 2, 3, 4, 5]
```

預設是從小排到大。

⚠️ `sort()` 會直接改變原本的列表。

---

# 十一、`len()`：計算列表裡有幾個資料

```python
L = [1, 2, 3, "a", "b", "c"]

print(len(L))
```

結果：

```text
6
```

因為列表裡有 6 個元素。

📌 `len()` 計算的是「有幾個東西」，不是最大編號！

---

# 十二、`pop()`：按照位置刪除資料

```python
L = ["a", "b", "c", "d", "a"]

L.pop(0)
```

這代表：

> 刪除編號 0 的資料。

也就是刪掉第一個 `"a"`。

如果沒有寫編號：

```python
L.pop()
```

就會刪掉最後一個資料。

---

# 十三、用迴圈讀取列表

有兩種常見的方法！

## 方法一：利用 index

```python
L = [1, 2, 3, "a", "b", "c"]

for i in range(0, len(L), 2):
    print(L[i])
```

這裡的：

```python
range(0, len(L), 2)
```

代表：

> 從 0 開始，每次跳 2 格。

---

## 方法二：直接拿資料

```python
L = [1, 2, 3, "a", "b", "c"]

for i in L:
    print(i)
```

結果：

```text
1
2
3
a
b
c
```

這種方法比較簡單。

---

# 十四、刪除列表中所有符合的資料

例如：

```python
L = ["a", "b", "c", "d", "a"]

for i in L:
    if i == "a":
        L.remove(i)
```

意思是：

> 一個一個檢查列表，如果找到 `"a"`，就把它刪掉。

⚠️ 不過要特別小心：**一邊用 `for` 走訪列表，一邊直接刪除列表裡的資料，某些情況可能會造成漏掉元素。**

初學時可以先知道這個觀念，之後會學到更安全的刪除方法。

---

# 十五、Streamlit 的欄位：`st.columns()` 📰

有時候我們希望網頁上的東西不要全部直直排下來，而是左右排列。

可以使用：

```python
col1, col2 = st.columns(2)
```

這代表建立兩個欄位：

```text
┌──────────┬──────────┐
│   col1   │   col2   │
└──────────┴──────────┘
```

然後可以在不同欄位放不同的東西：

```python
col1.button("按鈕1", key="btn1")
col2.button("按鈕2", key="btn2")
```

---

# 十六、設定欄位寬度比例

可以建立三個欄位：

```python
col1, col2, col3 = st.columns([1, 2, 3])
```

這代表欄位寬度比例是：

```text
col1 : col2 : col3
 1   :  2   :  3
```

所以 `col3` 最大，`col1` 最小。

---

# 十七、`with`：在指定欄位裡放很多東西

```python
col1, col2 = st.columns([1, 2])

with col1:
    st.write("這是 col1")
    st.button("按鈕1", key="btn8")

with col2:
    st.write("這是 col2")
    st.button("按鈕2", key="btn9")
```

可以把 `with col1:` 想成：

> 接下來的東西都放到 col1 裡面！

---

# 十八、按下按鈕後放氣球 🎈

```python
with col1:
    if st.button("按鈕1", key="btn8"):
        st.balloons()

    st.write("這是 col1")
```

意思是：

> 如果按下按鈕，就放氣球！

---

# 十九、`st.text_input()`：文字輸入框 ⌨️

可以讓使用者在網頁上輸入文字：

```python
text = st.text_input(
    "請輸入文字",
    value="這是預設文字"
)
```

這裡：

* `"請輸入文字"` → 輸入框的標題
* `value="這是預設文字"` → 一開始預先放好的文字

然後可以顯示使用者輸入的內容：

```python
st.write(f"你輸入的文字是：{text}")
```

---

# 二十、`st.session_state`：讓網頁記住資料 🧠

Streamlit 的網頁有時候重新執行後，一般變數的內容可能會重新開始。

這時候可以使用：

```python
st.session_state
```

把它想成 Streamlit 的「小記憶盒」。

---

## 第一次先建立資料

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1
```

意思是：

> 如果記憶盒裡還沒有 `ans1`，就建立它，並且設定成 1。

---

## 按一次按鈕就加 1

```python
if st.button("按下去 ans 加 1", key="ans2"):
    st.session_state.ans1 = st.session_state.ans1 + 1
```

如果原本：

```text
ans1 = 1
```

按一次：

```text
ans1 = 2
```

再按一次：

```text
ans1 = 3
```

最後顯示：

```python
st.write(f"ans = {st.session_state.ans1}")
```

---

# 二十一、`st.rerun()`：重新執行程式 🔄

有時候按下按鈕後，希望網頁馬上重新執行，可以使用：

```python
st.rerun()
```

例如：

```python
if st.button("重新整理畫面", key="banana"):
    st.rerun()
```

意思是：

> 如果使用者按下按鈕，就重新執行 Streamlit 程式。

---

# 🎯 今天的重點總整理

| 指令                 | 功能            |
| ------------------ | ------------- |
| `for`              | 重複做事情         |
| `in`               | 從一個範圍中一個一個拿資料 |
| `range()`          | 產生一串數字        |
| `list`             | 儲存很多資料        |
| `[]`               | 建立列表          |
| `[0]`              | 取得列表指定位置的資料   |
| `append()`         | 在列表最後面新增資料    |
| `remove()`         | 刪除指定的資料       |
| `sort()`           | 排序資料          |
| `len()`            | 計算列表裡有幾個資料    |
| `pop()`            | 依照位置刪除資料      |
| `st.columns()`     | 建立網頁欄位        |
| `with`             | 在指定區域放多個元件    |
| `st.text_input()`  | 建立文字輸入框       |
| `st.session_state` | 記住網頁上的資料      |
| `st.rerun()`       | 重新執行網頁程式      |

---

# 🌟 今天最重要的一句話

**`for` 迴圈可以幫我們重複做事情，`list` 可以幫我們把很多資料放在一起，而 Streamlit 的欄位、輸入框和 `session_state` 可以讓我們做出更有互動性的網頁！**

💪 今天學到的內容已經可以做出很多有趣的小作品，例如：**數字金字塔、待辦事項清單、簡單的計數器，以及有按鈕互動的小網頁！**

      """
    )
with st.expander("class4 課堂筆記"):
    st.write(
        """
# 🐍 Python 學習筆記（四）：`while` 迴圈、亂數、猜數字、字典與圖片

今天學到的 Python 功能越來越厲害了！🎉
我們今天讓 Python 學會：

> 🔄 一直重複做事情
> 🛑 在需要的時候停止
> 🎲 隨機抽數字
> 🎯 製作猜數字遊戲
> 🗂️ 用字典整理資料
> 🖼️ 在網頁上顯示圖片

---

# 一、`while` 迴圈：只要條件成立，就一直做 🔄

`while` 迴圈和之前學過的 `for` 迴圈一樣，都可以重複做事情。

不過 `while` 比較像是在說：

> **「只要這個條件還是 True，就一直做下去！」**

基本寫法：

```python
while 條件:
    重複做的事情
```

例如：

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

結果：

```text
0
1
2
3
4
```

Python 每做完一次，都會再檢查：

> `i < 5` 還是真的嗎？

如果是 `True`，就再做一次。

如果變成 `False`，就停止迴圈。

---

## `i += 1` 是什麼？

```python
i += 1
```

意思是：

```python
i = i + 1
```

例如原本：

```text
i = 0
```

執行一次後：

```text
i = 1
```

再執行：

```text
i = 2
```

---

## ⚠️ 小心無限迴圈！

看看這段程式：

```python
i = 0

while i < 5:
    print(i)
```

這樣會一直印出：

```text
0
0
0
0
0
...
```

因為 `i` 永遠沒有增加，所以：

```python
i < 5
```

永遠都是 `True`。

因此，使用 `while` 時要記得想：

> **「我的條件什麼時候才會變成 False？」**

---

# 二、`break`：強制停止迴圈 🛑

`break` 的意思是：

> **立刻跳出目前所在的迴圈！**

例如：

```python
i = 0

while i < 5:
    print(i)
    i += 1

    if i == 3:
        break
```

當 `i` 變成 3 時：

```python
break
```

就會讓迴圈停止。

---

## `break` 也可以用在 `for` 迴圈

```python
for i in range(5):
    print(i)

    if i == 3:
        break
```

結果：

```text
0
1
2
3
```

因為當 `i` 等於 3 時，就停止了。

💡 `break` 只會跳出**它所在的那一層迴圈**。

---

# 三、`random`：讓 Python 隨機抽數字 🎲

Python 可以使用 `random` 模組來產生隨機數字。

首先要先：

```python
import random
```

可以把 `random` 想成：

> 🎲 Python 的抽籤工具箱！

---

# 四、`random.randrange()`：像 `range()` 一樣抽數字

## `random.randrange(7)`

```python
print(random.randrange(7))
```

可能抽到：

```text
0～6
```

注意：**不會抽到 7！**

---

## 設定開始和結束

```python
print(random.randrange(1, 6))
```

可能抽到：

```text
1、2、3、4、5
```

一樣不包含最後面的 6。

---

## 設定間隔

```python
print(random.randrange(1, 6, 2))
```

可能從這些數字中抽一個：

```text
1、3、5
```

---

# 五、`random.randint()`：包含最後一個數字 🎯

```python
print(random.randint(1, 6))
```

可能抽到：

```text
1、2、3、4、5、6
```

和 `randrange()` 最大的不同是：

> `randint()` **會包含最後面的數字！**

| 指令                       | 範圍  |
| ------------------------ | --- |
| `random.randrange(1, 6)` | 1～5 |
| `random.randint(1, 6)`   | 1～6 |

---

# 六、猜數字遊戲 🎮

我們可以讓電腦偷偷選一個數字：

```python
target = random.randint(1, 100)
```

設定玩家可以猜的範圍：

```python
low = 1
high = 100
```

完整程式：

```python
import random

target = random.randint(1, 100)
low, high = 1, 100

while True:
    num = int(input(f"請輸入 {low} 到 {high} 的整數："))

    if num == target:
        print("猜中了！")
        break

    elif num < target:
        print("太小了！")
        low = num

    else:
        print("太大了！")
        high = num
```

---

## 程式怎麼思考？🤔

假設電腦選的答案是：

```text
50
```

玩家猜：

```text
30
```

電腦會說：

> 太小了！

下一次就可以從比較大的範圍開始猜。

如果猜：

```text
70
```

電腦會說：

> 太大了！

如果猜中：

```text
50
```

電腦會說：

> 猜中了！🎉

然後使用：

```python
break
```

跳出 `while True` 的無限迴圈。

---

# 七、Streamlit 版猜數字遊戲 🖥️

我們也可以把猜數字遊戲做成網頁！

首先匯入：

```python
import streamlit as st
import random
import time
```

---

## 用 `ss` 縮短 `session_state`

```python
ss = st.session_state
```

之後原本很長的：

```python
st.session_state.ans
```

可以簡寫成：

```python
ss.ans
```

---

## 第一次進入遊戲時，先建立答案

```python
if "ans" not in ss:
    ss.ans = random.randint(1, 100)
```

意思是：

> 如果還沒有答案，就隨機產生一個 1～100 的數字。

這樣使用者每次按按鈕時，答案就不會一直重新換掉。

---

## 記住最大值和最小值

```python
if "max_num" not in ss:
    ss.max_num = 100

if "min_num" not in ss:
    ss.min_num = 1
```

這樣網頁可以記住目前猜數字的範圍。

---

## 建立輸入框

```python
num = st.number_input(
    f"請輸入 {ss.min_num} 到 {ss.max_num} 的整數",
    step=1
)
```

例如目前範圍是：

```text
30 到 70
```

使用者就會知道下一次應該猜哪個範圍。

---

## 按下「猜！」按鈕

```python
if st.button("猜！"):
```

如果使用者真的按下按鈕，就開始判斷。

### 猜太大

```python
if num > ss.ans:
    st.write("太大了")
```

### 猜太小

```python
elif num < ss.ans:
    st.write("太小了")
```

### 猜對了

```python
else:
    st.write("答對了")
    st.balloons()
```

答對時就放氣球！🎈🎈🎈

---

## `time.sleep()`：暫停一下 ⏰

```python
time.sleep(1)
```

意思是：

> 暫停 1 秒鐘。

例如答對時：

```python
st.balloons()
time.sleep(1)
st.rerun()
```

可以先看到氣球，再重新開始遊戲。

---

# 八、字典 `dict`：有標籤的資料盒 🗂️

之前我們學過 `list`：

```python
fruits = ["apple", "banana", "orange"]
```

列表是用編號找到資料：

```python
fruits[0]
```

但是字典不一樣！

字典是使用：

> **key → value**

也就是：

> **名字 → 資料**

例如：

```python
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

可以想成：

| Key（標籤） | Value（資料） |
| ------- | --------- |
| a       | 1         |
| b       | 2         |
| c       | 3         |

---

# 九、字典的特色

## Key 必須是唯一的

不能有兩個完全一樣的 key。

例如：

```python
{
    "姓名": "小明",
    "年齡": 10
}
```

---

## Value 可以重複

```python
{
    "國文": 100,
    "數學": 100,
    "英文": 100
}
```

Value 都是 100 沒關係。

---

## 字典不是用 index 取資料

列表：

```python
fruits[0]
```

字典：

```python
d["a"]
```

字典要使用 **key** 找資料。

---

# 十、`keys()`：取得所有 key

```python
d = {"a": 1, "b": 2, "c": 3}

print(d.keys())
```

可以使用迴圈：

```python
for key in d.keys():
    print(key)
```

結果：

```text
a
b
c
```

---

# 十一、`values()`：取得所有 value

```python
for value in d.values():
    print(value)
```

結果：

```text
1
2
3
```

---

# 十二、`items()`：一次取得 key 和 value

```python
for key, value in d.items():
    print(key, value)
```

結果：

```text
a 1
b 2
c 3
```

這個方法很適合需要同時知道「名字」和「資料」的時候。

---

# 十三、新增與修改字典資料 ✏️

## 新增

```python
d["d"] = 4
```

如果原本沒有 `"d"`，就會新增。

結果：

```python
{
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}
```

---

## 修改

```python
d["a"] = 5
```

如果 `"a"` 已經存在，就會把原本的值改掉。

---

# 十四、`pop()`：刪除字典資料 ❌

```python
d.pop("a")
```

會刪除 key 是 `"a"` 的資料，並且把它的 value 回傳。

如果想避免資料不存在時發生錯誤，可以設定預設答案：

```python
d.pop("e", "Not found")
```

如果找不到 `"e"`，就會得到：

```text
Not found
```

---

# 十五、`in`：檢查 key 存不存在 🔍

```python
print("a" in d)
```

如果有 `"a"`：

```text
True
```

如果沒有：

```python
print("e" in d)
```

結果：

```text
False
```

💡 對字典直接使用 `in` 時，主要是在檢查 **key**。

---

# 十六、複雜的字典：盒子裡還有盒子 📦

字典裡可以放列表，也可以放另一個字典！

```python
d = {
    "a": [1, 2, 3],
    "b": {
        "c": 4,
        "d": 5
    }
}
```

取得 `"a"`：

```python
print(d["a"])
```

結果：

```text
[1, 2, 3]
```

取得第一個數字：

```python
print(d["a"][0])
```

結果：

```text
1
```

取得 `"b"` 裡面的 `"c"`：

```python
print(d["b"]["c"])
```

結果：

```text
4
```

---

# 十七、成績登記系統 📚

我們可以用複雜的字典記錄學生的成績：

```python
grade = {
    "小明": {
        "國文": [90, 80, 70],
        "數學": [85, 75, 65],
        "英文": [95, 85, 75]
    },
    "小美": {
        "國文": [88, 78, 68],
        "數學": [83, 73, 63],
        "英文": [93, 83, 73]
    }
}
```

可以想成：

```text
學生
 └── 科目
      └── 每次考試成績
```

---

## 取得小明的數學成績

```python
print(grade["小明"]["數學"])
```

結果：

```text
[85, 75, 65]
```

---

## 取得小美第一次英文成績

```python
print(grade["小美"]["英文"][0])
```

結果：

```text
93
```

---

# 十八、計算平均成績 🧮

Python 有：

```python
sum()
```

可以把很多數字加起來。

例如：

```python
scores = [90, 80, 70]

print(sum(scores))
```

結果：

```text
240
```

再搭配：

```python
len(scores)
```

就可以算平均：

```python
avg = sum(scores) / len(scores)
```

---

## 印出每位同學的國文平均

```python
for name, subjects in grade.items():
    chinese = subjects["國文"]
    avg = sum(chinese) / len(chinese)

    print(f"{name}的國文段考平均成績是 {avg:.2f}")
```

---

## `:.2f` 是什麼？

```python
f"{avg:.2f}"
```

意思是：

> 小數點後面顯示 2 位。

例如：

```text
83.3333333
```

會變成：

```text
83.33
```

---

# 十九、計算總平均成績

可以先把所有科目的成績加起來：

```python
for name, subjects in grade.items():
    total = 0

    for scores in subjects.values():
        total += sum(scores)

    avg = total / (len(subjects) * 3)

    print(f"{name}的總平均成績是 {avg:.2f}")
```

這裡使用了：

* `for` 迴圈
* 字典 `dict`
* `values()`
* `sum()`
* `len()`
* f-string

把以前學過的東西全部結合在一起了！🎉

---

# 二十、Streamlit 顯示圖片 🖼️

首先建立標題：

```python
st.title("圖片元件")
```

然後使用：

```python
st.image("image/apple.png", width=300)
```

意思是：

> 顯示 `image/apple.png` 這張圖片，寬度設定為 300。

---

# 二十一、`os.listdir()`：查看資料夾裡的檔案 📁

首先匯入：

```python
import os
```

設定資料夾名稱：

```python
image_folder = "image"
```

取得裡面的檔案：

```python
image_files = os.listdir(image_folder)
```

假設資料夾裡有：

```text
apple.png
banana.png
orange.png
```

`image_files` 就會得到一個列表。

---

# 二十二、用 `for` 顯示所有圖片

```python
for image_file in image_files:
    st.image(
        f"{image_folder}/{image_file}",
        width=image_size
    )
```

意思是：

> 一張一張把資料夾裡的圖片拿出來顯示！

---

# 二十三、讓使用者調整圖片大小 🔍

```python
image_size = st.number_input(
    "圖片大小",
    min_value=1,
    max_value=100,
    value=100
)
```

使用者可以自己決定圖片要多大。

然後：

```python
st.image(
    f"{image_folder}/{image_file}",
    width=image_size
)
```

圖片就會跟著設定改變。

---

# 二十四、`use_container_width=True`

另一種顯示圖片的方法：

```python
st.image(
    f"{image_folder}/{image_file}",
    use_container_width=True
)
```

意思是：

> 讓圖片的寬度自動配合目前網頁容器的寬度。

---

# 二十五、`st.success()`：顯示成功訊息 ✅

```python
st.success("購買成功！")
```

網頁上會顯示一個漂亮的成功提示。

很適合用在：

* 註冊成功
* 登入成功
* 購買成功
* 儲存成功

---

# 🎯 今天的重點總整理

| 指令                         | 功能                 |
| -------------------------- | ------------------ |
| `while`                    | 條件成立時一直重複          |
| `while True`               | 建立持續執行的迴圈          |
| `break`                    | 強制跳出迴圈             |
| `+=`                       | 在原本的數字上增加          |
| `random.randint()`         | 隨機抽數字，包含結束值        |
| `random.randrange()`       | 隨機抽數字，不包含結束值       |
| `dict`                     | 用 key 和 value 儲存資料 |
| `keys()`                   | 取得所有 key           |
| `values()`                 | 取得所有 value         |
| `items()`                  | 同時取得 key 和 value   |
| `pop()`                    | 刪除資料               |
| `in`                       | 檢查 key 是否存在        |
| `sum()`                    | 把數字全部加起來           |
| `:.2f`                     | 小數點顯示兩位            |
| `os.listdir()`             | 取得資料夾裡的檔案          |
| `st.image()`               | 顯示圖片               |
| `use_container_width=True` | 圖片自動符合容器寬度         |
| `st.success()`             | 顯示成功訊息             |

---

# 🌟 今天最重要的一句話

**`while` 可以讓程式按照條件一直重複，`random` 可以讓電腦隨機抽數字，`dict` 可以把資料整理得更有條理，而 Streamlit 可以把這些功能變成好玩的互動網頁！**

💡 下一次可以試著把今天的「猜數字遊戲」再升級，例如加入「猜了幾次」的計數器，練習 `while`、`session_state` 和變數一起使用。

      """
    )
with st.expander("class5 課堂筆記"):
    st.write(
        """

🐍 Python 今日課程筆記

今天主要學了兩個很有趣的主題：

🛒 用 Streamlit 製作購物平台
🤖 用 OpenAI API 製作 AI 聊天機器人
💬 把 AI 聊天機器人放進 Streamlit 網頁
第一部分 🛒 製作購物平台
1. import 是什麼？
import streamlit as st
import time


import 就像是：

📦「把別人做好的工具箱拿來使用！」

例如：

streamlit：幫我們做網頁
time：可以控制時間，例如等待 1 秒

而：

as st


就是幫工具取一個比較短的名字。

所以：

import streamlit as st


之後就可以寫：

st.title()
st.button()
st.image()


而不用一直寫 streamlit.title()。

2. st.title()：放一個大標題
st.title("購物平台")


就是在網頁上顯示：

購物平台

可以把它想成：

🏷️ 幫網頁掛上一個大招牌。

3. st.number_input()：讓使用者輸入數字
cols_count = st.number_input(
    "請輸入欄位數",
    min_value=1,
    max_value=5,
    value=2,
    step=1
)


這是在網頁上放一個「數字輸入框」。

例如使用者可以選：

1
2
3
4
5


幾個重要設定：

min_value=1 → 最小只能輸入 1
max_value=5 → 最大只能輸入 5
value=2 → 一開始預設是 2
step=1 → 每次增加 1

📌 可以記成：

number_input = 「請你輸入一個數字」

4. session_state：記住資料的小書包 🎒

這是今天非常重要的東西。

st.session_state


可以把它想成：

🎒 Streamlit 幫我們準備的一個「可以記住東西的小書包」。

例如：

if "products" not in st.session_state:


意思是：

「書包裡面有沒有叫做 products 的東西？」

如果沒有：

st.session_state.products = [...]


就把商品資料放進去。

5. List（列表）📋

例如：

[
    "apple",
    "banana",
    "orange"
]


這是一個列表（List）。

可以把 List 想成：

📋 一張購物清單。

裡面可以放很多東西。

例如：

fruits = ["apple", "banana", "orange"]


就代表：

fruits
 ├─ apple
 ├─ banana
 └─ orange

6. Dictionary（字典）📖

你的商品資料是：

{
    "name": "apple",
    "path": "image/apple.png",
    "price": 10,
    "stock": 10
}


這叫做 Dictionary（字典）。

可以把它想成：

📖 一本「商品資料卡」。

每一個資料都有自己的名字。

例如：

"name"


代表商品名稱。

"price"


代表價格。

"stock"


代表庫存。

所以：

product["price"]


就是：

💰 「拿出這個商品的價格。」

7. List + Dictionary

你的商品資料其實是：

[
    {"name": "apple", "price": 10, "stock": 10},
    {"name": "banana", "price": 10, "stock": 10},
    {"name": "orange", "price": 10, "stock": 10}
]


可以想成：

📋 一張商品清單，裡面放了很多張商品資料卡。

8. st.columns()：把網頁切成幾欄
cols = st.columns(cols_count)


如果：

cols_count = 3


就會把網頁分成：

┌────────┬────────┬────────┐
│ 第1欄  │ 第2欄  │ 第3欄  │
└────────┴────────┴────────┘


這樣商品就可以排在不同欄位裡。

9. for 迴圈 🔄
for i in range(len(st.session_state.products)):


for 可以想成：

🔄「一個一個檢查。」

例如有 4 個商品：

apple
banana
orange
bg


程式就會一個一個處理。

10. range()：產生數字
range(4)


會產生：

0
1
2
3


所以：

for i in range(4):


就是：

「從 0 開始，一直做到 3。」

📌 Python 很重要的一個特色：

數字通常從 0 開始算。

11. % 餘數

這一行很重要：

col_index = i % cols_count


% 叫做取餘數。

例如：

5 % 2 = 1


因為：

5 ÷ 2 = 2 …… 1


所以餘數是 1。

在這個購物平台裡：

i % cols_count


可以幫助我們決定：

📍「這個商品應該放在哪一欄？」

12. with：在某個區域裡做事情
with cols[col_index]:


可以想成：

🚪「進入這一欄，接下來的東西都放在這裡。」

例如：

with cols[0]:
    st.write("蘋果")


就是把「蘋果」放到第 1 欄。

13. st.image()：顯示圖片 🖼️
st.image(
    st.session_state.products[i]["path"],
    use_container_width=True
)


就是：

🖼️ 把商品圖片顯示在網頁上。

path 是圖片的位置。

例如：

"image/apple.png"


代表：

📁 在 image 資料夾裡，有一張叫做 apple.png 的圖片。

14. st.write()：顯示文字
st.write("價格：10")


就是把文字顯示在網頁上。

例如：

st.write(f"價格：{product['price']}")


就可以把商品真正的價格放進去。

15. f""：把資料放進文字裡

例如：

name = "apple"
price = 10


可以寫：

f"商品：{name}"


結果：

商品：apple


也可以：

f"價格：{price}"


結果：

價格：10


📌 記法：

f"" = 「我要把變數塞進文字裡！」

16. st.button()：做一個按鈕 🔘
if st.button("購買apple"):


網頁就會出現：

[ 購買apple ]


當使用者按下按鈕：

if


裡面的程式就會執行。

所以可以把它想成：

🔘 如果我按下按鈕，就做某件事情。

17. if：如果……就……
if stock > 0:


意思是：

「如果庫存大於 0，就可以買。」

例如：

if stock > 0:
    print("可以購買")
else:
    print("沒有庫存")


就像生活中的：

🧑「如果冰箱裡有牛奶，就喝牛奶；不然就不能喝。」

18. else：不然……
else:


代表：

「如果前面的條件不成立，就做這件事。」

例如：

if stock > 0:
    print("可以購買")
else:
    print("庫存不足")

19. >：大於
stock > 0


意思是：

庫存是不是「大於 0」？

其他常見符號：

符號	意思
>	大於
<	小於
>=	大於或等於
<=	小於或等於
==	等於
!=	不等於

⚠️ 注意：

=


和

==


不一樣！

= 是「放進去」。

x = 10


意思是：

把 10 放進 x。

而：

x == 10


是在問：

「x 是不是等於 10？」

20. 修改庫存

購買一個商品：

st.session_state.products[i]["stock"] = \
    st.session_state.products[i]["stock"] - 1


意思就是：

🛒 買走一個 → 庫存減少 1。

例如原本：

庫存：10


買一次：

庫存：9


再買一次：

庫存：8

21. st.success()：顯示成功訊息 ✅
st.success("購買成功")


網頁會顯示成功的訊息。

可以想成：

🟢「太棒了！事情成功了！」

22. st.error()：顯示錯誤訊息 ❌
st.error("庫存不足")


可以想成：

🔴「糟糕！出現問題了！」

23. in：有沒有在裡面？
if "成功" in st.session_state.message:


意思是：

「成功 這兩個字有沒有出現在訊息裡？」

例如：

購買apple成功


裡面有「成功」。

所以條件成立。

24. time.sleep()：休息一下 ⏰
time.sleep(1)


意思是：

⏳ 暫停 1 秒。

例如顯示：

購買成功！


停留 1 秒後，再繼續做其他事情。

25. st.rerun()：重新整理 🔄
st.rerun()


可以想成：

🔄「請重新跑一次網頁程式！」

為什麼需要？

例如買完蘋果後：

原本庫存：10
↓
購買
↓
庫存：9


重新執行後，網頁就會顯示最新的庫存。

第二部分 📦 新增商品庫存
26. append()：加入東西
product_names = []

for p in st.session_state.products:
    product_names.append(p["name"])


一開始：

product_names = []


是一個空清單。

然後：

append()


就是：

➕「把東西加到清單最後面。」

例如：

names = []

names.append("apple")
names.append("banana")


最後：

["apple", "banana"]

27. selectbox()：選擇一個東西
selected_product = st.selectbox(
    "選擇商品",
    product_names
)


網頁會出現一個選單：

選擇商品 ▼
apple
banana
orange


使用者可以選其中一個。

📌 記法：

selectbox = 📋「請你選一個！」

28. 新增庫存
p["stock"] = p["stock"] + add_stock


假設：

原本庫存：10
新增：5


就變成：

10 + 5 = 15


所以：

➕ 新增商品就是把數量加回去。

第三部分 🤖 製作 AI 聊天機器人

接下來進入今天另一個大主題：

🤖 讓 Python 可以跟 AI 說話！

29. openai
import openai


這是把 OpenAI 的工具拿進 Python。

就像：

🧰 拿出一個「可以跟 AI 溝通」的工具箱。

30. dotenv
from dotenv import load_dotenv


這個工具可以幫我們讀取 .env 檔案。

.env 可以想成：

🔐 一個專門放秘密設定的小盒子。

例如 API 金鑰就可以放在裡面。

31. API 金鑰 🔑
load_dotenv()


先讀取 .env。

然後：

openai.api_key = os.getenv("OPENAI_API_KEY")


就是把 API 金鑰拿出來。

可以想成：

🔑 API Key 就像「進入 AI 服務的鑰匙」。

⚠️ API 金鑰很重要，不要把自己的金鑰公開給別人看。

32. os.getenv()
os.getenv("OPENAI_API_KEY")


意思是：

「去環境設定裡，找名字叫 OPENAI_API_KEY 的資料。」

33. while True：一直做下去 🔄
while True:


可以想成：

🔁「一直重複做這件事。」

所以：

while True:
    user_input = input("你：")


程式就會一直等待你輸入。

34. input()：讓使用者輸入文字 ⌨️
user_input = input("你：")


畫面會出現：

你：


然後你可以輸入：

你好


程式就會把它放進：

user_input

35. .lower()：把英文變成小寫
user_input.lower()


例如：

EXIT


會變成：

exit


這樣程式就不用分辨：

exit
EXIT
Exit
eXiT

36. break：停止迴圈 🛑
if user_input.lower() in ["exit", "quit"]:
    break


意思是：

如果使用者輸入 exit 或 quit，就停止聊天。

break 可以想成：

🛑「好了，停止！」

37. 呼叫 AI
response = openai.chat.completions.create(


這是在告訴 OpenAI：

🤖「請 AI 幫我回答這個問題。」

38. model：選擇 AI
model="gpt-4o-mini"


意思是：

「我要使用哪一個 AI 模型？」

可以把模型想成：

🤖 AI 機器人的不同種類。

39. messages：告訴 AI 對話內容 💬
messages=[
    {"role": "system", "content": "請用繁體中文進行後續對話"},
    {"role": "user", "content": user_input},
]


這裡很重要。

AI 對話裡有不同角色：

system
"role": "system"


可以想成：

📢「老師交代 AI 的規則。」

例如：

請用繁體中文回答。

user
"role": "user"


就是：

🙋「使用者說的話。」

例如：

今天天氣如何？

40. response.choices[0]

AI 回答後：

response.choices[0].message.content


就是把 AI 真正回答的文字拿出來。

可以想成：

📦 AI 回傳了一個大包裹，我們把裡面的「答案」拿出來。

41. print()
print(f"AI:{assistant_massage}")


就是在終端機印出：

AI：你好！很高興認識你！


📌 print()：

🖨️ 把東西印出來。

第四部分 💬 把 AI 做成網頁聊天機器人

前面的 AI 是在「終端機」聊天。

這次我們使用：

import streamlit as st


把它做成漂亮的網頁。

42. st.secrets：安全取得秘密資料 🔐
openai.api_key = st.secrets["OPENAI_API_KEY"]


這次沒有使用 .env，而是使用 Streamlit 的秘密設定。

可以想成：

🔐「從安全的小保險箱裡拿 API Key。」

43. 幫 session_state 取短名字
ss = st.session_state


原本要寫：

st.session_state.history


現在可以寫：

ss.history


因為：

ss = st.session_state


就是幫它取一個短名字。

📌 就像：

「王小明太長了，我叫他小明。」

44. 儲存聊天紀錄
if "history" not in ss:
    ss.history = []


意思是：

「如果還沒有聊天紀錄，就先準備一個空清單。」

例如：

ss.history = []


一開始是：

[]


聊天之後變成：

[
  使用者說的話,
  AI說的話,
  使用者說的話,
  AI說的話
]

45. role 和 content

聊天紀錄可能長這樣：

{
    "role": "user",
    "content": "你好"
}


其中：

role → 誰說的？
content → 說了什麼？

例如：

role：user
content：你好


就是：

🙋 使用者說：「你好」

AI 則是：

{
    "role": "assistant",
    "content": "你好！"
}

46. st.chat_message()：顯示聊天訊息 💬
st.chat_message("user").write(message["content"])


可以顯示：

🪄 你好


AI：

st.chat_message("assistant").write(message["content"])


可以顯示：

✨ 你好！很高興認識你。

47. st.chat_input()：聊天輸入框
prompt = st.chat_input("請輸入想要對話的訊息")


網頁底下會有一個聊天輸入框。

使用者輸入：

你好


之後：

prompt


就會得到：

你好

48. 把訊息加入聊天紀錄
ss.history.append({
    "role": "user",
    "content": prompt
})


意思是：

📋「把使用者剛剛說的話加入聊天紀錄。」

49. 把 AI 回答也存起來
ss.history.append({
    "role": "assistant",
    "content": assistant_massage
})


意思是：

🤖「把 AI 的回答也加入聊天紀錄。」

這樣下一次 AI 才能知道之前聊過什麼。

50. 三欄排版
col1, col2, col3 = st.columns([4, 2, 1])


代表把畫面分成三個區域：

┌──────────────────┬──────────┬─────┐
│      col1        │   col2   │col3 │
│       4          │    2     │  1  │
└──────────────────┴──────────┴─────┘


數字越大，欄位越寬。

所以：

[4, 2, 1]


就是：

📐 第一欄最大，第二欄其次，第三欄最小。

51. text_input()：輸入文字
ss.system_message = st.text_input(
    "系統訊息",
    ss.system_message
)


可以讓使用者自己修改 AI 的規則。

例如：

請用繁體中文回答


改成：

請像老師一樣回答問題


AI 的回答方式就可能跟著改變。

52. selectbox() 選 AI 模型
ss.model = st.selectbox(
    "AI模型",
    ["gpt-4o-mini", "gpt-4o", ...]
)


讓使用者可以從選單選擇 AI 模型。

就像：

🤖「你今天想請哪一個 AI 幫忙？」

53. 清除聊天紀錄 🗑️
if st.button("🗑️ 清除對話紀錄"):
    ss.history = []
    st.rerun()


按下按鈕後：

ss.history = []


把聊天紀錄變成空清單。

就像：

🗑️ 把聊天紀錄全部丟進垃圾桶。

然後：

st.rerun()


重新整理網頁。

⭐ 今天最重要的觀念整理

如果要準備考試，我最推薦你記住下面這些。

Python 指令	簡單意思
import	📦 拿工具來使用
if	🤔 如果
else	↪️ 不然
for	🔄 一個一個重複做
while	🔁 一直重複
break	🛑 停止迴圈
in	🔎 有沒有在裡面
=	📥 把資料放進去
==	⚖️ 比較是不是相等
>	⬆️ 大於
<	⬇️ 小於
%	🧮 取餘數
append()	➕ 加進列表
print()	🖨️ 印出文字
input()	⌨️ 讓使用者輸入
range()	🔢 產生數字範圍
lower()	🔡 變成英文小寫
sleep()	⏰ 等待一下
rerun()	🔄 重新執行網頁
🌟 Streamlit 指令小抄
指令	功能
st.title()	🏷️ 大標題
st.write()	✏️ 顯示文字
st.image()	🖼️ 顯示圖片
st.button()	🔘 按鈕
st.number_input()	🔢 數字輸入
st.text_input()	✏️ 文字輸入
st.selectbox()	📋 選擇一個項目
st.columns()	📐 分欄
st.success()	🟢 成功訊息
st.error()	🔴 錯誤訊息
st.chat_message()	💬 顯示聊天訊息
st.chat_input()	💬 聊天輸入框
st.rerun()	🔄 重新執行
st.session_state	🎒 記住資料
🤖 AI 聊天機器人的流程

最後，把整個 AI 程式想成一個小故事：

🙋 使用者
   ↓
「你好」
   ↓
📨 Python 把問題送給 AI
   ↓
🤖 AI 思考
   ↓
💬 AI 回答
   ↓
📦 Python 把答案拿回來
   ↓
🖥️ 顯示在網頁上


而 history 就像一本：

📕「聊天日記」

把每次：

🙋 使用者說什麼
🤖 AI 說什麼


都記錄下來。

🧠 一張圖記住今天的課程
                    🐍 Python
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
      🛒 購物平台                 🤖 AI 聊天
          │                         │
     Streamlit                    OpenAI
          │                         │
   ┌──────┼──────┐           ┌──────┼──────┐
   ↓      ↓      ↓           ↓      ↓      ↓
 商品    按鈕   庫存        API    Model  History
   │      │      │           │      │      │
 List   if/else session     Key   模型   聊天紀錄
        button   state

🎯 今天最核心的三件事

第一：Python 可以管理資料。

例如：

products = []


和：

product["price"]


可以幫我們管理商品。

第二：Streamlit 可以把 Python 變成網頁。

例如：

st.button()
st.image()
st.write()
st.chat_input()


可以做出互動式網站。

第三：OpenAI API 可以讓程式跟 AI 對話。

基本流程就是：

使用者問題
    ↓
Python
    ↓
OpenAI API
    ↓
AI
    ↓
Python
    ↓
顯示回答


只要把這三個觀念弄懂，你今天學的購物平台和 AI 聊天機器人就會串起來了。
      """
    )