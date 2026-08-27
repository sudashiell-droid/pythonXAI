import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2) # 2columns
col1.button('按鈕1',key='btn1') # 在col1中建立一個按鈕類似st.button('按鈕1')
col2.button('按鈕2',key='btn2') # 在col1中建立一個按鈕類似st.button('按鈕1')

# 3columns, 可以用比例來設定每個column的寬度，將比例放到list中
col1, col2, col3 = st.columns([1,2,3]) 
col1.button('按鈕1',key='btn5') # 在col1中建立一個按鈕類似st.button('按鈕1')
col2.button('按鈕2',key='btn6') # 在col1中建立一個按鈕類似st.button('按鈕2')
col3.button('按鈕3',key='btn7') # 在col1中建立一個按鈕類似st.button('按鈕3')

col1, col2 = st.columns([1,2]) 
with col1:  # 在col1使用with語句放更多東西
    if st.button('按鈕1',key='btn8'): # 在col1中建立一個按鈕
        st.balloons()  # 在col1中建立一個氣球
    st.write('這是col1') # 在col1中建立一個文字
with col2:  # 在col2使用with語句放更多東西
    st.button('按鈕2',key='btn9') # 在col2中建立一個按鈕
    st.write('這是col2') # 在col2中建立一個文字

st.write('---')
st.title('文字輸入元件')
# st.text_input指令格式st.text_input(輸入欄位的標題，value='預設顯示文字')
text = st.text_input('請輸入文字',value='這是預設文字')
st.write(f'你輸入的文字是：{text}')

if'ans1' not in st.session_state:  # 如果session_state中沒有ans這個變數
    st.session_state.ans1 = 1 # 設定session_state.ans1=1 

if st.button('按下去ans加1',key='ans2'):
    st.session_state.ans1 = st.session_state.ans1 + 1
st.write(f'ans={st.session_state.ans1}') # 在顯示session_state.ans的值

if'apple' not in st.session_state:  # 如果session_state中沒有apple這個變數
    st.session_state.apple = 1 # 設定session_state.apple=1
# 有時候按鈕按下，不一定會重新整理畫面
# 這時候可以使用st.rerun()強制重新整理畫面
if st.button('重新整理畫面',key='banana'): # 如果按下按鈕
    # .....
    st.rerun() # 重新執行程式

