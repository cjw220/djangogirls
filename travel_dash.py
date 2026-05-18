import streamlit as st
import random
import time
from travel_data import TRAVEL_DATABASE

# --- 1. DEFINE NAVIGATION ORDER (PAGES) ---
# Ordered per user requirements: Home, Services, AI Quiz, Contact, About Us, Imprint
PAGES = [
    "🏠 Home",
    "✨ Services",
    "🧠 AI Quiz",
    "📩 Contact",
    "ℹ️ About Us",
    "⚖️ Imprint"
]

# --- 2. INITIALIZE SESSION STATE ---
if 'menu_selection' not in st.session_state:
    st.session_state.menu_selection = PAGES[0] # Default selected page is Home

if 'page' not in st.session_state:
    st.session_state.page = 'home' # Internal sub-page state for the AI Quiz routing

if 'result' not in st.session_state:
    st.session_state.result = None

# --- 3. NAVIGATION SYNC FUNCTION ---
def sync_nav():
    """Sync menu selection state when the sidebar is clicked manually"""
    st.session_state.menu_selection = st.session_state.sidebar_nav

# --- 4. CSS & THEMING ---
st.markdown("""
    <style>
/* PREMIUM SIDEBAR STYLE */
section[data-testid="stSidebar"] {
    background: #151524;
    border-right: 1px solid rgba(255,255,255,0.05);
    padding-top: 40px;
}

/* 💡 FIX: Only hide radio button circles inside the sidebar */
section[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
    display: none;
}

/* Remove Navigation title styling */
section[data-testid="stSidebar"] .stRadio > label {
    display: none;
}

/* 💡 FIX: Style configurations applied exclusively to sidebar options */
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    padding: 14px 18px;
    margin-bottom: 12px;
    border-radius: 14px;
    font-size: 20px !important;
    font-weight: 700 !important;
    color: #F5F5F5 !important;
    transition: all 0.25s ease;
}

/* 💡 FIX: Hover animation effect exclusive to sidebar items */
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background-color: rgba(255,255,255,0.06);
    transform: translateX(4px);
}

/* 💡 FIX: Active selected state styling exclusive to sidebar items */
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background-color: rgba(255,255,255,0.08);
    border-left: 3px solid white;
    padding-left: 20px;
}

/* General layout adjustments and hiding redundant elements */
[data-baseweb="tooltip"], [data-testid="collapsedControl"], span.material-symbols-rounded {
    display: none !important;
}

section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] div, section[data-testid="stSidebar"] p {
    color: white;
    font-family: 'Helvetica Neue', sans-serif;
}

.stButton>button {
    background-color: #D4AF37;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 12px 24px;
    font-weight: bold;
    width: auto;
}

h1, h2, h3 { color: #2c3e50; font-family: 'Helvetica Neue', sans-serif; }
footer { visibility: hidden; }
.custom-footer { text-align: center; padding: 20px; color: #7f8c8d; font-size: 0.8rem; }
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

# Drive the view layout based on the current active page
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
if current_page == "🏠 Home":
    st.markdown("<h1>🥐 Paris Destiny Agency</h1>", unsafe_allow_html=True)
    st.markdown("### *AI-Powered Luxury Travel Consulting*")
    st.divider()
    
    st.subheader("Welcome to Paris Destiny Agency ✨")
    st.write("""
    Discover personalized Paris experiences powered by AI.
    Whether you dream of romantic evenings, hidden cafés, or luxury adventures,
    our agency helps you uncover your perfect Paris journey.
    """)

    # 🚀 CTA Button: Route user straight to the AI Quiz page
    if st.button("✨ Try Our AI Quiz Now!"):
        st.session_state.menu_selection = "🧠 AI Quiz"
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
elif current_page == "✨ Services":
    st.title("Our Services")
    st.subheader("🥐 Luxury Food Tours")
    st.write("Discover hidden bakeries and iconic Paris cafés.")
    st.subheader("🎨 Art & Museum Experiences")
    st.write("Explore the Louvre and Parisian art culture.")
    st.subheader("🌃 Romantic Evening Walks")
    st.write("Private guided experiences around Paris at night.")
    st.subheader("🤖 AI Travel Matching")
    st.write("Receive personalized recommendations through our AI quiz.")
    st.image("https://images.unsplash.com/photo-1511739001486-6bfe10ce785f", use_container_width=True)

# =========================================================
# AI QUIZ PAGE
# =========================================================
elif current_page == "🧠 AI Quiz":
    
    # ---- QUIZ INPUT INTERFACE ----
    if st.session_state.page == 'home':
        st.markdown("<h1>🔮 Paris Destiny Quiz</h1>", unsafe_allow_html=True)
        st.markdown("### Discover your spiritual corner in Paris")
        st.divider()
        q1 = st.selectbox("1. What kind of traveler are you?", ["I survive on chaos and caffeine", "Romantic explorer", "Art and museum lover", "Luxury traveler"])
        q2 = st.radio("2. Your ideal Paris breakfast?", ["Free hotel bread", "Artisan croissant and coffee", "Fancy rooftop brunch"])
        q3 = st.selectbox("3. What is your vacation energy?", ["Confused but trying my best", "Elegant and classy", "Adventure and exploration"])

        if st.button("🔮 Seek My Fortune"):
            # Internal keywords to match funny/chaotic user selections
            funny_options = ["I survive on chaos and caffeine", "Free hotel bread", "Confused but trying my best"]
            funny_count = sum(1 for ans in [q1, q2, q3] if ans in funny_options)
            category = "funny" if funny_count >= 1 else "serious"
            
            with st.spinner('Consulting the spirits of Paris...'):
                time.sleep(1.5)
                go_to_result(category)
                st.rerun()

    # ---- QUIZ MATCHING RESULT PAGE ----
    elif st.session_state.page == 'result':
        res = st.session_state.result
        st.markdown(f"<h1>🔮 Your Destiny: {res['place']}</h1>", unsafe_allow_html=True)
        st.image(res['img'], caption=f"View of {res['place']}", use_container_width=True)
        st.info(res['desc'])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Retake Quiz"):
                go_back()
                st.rerun()
        with col2:
            if 'url' in res: st.link_button("Official Info", res['url'])
            
        st.divider()
        
        # Embedded Booking Form
        st.subheader("📩 Book a Private Tour")
        with st.form("contact"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            if st.form_submit_button("Send to Consultant"):
                st.success(f"Merci, {name}! We will contact you at {email} soon.")

# =========================================================
# CONTACT PAGE
# =========================================================
elif current_page == "📩 Contact":
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
elif current_page == "ℹ️ About Us":
    st.title("About Paris Destiny Agency")
    st.write("We combine technology and travel inspiration into one interactive experience.")
    st.image("https://images.unsplash.com/photo-1499856871958-5b9627545d1a", use_container_width=True)

# =========================================================
# IMPRINT PAGE
# =========================================================
elif current_page == "⚖️ Imprint":
    st.title("Imprint")
    st.write("Paris Destiny Agency | 123 Rue de la Paix, 75002 Paris, France")

# --- FOOTER DISPLAY ---
st.markdown('<div class="custom-footer"><hr><p><b>Paris Destiny Agency</b> | Student Project</p></div>', unsafe_allow_html=True)