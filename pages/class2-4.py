import streamlit as st 
st.title("數字金字塔")
i = st.number_input("請輸入一個整數*(1-9)", min_value=1, max_value=9, step=1)
st.write('數字金字塔:')
for j in range(1,i+1):
    st.write(str(j)*j)