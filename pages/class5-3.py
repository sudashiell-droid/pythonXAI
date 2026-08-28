import streamlit as st
import openai

openai.api_key =st.secrets['OPENAI_API_KEY']  #設定Openai的API金鑰
ss=st.session_state
if 'history' not in ss: #初始化對話紀錄
    ss.history=[]  #如果對話紀錄不存在，創建一個空的列表
if'system_message' not in ss: #初始化系統訊息
    ss.system_message=(
        '請用繁體中文進行後續對話'  #如果系統訊息不存在，設置預設系統訊息
        )
if'model'not in ss: #初始化AI模型
    ss.model='gpt-4o-mini'  #如果AI模型不存在，設置預設模型

# 設置三個布局，分別占用4:2:12的寬度
col1,col2,col3=st.columns([4,2,1])
with col1:
    ss.system_message=st.text_input('系統訊息',ss.system_message)
with col2:
    ss.model=st.selectbox('AI模型',['gpt-4o-mini','gpt-4o','gpt-5.6-luna','gpt-5.6-terra'])
with col3:
    if st.button('🗑️ 清除對話紀錄'): # 在第三列顯示清空案鈕
        ss.history=[]  #如果按下清除案鈕，就清空對話紀錄
        st.rerun() #重新整理頁面以反映更改

for message in ss.history: 
    if message['role']=='user': #如果訊息的角色是使用者
        st.chat_message('user',avatar='🪄').write(message['content']) # 顯示使用者的訊息，使用指定的頭像

    else:
        st.chat_message('assistant',avatar='✨').write(message['content']) # 顯示AI的訊息，使用指定的頭像

prompt=st.chat_input('請輸入想要對話的訊息') # 顯示對話輸入框，等待使用者輸入訊息\
if prompt: #如果使用者輸入了訊息
    ss.history.append({'role':'user','content':prompt}) #將使用者輸入的訊息加入對話紀錄

    response = openai.chat.completions.create(
        model=ss.model, # 使用指定的AI模型
        messages=[{'role':'system','content':ss.system_message}]+ss.history,
    )

    assistant_massage=response.choices[0].message.content #取得AI助手回傳的訊息內容
    ss.history.append({'role':'assistant','content':assistant_massage}) #將AI助手的訊息加入對話紀錄
    st.rerun() #重新整理頁面以顯示新的訊息