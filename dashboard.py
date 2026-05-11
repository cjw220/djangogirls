import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 載入資料
df = sns.load_dataset("penguins")

st.title("🐧 Penguin Data Dashboard")

# 2. 建立下拉式選單 (Selectbox)
# 第一個參數是標題，第二個參數是選單選項
chart_type = st.selectbox(
    "Choose the table you want：",
    ["資料表格", "翅膀 vs 體重 (散佈圖)", "品種體重分佈 (箱形圖)", "島嶼數量統計 (計數圖)"]
)

# 3. 根據選單的結果 (chart_type) 來決定顯示什麼內容
if chart_type == "資料表格":
    st.write("### 原始資料表")
    st.write(df)

elif chart_type == "翅膀 vs 體重 (散佈圖)":
    st.write("### Flipper Length vs Body Mass")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species", ax=ax)
    st.pyplot(fig)

elif chart_type == "品種體重分佈 (箱形圖)":
    st.write("### Body Mass Distribution by Species")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="species", y="body_mass_g", palette="pastel", ax=ax)
    st.pyplot(fig)

elif chart_type == "島嶼數量統計 (計數圖)":
    st.write("### Penguin Counts by Island")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="island", hue="species", palette="coolwarm", ax=ax)
    st.pyplot(fig)