import streamlit as st
import random
import time
from travel_data import TRAVEL_DATABASE

# --- 1. DEFINE NAVIGATION ORDER (PAGES) ---
# TA Feedback Applied: Replaced casual emojis with elegant non-emoji typography (✦)
# Renamed "AI Quiz" to "Destiny Quiz" to look more like a bespoke luxury product
PAGES = [
    "✦  Home",
    "✦  Services",
    "✦  Destiny Quiz",
    "✦  Contact",
    "✦  About Us",
    "✦  Imprint"
]

# --- 2. INITIALIZE SESSION STATE ---
if 'menu_selection' not in st.session_state:
    st.session_state.menu_selection = PAGES[0] 

if 'page' not in st.session_state:
    st.session_state.page = 'home' 

if 'result' not in st.session_state:
    st.session_state.result = None

# --- 3. NAVIGATION SYNC FUNCTION ---
def sync_nav():
    st.session_state.menu_selection = st.session_state.sidebar_nav

# --- 4. CSS & THEMING (PARISIAN CHIC EDITION) ---
st.markdown("""
    <style>
/* ========================================================= */
/* 🚀 IMPORT GOOGLE FONTS */
/* ========================================================= */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Montserrat:wght@300;400;500;600&display=swap');

/* ========================================================= */
/* GLOBAL STYLES & FONTS */
/* ========================================================= */
.stApp {
    font-family: 'Montserrat', sans-serif;
}

/* Force the entire background view container to be French Dusty Rose */
[data-testid="stAppViewContainer"] {
    background-color: #F5EBE6 !important;
}

/* 💡 FIX: Make the top header container transparent to remove the white bar */
header[data-testid="stHeader"] {
    background-color: transparent !important;
    background: transparent !important;
}

/* Luxury Serif font for Headers (Vogue Style) */
h1, h2, h3, .stSubheader p {
    font-family: 'Playfair Display', serif !important;
    color: #1A1A2E !important;
    font-weight: 700 !important;
}

h1 {
    letter-spacing: -0.5px;
    font-size: 3rem !important;
}

/* ========================================================= */
/* PREMIUM SIDEBAR */
/* ========================================================= */
section[data-testid="stSidebar"] {
    background: #12121F !important;
    border-right: 1px solid rgba(0,0,0,0.05);
    padding-top: 40px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
    display: none !important;
}

section[data-testid="stSidebar"] .stRadio > label {
    display: none !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    font-family: 'Playfair Display', serif !important;
    padding: 14px 20px;
    margin-bottom: 10px;
    border-radius: 12px;
    font-size: 18px !important;
    font-weight: 500 !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

section[data-testid="stSidebar"] p, 
section[data-testid="stSidebar"] label, 
section[data-testid="stSidebar"] div[role="radiogroup"] label p {
    color: #EAEAEA !important;
    font-family: 'Playfair Display', serif !important;
    letter-spacing: 0.5px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background-color: rgba(255, 255, 255, 0.05) !important;
    transform: translateX(6px);
}
section[data-testid="stSidebar"] div[role="radiogroup ] label:hover p {
    color: #C5A059 !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background-color: rgba(197, 160, 89, 0.12) !important;
    border-left: 3px solid #C5A059 !important;
    padding-left: 22px;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
    color: #C5A059 !important;
    font-weight: 700 !important;
}

[data-baseweb="tooltip"], [data-testid="collapsedControl"], span.material-symbols-rounded {
    display: none !important;
}

.block-container {
    padding-top: 3rem;
}

/* ========================================================= */
/* BUTTONS & FORMS */
/* ========================================================= */
.stButton>button, div[data-testid="stForm"] button {
    background-color: #C5A059 !important; 
    color: #FFFFFF !important;
    border-radius: 8px !important;
    border: none !important;
    padding: 12px 28px !important;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600 !important;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 12px rgba(197, 160, 89, 0.2);
    transition: all 0.25s ease !important;
}

.stButton>button:hover, div[data-testid="stForm"] button:hover {
    background-color: #A3803B !important; 
    box-shadow: 0 6px 18px rgba(197, 160, 89, 0.35);
    transform: translateY(-1px);
}

/* ========================================================= */
/* CUSTOM FOOTER */
/* ========================================================= */
.custom-footer {
    text-align: center;
    padding: 30px 20px;
    color: #8A8A9A;
    font-size: 0.8rem;
    font-family: 'Montserrat', sans-serif;
}
.custom-footer hr {
    border-top: 1px solid rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
    </style>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR NAVIGATION CONTROLLER ---
menu = st.sidebar.radio(
    "Navigation",
    PAGES,
    index=PAGES.index(st.session_state.menu_selection),
    key="sidebar_nav",
    on_change=sync_nav
)

current_page = st.session_state.menu_selection

# --- 6. CORE LOGIC FUNCTIONS ---
def go_to_result(category):
    st.session_state.result = random.choice(TRAVEL_DATABASE[category])
    st.session_state.page = 'result'

def go_back():
    st.session_state.page = 'home'

# =========================================================
# HOME PAGE
# =========================================================
if current_page == "✦  Home":
    st.markdown("<h1>✦ Paris Destiny Agency</h1>", unsafe_allow_html=True)
    st.markdown("### *AI-Powered Luxury Travel Consulting*")
    st.divider()
    
    st.subheader("Welcome to Paris Destiny Agency")
    st.write("""
    Discover personalized Paris experiences powered by advanced intelligence.
    Whether you dream of romantic evenings, hidden cafés, or luxury adventures,
    our agency helps you uncover your perfect Paris journey.
    """)

    # High-end action button
    if st.button("Begin Your Destiny Match"):
        st.session_state.menu_selection = "✦  Destiny Quiz"
        st.rerun()

    st.image(
        "https://images.unsplash.com/photo-1502602898657-3e91760cbb34",
        caption="The beauty of Paris at sunset",
        use_container_width=True
    )
    st.divider()
    
    st.subheader("Why Choose Us?")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Happy Travelers", "10,000+")
    with col2: st.metric("Hidden Cafés Explored", "250+")
    with col3: st.metric("Chance of Paris Drama", "99%")

# =========================================================
# SERVICES PAGE
# =========================================================
elif current_page == "✦  Services":
    st.title("Our Services")
    st.subheader("Bespoke Gastronomy Tours")
    st.write("Discover hidden bakeries and iconic Paris cafés.")
    st.subheader("Curated Fine Art Experiences")
    st.write("Explore the Louvre and private Parisian art collections.")
    st.subheader("Exclusive Evening Promenades")
    st.write("Private guided experiences around Paris at night.")
    st.subheader("Algorithmic Travel Matching")
    st.write("Receive personalized recommendations through our bespoke consulting framework.")
    st.image("https://images.unsplash.com/photo-1511739001486-6bfe10ce785f", use_container_width=True)

# =========================================================
# DESTINY QUIZ PAGE
# =========================================================
elif current_page == "✦  Destiny Quiz":
    
    if st.session_state.page == 'home':
        st.markdown("<h1>✦ Paris Destiny Quiz</h1>", unsafe_allow_html=True)
        st.markdown("### Discover your spiritual corner in Paris")
        st.divider()
        q1 = st.selectbox("1. What kind of traveler are you?", ["I survive on chaos and caffeine", "Romantic explorer", "Art and museum lover", "Luxury traveler"])
        q2 = st.radio("2. Your ideal Paris breakfast?", ["Free hotel bread", "Artisan croissant and coffee", "Fancy rooftop brunch"])
        q3 = st.selectbox("3. What is your vacation energy?", ["Confused but trying my best", "Elegant and classy", "Adventure and exploration"])

        if st.button("Consult Destiny"):
            funny_options = ["I survive on chaos and caffeine", "Free hotel bread", "Confused but trying my best"]
            funny_count = sum(1 for ans in [q1, q2, q3] if ans in funny_options)
            category = "funny" if funny_count >= 1 else "serious"
            
            with st.spinner('Consulting the spirits of Paris...'):
                time.sleep(1.5)
                go_to_result(category)
                st.rerun()

    elif st.session_state.page == 'result':
        res = st.session_state.result
        st.markdown(f"<h1>✦ Your Destiny: {res['place']}</h1>", unsafe_allow_html=True)
        st.image(res['img'], caption=f"View of {res['place']}", use_container_width=True)
        st.info(res['desc'])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Retake Quiz"):
                go_back()
                st.rerun()
        with col2:
            if 'url' in res: st.link_button("Official Info", res['url'])
            
        st.divider()
        
        st.subheader("Book a Private Tour")
        with st.form("contact"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            if st.form_submit_button("Send to Consultant"):
                st.success(f"Merci, {name}! We will contact you at {email} soon.")

# =========================================================
# CONTACT PAGE
# =========================================================
elif current_page == "✦  Contact":
    st.title("Contact Us")
    with st.form("main_contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        st.text_area("Your Message")
        if st.form_submit_button("Send Message"):
            st.success("Your message has been sent successfully!")

# =========================================================
# ABOUT PAGE
# =========================================================
elif current_page == "✦  About Us":
    st.title("About Paris Destiny Agency")
    st.write("We combine software engineering and luxury travel inspiration into one interactive corporate prototype.")
    st.image("https://images.unsplash.com/photo-1499856871958-5b9627545d1a", use_container_width=True)

# =========================================================
# IMPRINT PAGE
# =========================================================
elif current_page == "✦  Imprint":
    st.title("Imprint")
    st.write("Paris Destiny Agency | 123 Rue de la Paix, 75002 Paris, France")

# --- FOOTER DISPLAY ---
st.markdown("""
    <div class="custom-footer">
        <hr>
        <p>© 2026 <b>Paris Destiny Agency</b> | Premium Travel Consulting</p>
        <p style="font-style: italic; font-size: 0.75rem;">Created by Chenro & Darshan • All Rights Reserved</p>
    </div>
""", unsafe_allow_html=True)