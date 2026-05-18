import streamlit as st
import random
import time
from travel_data import TRAVEL_DATABASE

# --- 1. DEFINE NAVIGATION MAPS ---
# Pure minimalist style per TA specifications
PAGES = [
    "✦  Home",
    "✦  Services",
    "✦  Destiny Quiz",
    "✦  Contact",
    "✦  About Us",
    "✦  Imprint"
]

# Internal tracking keys for language-independent routing
TABS = ["home", "services", "quiz", "contact", "about", "imprint"]

# --- 2. INITIALIZE SESSION STATE ---
# FIX: Unified state tracking variable to 'current_tab' to prevent AttributeError
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = "home" 

if 'page' not in st.session_state:
    st.session_state.page = 'home' 

if 'result' not in st.session_state:
    st.session_state.result = None

# --- 3. CSS & THEMING (PARISIAN CHIC EDITION) ---
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

/* Force base canvas background to luxury dusty rose */
[data-testid="stAppViewContainer"] {
    background-color: #F5EBE6 !important;
}

/* Eradicate white header banner constraint */
header[data-testid="stHeader"] {
    background-color: transparent !important;
    background: transparent !important;
}

h1, h2, h3, .stSubheader p {
    font-family: 'Playfair Display', serif !important;
    color: #1A1A2E !important;
    font-weight: 700 !important;
}

h1 { letter-spacing: -0.5px; font-size: 3rem !important; }

/* PREMIUM SIDEBAR */
section[data-testid="stSidebar"] {
    background: #12121F !important;
    border-right: 1px solid rgba(0,0,0,0.05);
    padding-top: 20px;
}

/* Hide Streamlit radio decoration elements inside sidebar */
section[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
    display: none !important;
}
section[data-testid="stSidebar"] .stRadio > label {
    display: none !important;
}

/* Sidebar navigation item spacing and fonts */
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
section[data-testid="stSidebar"] div[role="radiogroup"] label p,
section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p {
    color: #EAEAEA !important;
    font-family: 'Playfair Display', serif !important;
    letter-spacing: 0.5px;
}

/* Hover effects */
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background-color: rgba(255, 255, 255, 0.05) !important;
    transform: translateX(6px);
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover p {
    color: #C5A059 !important;
}

/* Active navigation tab highlight overlay */
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

.block-container { padding-top: 3rem; }

/* VINTAGE CHAMPAGNE GOLD BUTTONS */
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

.custom-footer { text-align: center; padding: 30px 20px; color: #8A8A9A; font-size: 0.8rem; font-family: 'Montserrat', sans-serif; }
.custom-footer hr { border-top: 1px solid rgba(0,0,0,0.05); margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR CONTROLLERS (LANGUAGE & ROUTING) ---
st.sidebar.markdown("<p style='font-size:14px; opacity:0.6; margin-bottom:-5px;'>✦ LANGUAGE / LANGUE</p>", unsafe_allow_html=True)
lang_label = st.sidebar.selectbox("LangSelector", ["English", "Français"], label_visibility="collapsed")
lang = "EN" if lang_label == "English" else "FR"

# Pure multilingual dictionary configuration
TXT = {
    "EN": {
        "nav_home": "✦  Home",
        "nav_services": "✦  Services",
        "nav_quiz": "✦  Destiny Quiz",
        "nav_contact": "✦  Contact",
        "nav_about": "✦  About Us",
        "nav_imprint": "✦  Imprint",
        
        "title": "✦ Paris Destiny Agency",
        "subtitle": "### *Bespoke Destiny Orchestration & Premium Survival Consulting*",
        "welcome_h": "Welcome to Paris Destiny Agency",
        "welcome_b": "Discover personalized Paris experiences powered by advanced intelligence. Whether you dream of romantic evenings, hidden cafés, or luxury adventures, our agency helps you uncover your perfect Paris journey (and successfully survive local facial expressions).",
        "cta_btn": "Begin Your Destiny Match",
        "metric_1": "Happy Travelers",
        "metric_2": "Hidden Cafés Explored",
        "metric_3": "Chance of Paris Drama",
        "metric_3_val": "99.9%",
        
        "services_title": "Our Bespoke Services",
        "s1_h": "✦  Bespoke Carbohydrate Overload Tours",
        "s1_b": "Discover hidden multi-generational bakeries, iconic cafés, and master the survival art of looking fiercely Parisian while eating a buttery, dangerously flaky croissant.",
        "s2_h": "✦  Curated Fine Art & Smart Crowd Navigation",
        "s2_b": "Explore the Louvre Museum. Our elite guides teach you how to position your body perfectly to view the Mona Lisa's left eyebrow through a forest of 500 smartphones.",
        "s3_h": "✦  Exclusive Midnight Promenades",
        "s3_b": "Private guided experiences around dark, romantic Parisian alleyways. Raincoats are not included but emotionally highly recommended.",
        "s4_h": "✦  Algorithmic Destiny Alignment",
        "s4_b": "Receive tailored travel recommendations driven by our highly speculative cosmological-computational Python framework.",
        
        "quiz_title": "✦  Paris Destiny Quiz",
        "quiz_subtitle": "### Let our algorithm judge your spiritual corner in Paris",
        "q1_label": "1. What kind of traveler are you?",
        "q1_opts": ["I survive on existential dread, chaos and caffeine", "Romantic explorer chasing old ghosts", "Art lover pretending to understand cubism", "Luxury traveler with someone else's credit card"],
        "q2_label": "2. Your ideal Paris breakfast?",
        "q2_opts": ["Free, stale hotel bread hidden in my bag", "Artisan croissant and an overpriced espresso", "Fancy rooftop brunch to make my ex jealous"],
        "q3_label": "3. What is your current vacation energy?",
        "q3_opts": ["Completely confused but trying my absolute best", "Elegant, classy, and mildly judgmental", "Adventure, exploration, and ignoring my bank app"],
        "quiz_btn": "Consult the Spirits of Paris",
        "quiz_spinner": "Consulting the ghosts of French philosophers...",
        "result_title": "✦  Your Appointed Destiny",
        "retake_btn": "Retake Quiz (Try to be richer)",
        "booking_h": "✦  Secure an Elite Private Tour (Before you regret it)",
        "booking_btn": "Surrender Data to Consultant",
        "booking_success": "Merci, {}! Our consultants are already arguing about your lifestyle choices. We will contact you at {} shortly.",
        
        "contact_title": "Contact Our Headquarters",
        "contact_subtitle": "Send us a message. We promise to reply slower than a French waiter, but with double the style.",
        "contact_btn": "Send Message into the Void",
        "contact_success": "Success! Your message has been safely fired into the Parisian bureaucracy.",
        
        "about_title": "About the Agency",
        "about_b": "Paris Destiny Agency is a premium interactive corporate prototype combining state-of-the-art software engineering, severe caffeine dependencies, and luxury travel marketing simulations.",
        "imprint_title": "Corporate Imprint",
        "footer_text": "© 2026 <b>Paris Destiny Agency</b> | Premium Algorithmic Travel Orchestration",
        "footer_credits": "Built with blood, sweat, and stale croissants by Chenro & Darshan • All Rights Reserved"
    },
    "FR": {
        "nav_home": "✦  Accueil",
        "nav_services": "✦  Services Premium",
        "nav_quiz": "✦  Bilan de Destin",
        "nav_contact": "✦  Contact",
        "nav_about": "✦  À Propos",
        "nav_imprint": "✦  Mentions Légales",
        
        "title": "✦ Agence Destin Paris",
        "subtitle": "### *Orchestration de Destin Sur-Mesure & Conseil en Survivance*",
        "welcome_h": "Bienvenue à l'Agence Destin Paris",
        "welcome_b": "Découvrez des expériences parisiennes personnalisées, propulsées par une intelligence artificielle hautement spéculative. Que vous rêviez de soirées romantiques ou d'aventures luxueuses, notre agence vous aide à révéler votre voyage parfait (et à survivre aux expressions faciales des locaux).",
        "cta_btn": "Révéler Mon Destin",
        "metric_1": "Voyageurs Heureux",
        "metric_2": "Cafés Cachés Explorés",
        "metric_3": "Risque de Crise de Nerfs",
        "metric_3_val": "99.9%",
        
        "services_title": "Nos Services Exclusifs",
        "s1_h": "✦  Surcharge de Glucides Sur-Mesure",
        "s1_b": "Découvrez des boulangeries ancestrales et apprenez l'art de paraître intensément parisien tout en perdant la moitié de votre croissant en miettes sur votre veste.",
        "s2_h": "✦  Art Raffiné & Gestion Élitaire des Foules",
        "s2_b": "Explorez le musée du Louvre. Nos guides vous apprennent à vous positionner stratégiquement pour admirer le sourcil gauche de la Joconde à travers 500 smartphones.",
        "s3_h": "✦  Promenades Nocturnes Exclusives",
        "s3_b": "Expériences privées dans les ruelles sombres et romantiques de Paris. Imperméables non inclus mais fortement recommandés pour votre santé mentale.",
        "s4_h": "✦  Alignement Algorithmique du Destin",
        "s4_b": "Recevez des recommandations de voyage dictées par notre framework Python cosmologico-informatique exclusif.",
        
        "quiz_title": "✦  Le Quiz du Destin Parisien",
        "quiz_subtitle": "### Laissez notre algorithme juger votre âme voyageuse",
        "q1_label": "1. Quel genre de voyageur êtes-vous ?",
        "q1_opts": ["Je survis grâce à l'angoisse existentielle, au chaos et au café", "Explorateur romantique à la recherche de fantômes", "Amateur d'art prétendant comprendre le cubisme", "Voyageur de luxe utilisant la carte de crédit de quelqu'un d'autre"],
        "q2_label": "2. Votre petit-déjeuner parisien idéal ?",
        "q2_opts": ["Le pain rassis et gratuit de l'hôtel caché dans mon sac", "Un croissant artisanal et un expresso hors de prix", "Un brunch chic sur un rooftop pour rendre mon ex jaloux"],
        "q3_label": "3. Quelle est votre énergie de vacances actuelle ?",
        "q3_opts": ["Complètement confus mais je fais de mon mieux", "Élégant, classique et légèrement méprisant", "Aventure, exploration et ignorance totale de mon solde bancaire"],
        "quiz_btn": "Consulter les Esprits de Paris",
        "quiz_spinner": "Consultation des fantômes des philosophes français...",
        "result_title": "✦  Votre Destin Assigné",
        "retake_btn": "Recommencer le Quiz (Essayez d'être plus riche)",
        "booking_h": "✦  Réserver une Visite Privée (Avant de le regretter)",
        "booking_btn": "Abandonner mes Données au Consultant",
        "booking_success": "Merci, {} ! Nos consultants se disputent déjà sur vos choix de vie. Nous vous contacterons à {} sous peu.",
        
        "contact_title": "Contacter le Quartier Général",
        "contact_subtitle": "Envoyez-nous un message. Nous promettons de répondre plus lentement qu'un serveur parisien, mais avec deux fois plus de style.",
        "contact_btn": "Envoyer le Message dans le Vide",
        "contact_success": "Succès ! Votre message a été injecté avec succès dans la bureaucratie française.",
        
        "about_title": "À Propos de l'Agence",
        "about_b": "L'Agence Destin Paris est un prototype d'entreprise premium combinant ingénierie logicielle avancée, dépendance sévère à la caféine et simulations marketing de luxe.",
        "imprint_title": "Mentions Légales",
        "footer_text": "© 2026 <b>Paris Destiny Agency</b> | Orchestration de Voyage Algorithmique Premium",
        "footer_credits": "Créé avec du sang, de la sueur et des croissants rassis par Chenro & Darshan • Tous droits réservés"
    }
}

# Sync page labels dynamically based on state array
PAGES_DISPLAY = [
    TXT[lang]["nav_home"],
    TXT[lang]["nav_services"],
    TXT[lang]["nav_quiz"],
    TXT[lang]["nav_contact"],
    TXT[lang]["nav_about"],
    TXT[lang]["nav_imprint"]
]

# FIX: Safely retrieve tracking index from TABS using synchronized variable
nav_index = TABS.index(st.session_state.current_tab)
chosen_page_label = st.sidebar.radio("Navigation", PAGES_DISPLAY, index=nav_index, key="sidebar_nav")

# Write current tab cleanly to session state
st.session_state.current_tab = TABS[PAGES_DISPLAY.index(chosen_page_label)]
current_page = st.session_state.current_tab

def go_to_result(category):
    st.session_state.result = random.choice(TRAVEL_DATABASE[category])
    st.session_state.page = 'result'

def go_back():
    st.session_state.page = 'home'

# =========================================================
# HOME PAGE VIEW LAYER
# =========================================================
if current_page == "home":
    st.markdown(f"<h1>{TXT[lang]['title']}</h1>", unsafe_allow_html=True)
    st.markdown(TXT[lang]['subtitle'])
    st.divider()
    
    st.subheader(TXT[lang]['welcome_h'])
    st.write(TXT[lang]['welcome_b'])

    if st.button(TXT[lang]['cta_btn']):
        st.session_state.current_tab = "quiz"
        st.rerun()

    st.image(
        "https://images.unsplash.com/photo-1502602898657-3e91760cbb34",
        caption="Paris, France",
        use_container_width=True
    )
    st.divider()
    
    st.subheader("Key Global Metrics")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric(TXT[lang]['metric_1'], "10,000+")
    with col2: st.metric(TXT[lang]['metric_2'], "250+")
    with col3: st.metric(TXT[lang]['metric_3'], TXT[lang]['metric_3_val'])

# =========================================================
# SERVICES PAGE VIEW LAYER
# =========================================================
elif current_page == "services":
    st.title(TXT[lang]['services_title'])
    
    st.subheader(TXT[lang]['s1_h'])
    st.write(TXT[lang]['s1_b'])
    
    st.subheader(TXT[lang]['s2_h'])
    st.write(TXT[lang]['s2_b'])
    
    st.subheader(TXT[lang]['s3_h'])
    st.write(TXT[lang]['s3_b'])
    
    st.subheader(TXT[lang]['s4_h'])
    st.write(TXT[lang]['s4_b'])
    
    st.image("https://images.unsplash.com/photo-1511739001486-6bfe10ce785f", use_container_width=True)

# =========================================================
# DESTINY QUIZ VIEW LAYER
# =========================================================
elif current_page == "quiz":
    
    if st.session_state.page == 'home':
        st.markdown(f"<h1>{TXT[lang]['quiz_title']}</h1>", unsafe_allow_html=True)
        st.markdown(TXT[lang]['quiz_subtitle'])
        st.divider()
        
        q1 = st.selectbox(TXT[lang]['q1_label'], TXT[lang]['q1_opts'])
        q2 = st.radio(TXT[lang]['q2_label'], TXT[lang]['q2_opts'])
        q3 = st.selectbox(TXT[lang]['q3_label'], TXT[lang]['q3_opts'])

        if st.button(TXT[lang]['quiz_btn']):
            q1_idx = TXT[lang]['q1_opts'].index(q1)
            q2_idx = TXT[lang]['q2_opts'].index(q2)
            q3_idx = TXT[lang]['q3_opts'].index(q3)
            
            funny_count = 0
            if q1_idx == 0: funny_count += 1
            if q2_idx == 0: funny_count += 1
            if q3_idx == 0: funny_count += 1
            
            category = "funny" if funny_count >= 1 else "serious"
            
            with st.spinner(TXT[lang]['quiz_spinner']):
                time.sleep(1.5)
                go_to_result(category)
                st.rerun()

    elif st.session_state.page == 'result':
        res = st.session_state.result
        st.markdown(f"<h1>{TXT[lang]['result_title']}: {res['place']}</h1>", unsafe_allow_html=True)
        st.image(res['img'], caption=res['place'], use_container_width=True)
        st.info(res['desc'])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button(TXT[lang]['retake_btn']):
                go_back()
                st.rerun()
        with col2:
            if 'url' in res: st.link_button("Official Info", res['url'])
            
        st.divider()
        
        st.subheader(TXT[lang]['booking_h'])
        with st.form("contact"):
            name = st.text_input("Full Name", placeholder="e.g., Jean-Pierre")
            email = st.text_input("Email Address", placeholder="name@luxury-traveler.com")
            st.text_area("Special Requests", placeholder="e.g., Please ensure the local pigeons do not recognize my face.")
            if st.form_submit_button(TXT[lang]['booking_btn']):
                st.success(TXT[lang]['booking_success'].format(name, email))

# =========================================================
# CONTACT PAGE VIEW LAYER
# =========================================================
elif current_page == "contact":
    st.title(TXT[lang]['contact_title'])
    st.write(TXT[lang]['contact_subtitle'])
    
    with st.form("main_contact_form"):
        name = st.text_input("Full Name", placeholder="e.g., Amélie Poulain")
        email = st.text_input("Email Address")
        st.text_area("Your Message")
        if st.form_submit_button(TXT[lang]['contact_btn']):
            st.success(TXT[lang]['contact_success'])

# =========================================================
# ABOUT PAGE VIEW LAYER
# =========================================================
elif current_page == "about":
    st.title(TXT[lang]['about_title'])
    st.write(TXT[lang]['about_b'])
    st.image("https://images.unsplash.com/photo-1499856871958-5b9627545d1a", use_container_width=True)

# =========================================================
# IMPRINT PAGE VIEW LAYER
# =========================================================
elif current_page == "imprint":
    st.title(TXT[lang]['imprint_title'])
    st.write("Paris Destiny Agency | 123 Rue de la Paix, 75002 Paris, France")

# --- FOOTER DISPLAY ---
st.markdown(f"""
    <div class="custom-footer">
        <hr>
        <p>{TXT[lang]['footer_text']}</p>
        <p style="font-style: italic; font-size: 0.75rem;">{TXT[lang]['footer_credits']}</p>
    </div>
""", unsafe_allow_html=True)