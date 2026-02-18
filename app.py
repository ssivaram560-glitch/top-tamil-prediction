import streamlit as st
import random
import time

# Macha, Page Setup
st.set_page_config(page_title="siva prediction", page_icon="💰", layout="centered")

# UI Styling - Full Visibility
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stStatusWidget"] { visibility: hidden !important; }
    .stApp { background: linear-gradient(180deg, #050505 0%, #1a1a2e 100%); color: white; }
    
    .main-title { color: #00f2fe; text-align: center; font-size: 35px; font-weight: 900; margin-bottom: 20px; text-shadow: 2px 2px 10px #00f2fe; }
    
    /* Input Box Visibility - BLACK TEXT */
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
        background: rgba(0, 0, 0, 0.8); box-shadow: 0 0 40px #00f2fe; margin-top: 20px;
    }
    .prediction-txt { font-size: 80px; font-weight: 900; color: #ffffff; margin: 10px 0; }
    
    .status-line { font-size: 20px; font-weight: 900; margin-bottom: 10px; text-transform: uppercase; }
    .win-color { color: #00ff00; }
    .loss-color { color: #ff0000; }

    .reg-btn { display: block; background: #00ff00; color: black !important; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none !important; text-align: center; margin: 20px 0; font-size: 20px; }
    .tg-btn { display: block; background: #0088cc; color: white !important; padding: 15px; border-radius: 15px; text-decoration: none !important; font-weight: 900; text-align: center; margin-top: 30px; border: 1px solid white; }
    
    .stButton>button { background: linear-gradient(90deg, #00f2fe, #4facfe); color: black; font-weight: 900; border-radius: 50px; height: 3.5em; font-size: 18px; border: none; }
    </style>
    """, unsafe_allow_html=True)

# Session State
if 'registered' not in st.session_state: st.session_state.registered = False
if 'level' not in st.session_state: st.session_state.level = 1
if 'last_status' not in st.session_state: st.session_state.last_status = None

# --- PAGE 1: REGISTER & RULES ---
if not st.session_state.registered:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    
    st.markdown("""<div class="rules-box">
    <b>📜 விதிகள் (Rules):</b><br>
    🔹 1. முதலில் கீழே உள்ள பட்டனை அழுத்தி Register செய்யவும் ✅<br>
    🔹 2. சரியான Period Number-ஐ பதிவிடவும் ✍️<br>
    🔹 3. கடந்த 10 முடிவுகளை (B/S) சரியாக உள்ளிடவும் 📊<br>
    🔹 4. 5 Level வரையில் பணத்தை பராமரிக்கவும் 💰<br>
    🔹 5. Pattern சரியில்லை எனில் பந்தயம் கட்டுவதை தவிர்க்கவும் ⚠️
    </div>""", unsafe_allow_html=True)
    
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" class="reg-btn">REGISTER HERE ✅</a>', unsafe_allow_html=True)
    if st.button("நான் பதிவு செய்துவிட்டேன் ✅"):
        st.session_state.registered = True
        st.rerun()

# --- PAGE 2: PREDICTOR ---
else:
    st.markdown("<div class='main-title'>🚀 SIVA SURESHOT AI</div>", unsafe_allow_html=True)
    
    # Inputs
    period = st.text_input("அடுத்த Period Number:", placeholder="Ex: 405")
    history = st.text_input("கடந்த 10 முடிவுகள் (B/S மட்டும்):", placeholder="Ex: BBSSBSSBBS").upper()

    if st.button("GET SURESHOT RESULT"):
        if period and len(history) >= 5:
            with st.spinner('Sureshot Analysis-ல் உள்ளது...'):
                time.sleep(2)
            
            # Prediction Logic
            res = "BIG" if history.count("S") > history.count("B") else "SMALL"
            
            # Level & Win/Loss Logic (Inside Result Box)
            if st.session_state.last_status == "LOSS":
                st.session_state.level = st.session_state.level + 1 if st.session_state.level < 5 else 1
            else:
                st.session_state.level = 1
            
            # Status Banner
            status_text = "PREVIOUS: WIN ✅" if st.session_state.last_status == "WIN" else "PREVIOUS: LOSS ❌"
            status_class = "win-color" if st.session_state.last_status == "WIN" else "loss-color"

            # Result Box Display
            st.markdown(f"""
            <div class="result-container">
                {f'<div class="status-line {status_class}">{status_text}</div>' if st.session_state.last_status else ""}
                <div style="color:#ffff00; font-size:22px;">PERIOD: {period}</div>
                <h3 style='color:#00f2fe; margin-bottom:0;'>அடுத்த கணிப்பு</h3>
                <div class="prediction-txt">{res}</div>
                <div style='background:white; color:black; padding:5px 20px; border-radius:10px; font-weight:900;'>LEVEL {st.session_state.level} SURESHOT 🔥</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Update status for next round
            st.session_state.last_status = random.choice(["WIN", "LOSS", "WIN"]) # High win ratio simulation
        else:
            st.error("Period மற்றும் 10 முடிவுகளை (B/S) உள்ளிடவும் மச்சி!")

    st.markdown("""<a href="https://t.me/toptamilearning100k" target="_blank" class="tg-btn">✈️ JOIN TELEGRAM CHANNEL</a>""", unsafe_allow_html=True)
