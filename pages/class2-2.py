import streamlit as st #匯入streamlit模組並命名為st

# min_value=0可以設定最小值為0，max_value=100可以設定最大值為100
number = st.number_input("請輸入一個數字", min_value=0, max_value=100, step=1)
# st.markdown()可以在網頁上顯示markdown語法顯示文字
st.markdown(f"你輸入的數字是：{number}")

st.markdown("---")
st.markdown("### 練習")
score = st.number_input("請輸入你的分數", min_value=0, max_value=100, step=1)
if score >= 90:
    st.write("你的等級是 🫅A")
elif score >= 80:
    st.write("你的等級是 🕵️B")
elif score >= 70:
    st.write("你的等級是 👷C")
elif score >= 60:
    st.write("你的等級是 👩‍🦽D")
else:
    st.write("你的等級是 ___*( ￣皿￣)/#____F")

st.markdown("---")
st.markdown("### 按鈕練習")
# st.button()可以在網頁上一個顯示按鈕，使用者可點及按鈕
# key式按鈕的識別名稱，可以用來區分不同的按鈕
# 如果使用者點及按鈕，st.button()會回傳True，否則回傳False
st.button("按我一下", key="botton1")
if st.button("按我一下", key="ballons"):
    st.balloons()
if st.button("按我一下", key="snow"):
    st.snow()
st.markdown("---")