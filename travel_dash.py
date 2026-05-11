import streamlit as st
import random
import time
from travel_data import TRAVEL_DATABASE

# --- 1. CSS & THEMING (Criteria: CSS/Bootstrap) ---
st.markdown("""
    <style>
    .main { background-color: #fafafa; }
    .stButton>button { 
        background-color: #D4AF37; 
        color: white; 
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
    }
    h1 { color: #2c3e50; font-family: 'Helvetica Neue', sans-serif; }
    footer { visibility: hidden; }
    .custom-footer {
        text-align: center;
        padding: 20px;
        color: #7f8c8d;
        font-size: 0.8rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session State
if 'page' not in st.session_state: st.session_state.page = 'home'
if 'result' not in st.session_state: st.session_state.result = None

def go_to_result(category):
    st.session_state.result = random.choice(TRAVEL_DATABASE[category])
    st.session_state.page = 'result'

def go_back():
    st.session_state.page = 'home'

# --- PAGE 1: HOME ---
if st.session_state.page == 'home':
    # Criteria: HTML Header
    st.markdown("<h1>🥐 Paris Destiny Agency</h1>", unsafe_allow_html=True)
    st.markdown("### *AI-Powered Luxury Travel Consulting*")
    
    st.divider()
    
    st.subheader("Discover your spiritual corner in Paris...")
    q1 = st.selectbox("1. How much 'Emily in Paris' energy do you have?", 
                      ["(Funny) None, I just want to survive the day", 
                       "(Serious) I am ready for a romantic stroll", 
                       "(Serious) I want to see every museum"])
    
    q2 = st.radio("2. What is your current budget for a snack?", 
                  ["(Funny) I'm looking for a fallen crumb", 
                   "(Serious) A decent croissant from a boulangerie"])

    if st.button("🔮 Seek My Fortune"):
        funny_count = sum(1 for ans in [q1, q2] if "(Funny)" in ans)
        category = "funny" if funny_count >= 1 else "serious"
        with st.spinner('Consulting the spirits...'):
            time.sleep(1.5)
            go_to_result(category)
            st.rerun()

# --- PAGE 2: RESULT ---
elif st.session_state.page == 'result':
    res = st.session_state.result
    st.markdown(f"<h1>🔮 Your Destiny: {res['place']}</h1>", unsafe_allow_html=True)
    
    # Criteria: Images & Alt tags
    st.image(res['img'], caption=f"View of {res['place']}", use_container_width=True)
    st.info(res['desc'])

    # Criteria: Navigation (Internal Links)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Retake Quiz"): go_back(); st.rerun()
    with col2:
        if 'url' in res: st.link_button("Official Info", res['url'])

    st.divider()
    
    # --- 2. CONTACT FORM (Criteria: Contact Form) ---
    st.subheader("📩 Book a Private Tour")
    with st.form("contact"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        notes = st.text_area("Any special requests?")
        if st.form_submit_button("Send to Consultant"):
            st.success(f"Merci, {name}! We will contact you at {email} soon.")

# --- 3. IMPRINT (Criteria: Imprint) ---
st.markdown("""
    <div class="custom-footer">
        <hr>
        <p><b>Paris Destiny Agency</b> | 123 Rue de la Paix, 75002 Paris, France</p>
        <p><i>Imprint: This is a student graduation project. All images are sourced from Unsplash.</i></p>
    </div>
    """, unsafe_allow_html=True)