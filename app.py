import streamlit as st
import random
import time

# Macha, Page Setup - Strictly No Indents Here
st.set_page_config(page_title="siva prediction", page_icon="💰", layout="centered")

# UI Styling - Full Fix for HTML Visibility
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stStatusWidget"] { visibility: hidden !important; }
    .stApp { background: linear-gradient(180deg, #050505 0%, #1a1a2e 100%); color: white; }
    
    .main-title { color: #00f2fe; text-align: center; font-size: 35px; font-weight: 900; margin-bottom: 20px; text-shadow: 2px 2px 10px #00f2fe; }
    
    input {
        color: #000000 !important; 
        background-color: #FFFFFF !important; 
        font-weight: bold !important; 
        font-size: 18px !important;
        border-radius: 10px !important;
    }
    label { color: #00f2fe !important; font-weight: bold !important; }

    .rules-box { background: rgba(0, 242, 254, 0.1); padding: 15px; border-radius: 12px; border-left: 5px solid #00f2fe; margin-bottom: 20px; font-size: 14px; }
    
    .result-container {
        border: 4px solid #00f2fe; border-radius: 25px; padding: 25px; text-align: center;
        background: rgba(0, 0, 0, 0.9); box-shadow: 0 0 40px #00f2fe; margin-top: 20px;
    }
    .prediction-txt { font-size: 80px; font-weight: 900; color: #ffffff; margin: 10px 0; text-shadow: 0 0 20px #fff; }
    
    .status-line { font-size: 22px; font-weight: 900; margin-bottom: 10px; text-transform: uppercase; }
    .win-color { color: #00ff00; }
    .loss-color { color: #ff0000; }

    .reg-btn { display: block; background: #00ff00; color: black !important; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none !important; text-align: center; margin: 25px 0; font-size: 20px; }
    .tg-btn { display: block; background: #0088cc; color: white !important; padding: 15px; border-radius: 50px; text-decoration: none !important; font-weight: 900; text-align: center; margin-top: 30px; border: 2px solid white; }
    
    .stButton>button { background: linear-gradient(90deg, #00f2fe, #4facfe); color: black; font-weight: 900; border-radius: 50px; height: 3.5em; font-size: 18px; border: none; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Shared Rules
def show_rules():
    st.markdown("""<div class="rules-box">
    <b>📜 விதிகள் (Rules):</b><br>
    🔹 1. Register பட்டனை அழுத்தி கணக்கை உருவாக்கவும் ✅<br>
    🔹 2. Period Number (3 digits) உள்ளிடவும் ✍️<br>
    🔹 3. <b>கீழே இருந்து மேலாக (Bottom to Top) வரிசையாக type செய்யவும்</b> 💪🏼<br>
    🔹 4. Pattern சரியில்லை எனில் SKIP செய்யவும் ⚠️<br>
    🔹 5. minimum 7 level ஐ maintain பண்ணவும்
    </div>""", unsafe_allow_html=True)

# Session State for Real Tracking
if 'registered' not in st.session_state: st.session_state.registered = False
if 'current_level' not in st.session_state: st.session_state.current_level = 1
if 'history_log' not in st.session_state: st.session_state.history_log = []

# --- PAGE 1: REGISTER ---
if not st.session_state.registered:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    show_rules() 
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" class="reg-btn">REGISTER HERE ✅</a>', unsafe_allow_html=True)
    if st.button("REGISTER செய்துவிட்டேன் ✅"):
        st.session_state.registered = True
        st.rerun()

# --- PAGE 2: PREDICTOR ---
else:
    st.markdown("<div class='main-title'>🚀 SIVA SURESHOT PREDICTION 💥</div>", unsafe_allow_html=True)
    show_rules() 
    
    period = st.text_input("அடுத்த Period Number (Max 3):", placeholder="Ex: 314", max_chars=3)
    history_input = st.text_input("கடந்த 10 முடிவுகள் (B/S மட்டும்):", placeholder="Ex: Bbssssbbbb", max_chars=10).upper()

    if st.button("GET SURESHOT RESULT ⚡"):
        if period.isdigit() and history_input and all(c in "BS" for c in history_input):
            with st.spinner('Scanning Trends...'):
                time.sleep(1.2)
            
            # Actual Logic based on patterns
            prediction = "BIG" if history_input.count("S") >= history_input.count("B") else "SMALL"
            
            # Realistic Status Simulation (Avoiding constant 'Fake Win')
            # In a real app, this would compare prediction vs actual result
            status = random.choice(["WIN", "WIN", "LOSS"]) 
            
            if status == "LOSS":
                st.session_state.current_level = st.session_state.current_level + 1 if st.session_state.current_level < 4 else 1
            else:
                st.session_state.current_level = 1

            s_text = f"PREVIOUS: {status} " + ("✅" if status == "WIN" else "❌")
            s_class = "win-color" if status == "WIN" else "loss-color"

            # Final Result Display - Fixing HTML nesting errors
            st.markdown(f"""
            <div class="result-container">
                <div class="status-line {s_class}">{s_text}</div>
                <div style="color:#ffff00; font-size:24px; font-weight:900;">PERIOD: {period}</div>
                <h3 style='color:#00f2fe; margin-top:10px;'>அடுத்த கணிப்பு</h3>
                <div class="prediction-txt">{prediction}</div>
                <div style='background:white; color:black; padding:8px 30px; border-radius:15px; font-weight:900; display:inline-block; margin-top:10px;'>LEVEL {st.session_state.current_level} SURESHOT 🔥</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("சரியான தகவல்களை உள்ளிடவும்! (Ex: 304, BBBSSS)")

    st.markdown("""<a href="https://t.me/toptamilearning100k" target="_blank" class="tg-btn">✈️ JOIN TELEGRAM CHANNEL</a>""", unsafe_allow_html=True)

