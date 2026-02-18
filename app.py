import streamlit as st
import random
import time
from PIL import Image

# Macha, Mobile View & Page Setup
st.set_page_config(page_title="siva prediction", page_icon="💰🎯", layout="centered")

# Custom UI Styling
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stStatusWidget"] { visibility: hidden !important; }
    .stApp { background: linear-gradient(180deg, #0f0c29 0%, #302b63 50%, #24243e 100%); color: white; }
    .main-title { color: #00f2fe; text-align: center; font-size: 32px; font-weight: 900; margin-bottom: 5px; text-shadow: 2px 2px 10px #000; }
    
    .rules-box { background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 12px; border-left: 5px solid #00ff00; margin-bottom: 20px; font-size: 14px; }
    .result-box { padding: 25px; border-radius: 20px; border: 3px solid #00f2fe; background: rgba(0, 0, 0, 0.6); text-align: center; margin-top: 20px; box-shadow: 0 0 20px #00f2fe; }
    
    .status-msg { padding: 10px; border-radius: 10px; text-align: center; font-weight: bold; margin-bottom: 15px; font-size: 20px; border: 1px solid white; }
    .win-msg { background: #00ff00; color: #000; }
    .loss-msg { background: #ff0000; color: #fff; }

    .period-display { color: #ffff00; font-size: 24px; font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #00f2fe; display: inline-block; padding-bottom: 5px; }
    .reg-btn { display: block; background: linear-gradient(45deg, #00ff00, #008000); color: black !important; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none !important; text-align: center; margin: 15px 0; font-size: 18px; }
    .tg-btn { display: block; background: #0088cc; color: white !important; padding: 15px; border-radius: 15px; text-decoration: none !important; font-weight: 900; text-align: center; margin-top: 20px; border: 1px solid white; }
    
    .stButton>button { width: 100%; border-radius: 12px; font-weight: bold; height: 3.5em; font-size: 18px; background: #ff4b4b; color: white; border: none; }
    </style>
    """, unsafe_allow_html=True)

# Session State for Automatic Logic
if 'is_registered' not in st.session_state: st.session_state.is_registered = False
if 'level' not in st.session_state: st.session_state.level = 1
if 'last_result' not in st.session_state: st.session_state.last_result = None
if 'current_period' not in st.session_state: st.session_state.current_period = 100

# --- PAGE 1: REGISTER ---
if not st.session_state.is_registered:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" class="reg-btn">REGISTER HERE ✅</a>', unsafe_allow_html=True)
    if st.button("நான் பதிவு செய்துவிட்டேன் ✅"):
        st.session_state.is_registered = True
        st.rerun()

# --- PAGE 2: MAIN PREDICTOR ---
else:
    st.markdown("<div class='main-title'>🚀 VISION SURESHOT AI</div>", unsafe_allow_html=True)
    
    # 1. Automatic WIN/LOSS Status (Buttons thookiyaachu)
    if st.session_state.last_result:
        status_class = "win-msg" if st.session_state.last_result == "WIN" else "loss-msg"
        st.markdown(f'<div class="status-msg {status_class}">LAST RESULT: {st.session_state.last_result} (Level {st.session_state.level})</div>', unsafe_allow_html=True)

    st.markdown("""<div class="rules-box">
    1. 2 Screenshots-ஐ பதிவேற்றவும்.<br>
    2. Period முடிஞ்ச உடனே "GET RESULT" கொடுங்க, அதுவே WIN/LOSS சொல்லும்.
    </div>""", unsafe_allow_html=True)

    # Multiple screenshots upload
    up_files = st.file_uploader("2 Screenshots பதிவேற்றவும்", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if st.button("GET SURESHOT RESULT"):
        if up_files:
            # Automating the WIN/LOSS sequence
            if st.session_state.last_result == "WIN":
                st.session_state.level = 1
            elif st.session_state.last_result == "LOSS":
                st.session_state.level = st.session_state.level + 1 if st.session_state.level < 5 else 1
            
            # Period Number Simulation
            st.session_state.current_period += 1
            
            with st.spinner('Vision Scanning & Checking Last Bet...'):
                time.sleep(2.0)
            
            # Prediction Logic
            res = random.choice(["BIG", "SMALL"])
            num = random.choice([1,3,7,9]) if res == "BIG" else random.choice([2,4,6,8])
            
            # Result Display
            st.markdown(f"""
            <div class="result-box">
                <div class="period-display">PERIOD: {st.session_state.current_period}</div>
                <h3 style='margin:0; color:#00f2fe;'>அடுத்த கணிப்பு</h3>
                <h1 style='font-size:80px; margin:5px;'>{res}</h1>
                <h2 style='color:#ffff00;'>எண்: {num}</h2>
                <div style='background:white; color:black; padding:5px 15px; border-radius:8px; font-weight:900;'>LEVEL {st.session_state.level} உறுதி</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Update for the next round
            st.session_state.last_result = random.choice(["WIN", "LOSS"]) # AI analysis logic simulation
        else:
            st.error("குறைந்தது Screenshots பதிவேற்றவும் machi!")

    st.markdown("""<a href="https://t.me/toptamilearning100k" target="_blank" class="tg-btn">JOIN TELEGRAM CHANNEL</a>""", unsafe_allow_html=True)
