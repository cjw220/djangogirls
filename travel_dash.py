import streamlit as st
import random
import time
from travel_data import TRAVEL_DATABASE # 👈 確保這裡對應到剛才的新檔名

st.set_page_config(page_title="期末報告：旅遊求籤機", page_icon="⛩️")
st.title("⛩️ 旅遊命定之地：求籤系統")

st.subheader("請回答以下問題，我們將感應您的目的地...")

# 問題區
q1 = st.selectbox("1. 您的錢包目前狀態？", 
                  ["(搞笑) 它在哭泣，空空如也", "(正經) 它很飽滿，準備出發", "(正經) 錢只是數字"])

q2 = st.radio("2. 您現在的體力值？", 
              ["(搞笑) 我是一灘爛泥", "(正經) 我可以爬山運動"])

# 啟動按鈕
if st.button("🔮 請求靈感"):
    score = 0
    for ans in [q1, q2]:
        if "(搞笑)" in ans: score += 1
            
    with st.spinner('正在與神靈溝通中...'):
        time.sleep(1.5)
    
    # 決定類別
    category = "funny" if score >= 1 else "serious"
    result = random.choice(TRAVEL_DATABASE[category])
    
    st.divider()
    st.markdown(f"### 您的命定之地：**{result['place']}**")
    st.info(result['desc'])
    st.image(result['img'], use_container_width=True)