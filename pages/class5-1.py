import streamlit as st
import time

st.title("購物平台")

cols_count = st.number_input("請輸入欄位數", min_value=1, max_value=5, value=2, step=1)

if "products" not in st.session_state:
    st.session_state.products = [
        {"name": "apple", "path": "image/apple.png", "price": 10, "stock": 10},
        {"name": "banana", "path": "image/banana.png", "price": 10, "stock": 10},
        {"name": "orange", "path": "image/orange.png", "price": 10, "stock": 10},
        {"name": "bg", "path": "image/bg.png", "price": 10, "stock": 10}
    ]

if "message" not in st.session_state:
    st.session_state.message = ""

cols = st.columns(cols_count)

for i in range(len(st.session_state.products)):
    col_index = i % cols_count
    with cols[col_index]:
        st.image(st.session_state.products[i]["path"], use_container_width=True)
        st.write(f"{st.session_state.products[i]['name']}")
        st.write(f"價格：{st.session_state.products[i]['price']}")
        st.write(f"庫存：{st.session_state.products[i]['stock']}")
        if st.button(f"購買{st.session_state.products[i]['name']}", key=f"btn_{i}"):
            if st.session_state.products[i]['stock'] > 0:
                st.session_state.products[i]['stock'] = st.session_state.products[i]['stock'] - 1
                st.session_state.message = f"購買{st.session_state.products[i]['name']}成功"
            else:
                st.session_state.message = "庫存不足，無法購買！"
            st.rerun()

if st.session_state.message != "":
    if "成功" in st.session_state.message:
        st.success(st.session_state.message)
    else:
        st.error(st.session_state.message)
    
    time.sleep(1)
    st.session_state.message = ""
    st.rerun()

st.markdown("---")

c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.markdown("## 新增商品庫存")

    product_names = []
    for p in st.session_state.products:
        product_names.append(p["name"])

    selected_product = st.selectbox("選擇商品", product_names)
    add_stock = st.number_input("新增商品數量", min_value=1, step=1)

    if st.button("確認新增"):
        for p in st.session_state.products:
            if p["name"] == selected_product:
                p["stock"] = p["stock"] + add_stock
                st.success(f"已成功為 {selected_product} 增加 {add_stock} 個庫存！")
                time.sleep(1)
                st.rerun()