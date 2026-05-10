import streamlit as st
import random
import time
from travel_data import TRAVEL_DATABASE

# Page configuration
st.set_page_config(page_title="Paris Fortune Teller", page_icon="🥐")
st.title("🥐 Paris Edition: Destiny Finder")

st.subheader("Discover which corner of Paris is calling your soul today...")

# Question Section
q1 = st.selectbox("1. How much 'Emily in Paris' energy do you have?", 
                  ["(Funny) None, I just want to survive the day", 
                   "(Serious) I am ready for a romantic stroll", 
                   "(Serious) I want to see every museum in the city"])

q2 = st.radio("2. What is your current budget for a snack?", 
              ["(Funny) I'm looking for a fallen crumb", 
               "(Serious) A decent croissant from a boulangerie"])

# Prediction Button
if st.button("🔮 Summon the Parisian Spirits"):
    funny_count = 0
    for ans in [q1, q2]:
        if "(Funny)" in ans: 
            funny_count += 1
            
    with st.spinner('Preparing your croissant and consulting the spirits...'):
        time.sleep(1.5)
    
    category = "funny" if funny_count >= 1 else "serious"
    result = random.choice(TRAVEL_DATABASE[category])
    
    st.divider()
    
    if category == "funny":
        st.warning("⚠️ Ooh la la! The spirits sensed some chaotic vibes...")
    else:
        st.balloons()
        st.success("✨ C'est magnifique! A classic Parisian dream awaits.")
        
    st.markdown(f"### Your Destiny: **{result['place']}**")
    st.info(result['desc'])
    st.image(result['img'], use_container_width=True)