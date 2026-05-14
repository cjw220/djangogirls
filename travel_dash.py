import streamlit as st
import random
import time
from travel_data import TRAVEL_DATABASE

# --- CSS & THEMING ---
st.markdown("""
    <style>

    .main {
        background-color: #fafafa;
    }

    .stButton>button {
        background-color: #D4AF37;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }

    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Helvetica Neue', sans-serif;
    }

    footer {
        visibility: hidden;
    }

    .custom-footer {
        text-align: center;
        padding: 20px;
        color: #7f8c8d;
        font-size: 0.8rem;
    }

    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'result' not in st.session_state:
    st.session_state.result = None


# --- TOP NAVIGATION BAR ---
col1, col2, col3, col4, col5, col6 = st.columns([3,1,1,1,1,1])

with col1:
    st.markdown("## 🥐 Paris Destiny")

with col2:
    home_btn = st.button("Home")

with col3:
    about_btn = st.button("About")

with col4:
    services_btn = st.button("Services")

with col5:
    quiz_btn = st.button("Quiz")

with col6:
    contact_btn = st.button("Contact")
    # --- PAGE STATE ---
if 'menu' not in st.session_state:
    st.session_state.menu = "Home"

if home_btn:
    st.session_state.menu = "Home"

if about_btn:
    st.session_state.menu = "About"

if services_btn:
    st.session_state.menu = "Services"

if quiz_btn:
    st.session_state.menu = "Quiz"

if contact_btn:
    st.session_state.menu = "Contact"

menu = st.session_state.menu


# --- FUNCTIONS ---
def go_to_result(category):
    st.session_state.result = random.choice(TRAVEL_DATABASE[category])
    st.session_state.page = 'result'


def go_back():
    st.session_state.page = 'home'


# =========================================================
# HOME PAGE
# =========================================================
if menu == "🏠 Home":

    st.markdown("<h1>🥐 Paris Destiny Agency</h1>", unsafe_allow_html=True)

    st.markdown("### *AI-Powered Luxury Travel Consulting*")

    st.divider()

    st.subheader("Welcome to Paris Destiny Agency ✨")

    st.write("""
    Discover personalized Paris experiences powered by AI.

    Whether you dream of romantic evenings, hidden cafés,
    luxury shopping, artistic adventures, or unforgettable food tours,
    our agency helps you uncover your perfect Paris journey.
    """)

    st.image(
        "https://images.unsplash.com/photo-1502602898657-3e91760cbb34",
        caption="The beauty of Paris at sunset",
        use_container_width=True
    )

    st.divider()

    st.subheader("Why Choose Us?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Happy Travelers", "10,000+")

    with col2:
        st.metric("Hidden Cafés Explored", "250+")

    with col3:
        st.metric("Chance of Paris Drama", "99%")


# =========================================================
# ABOUT PAGE
# =========================================================
elif menu == "ℹ️ About Us":

    st.title("About Paris Destiny Agency")

    st.write("""
    Paris Destiny Agency is a fictional luxury travel company
    created as a graduation project.

    Our mission is to combine technology, humor,
    and travel inspiration into one interactive experience.

    We help travelers discover:
    - Romantic destinations
    - Hidden Paris cafés
    - Museum experiences
    - Luxury adventures
    - Fun local culture
    """)

    st.image(
        "https://images.unsplash.com/photo-1499856871958-5b9627545d1a",
        caption="Paris street life",
        use_container_width=True
    )


# =========================================================
# SERVICES PAGE
# =========================================================
elif menu == "✨ Services":

    st.title("Our Services")

    st.subheader("🥐 Luxury Food Tours")
    st.write("Discover hidden bakeries and iconic Paris cafés.")

    st.subheader("🎨 Art & Museum Experiences")
    st.write("Explore the Louvre and Parisian art culture.")

    st.subheader("🌃 Romantic Evening Walks")
    st.write("Private guided experiences around Paris at night.")

    st.subheader("🤖 AI Travel Matching")
    st.write("Receive personalized recommendations through our AI quiz.")

    st.image(
        "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f",
        caption="Luxury Paris Experience",
        use_container_width=True
    )


# =========================================================
# AI QUIZ PAGE
# =========================================================
elif menu == "🧠 AI Quiz":

    # ---------------- HOME QUIZ PAGE ----------------
    if st.session_state.page == 'home':

        st.markdown("<h1>🔮 Paris Destiny Quiz</h1>", unsafe_allow_html=True)

        st.markdown("### Discover your spiritual corner in Paris")

        st.divider()

        q1 = st.selectbox(
            "1. What kind of traveler are you?",
            [
                "(Funny) I survive on chaos and caffeine",
                "(Serious) Romantic explorer",
                "(Serious) Art and museum lover",
                "(Serious) Luxury traveler"
            ]
        )

        q2 = st.radio(
            "2. Your ideal Paris breakfast?",
            [
                "(Funny) Free hotel bread",
                "(Serious) Artisan croissant and coffee",
                "(Serious) Fancy rooftop brunch"
            ]
        )

        q3 = st.selectbox(
            "3. What is your vacation energy?",
            [
                "(Funny) Confused but trying my best",
                "(Serious) Elegant and classy",
                "(Serious) Adventure and exploration"
            ]
        )

        if st.button("🔮 Seek My Fortune"):

            funny_count = sum(
                1 for ans in [q1, q2, q3]
                if "(Funny)" in ans
            )

            category = "funny" if funny_count >= 1 else "serious"

            with st.spinner('Consulting the spirits of Paris...'):
                time.sleep(1.5)
                go_to_result(category)
                st.rerun()

    # ---------------- RESULT PAGE ----------------
    elif st.session_state.page == 'result':

        res = st.session_state.result

        st.markdown(
            f"<h1>🔮 Your Destiny: {res['place']}</h1>",
            unsafe_allow_html=True
        )

        st.image(
            res['img'],
            caption=f"View of {res['place']}",
            use_container_width=True
        )

        st.info(res['desc'])

        # Navigation Buttons
        col1, col2 = st.columns(2)

        with col1:
            if st.button("⬅️ Retake Quiz"):
                go_back()
                st.rerun()

        with col2:
            if 'url' in res:
                st.link_button("Official Info", res['url'])

        st.divider()

        # Contact Form
        st.subheader("📩 Book a Private Tour")

        with st.form("contact"):

            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            travelers = st.number_input(
                "Number of Travelers",
                min_value=1,
                max_value=20,
                value=2
            )

            notes = st.text_area("Any special requests?")

            if st.form_submit_button("Send to Consultant"):

                st.success(
                    f"Merci, {name}! "
                    f"We will contact you at {email} soon."
                )


# =========================================================
# CONTACT PAGE
# =========================================================
elif menu == "📩 Contact":

    st.title("Contact Us")

    st.write("""
    Have questions about your Paris adventure?
    Our consultants are here to help.
    """)

    with st.form("main_contact_form"):

        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success("Your message has been sent successfully!")


# =========================================================
# IMPRINT PAGE
# =========================================================
elif menu == "⚖️ Imprint":

    st.title("Imprint")

    st.write("""
    Paris Destiny Agency  
    123 Rue de la Paix  
    75002 Paris, France  

    Email: hello@parisdestinyagency.com  

    This website is a student graduation project.

    Image Sources:
    Unsplash.com
    """)


# =========================================================
# FOOTER
# =========================================================
st.markdown("""
    <div class="custom-footer">
        <hr>
        <p>
        <b>Paris Destiny Agency</b> |
        AI-Powered Luxury Travel Consulting
        </p>

        <p>
        Student Graduation Project • Built with Streamlit
        </p>
    </div>
""", unsafe_allow_html=True)
