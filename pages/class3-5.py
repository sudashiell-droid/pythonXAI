import random
import streamlit as st
import time
ss=st.session_state # 用來縮短session_state的寫法
if 'ans'not in ss:
    ss.ans=random.randint(1,100)
if'max_num'not in ss:
    ss.max_num=100
if'min_num'not in ss:
    ss.min_num=1
st.title('猜數字遊戲')
num=st.number_input(f'請輸入{ss.min_num}到{ss.max_num}的整數',step=1)
if st.button('猜!'):
    if num > ss.ans:
        st.write('太大了')
        if num < ss.max_num:
            ss.max_num=num
    elif num < ss.ans:
        st.write('太小了')
        if num > ss.min_num:
            ss.min_num=num
    else:
        st.write('答對了')
        st.balloons()
        time.sleep(1)
        st.rerun()
