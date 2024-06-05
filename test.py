#streamlit run d:\大模型\streamlit\vis\test.py [ARGUMENTS]
import streamlit as st
import os
import qianfan
from streamlit_chat import message

ACCESS_KEY=st.text_input("设置ACCESS_KEY:",key='input1')
SECRET_KEY=st.text_input("设置SECRET_KEY:",key='input2')
os.environ["QIANFAN_ACCESS_KEY"] = ACCESS_KEY
os.environ["QIANFAN_SECRET_KEY"] = SECRET_KEY

def generate_response(prompt):
    chat_comp = qianfan.ChatCompletion(model="ERNIE-Speed")
    resp = chat_comp.do(
        messages=[{"role": "user", "content":prompt }],
        top_p=0.8,
        temperature=0.9,
        penalty_score=1.0,
    )
    ms=resp["result"]
    return ms
 
st.markdown("#### 我是医生聊天机器人,我可以回答您的任何问题！")
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
user_input=st.text_input("请输入您的问题:",key='input3')
if user_input:
    output=generate_response(user_input)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], 
                is_user=True, 
                key=str(i)+'_user')


