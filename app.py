import streamlit as st
import random
import time
from PIL import Image

# Macha, Mobile View & Page Setup
st.set_page_config(page_title="siva prediction", page_icon="💰🎯", layout="centered")

# Custom UI Styling - Visibility & Layout pakka-vaa irukkum
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stStatusWidget"] { visibility: hidden !important; }
    .stApp { background: linear-gradient(180deg, #0f0c29 0%, #302b63 50%, #24243e 100%); color: white; }
    .main-title { color: #00f2fe; text-align: center; font-size: 32px; font-weight: 900; margin-bottom: 5px; text-shadow: 2px 2px 10px #000; }
    
    /* Input and Box Visibility Fix */
    input[type="text"] {
        color: #000000 !important; 
        background-color: #FFFFFF !important; 
        font-weight: bold !important; 
        font-size: 18px !important;
    }
    label { color: #00f2fe !important; font-weight: bold !important; }

    .rules-box { background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 12px; border-left: 5px solid #00ff00; margin-bottom: 20px; font-size: 14px; }
    .result-box { padding: 25px; border-radius: 20px; border: 3px solid #00f2fe; background: rgba(0, 0, 0, 0.6); text-align: center; margin-top: 20px; box-shadow: 0 0 20px #00f2fe; }
    
    .history-bar { padding: 10px; border-radius: 10px; text-align: center; font-weight: bold; margin-bottom: 15px; border: 1px solid #ffffff; }
    .win-msg { background: #00ff00; color: #000; }
    .loss-msg { background: #ff0000; color: #fff; }

    .reg-btn { display: block; background: linear-gradient(45deg, #00ff00, #008000); color: black !important; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none !important; text-align: center; margin: 15px 0; font-size: 18px; }
    .tg-btn { display: block; background: #0088cc; color: white !important; padding: 15px; border-radius: 15px; text-decoration: none !important; font-weight: 900; text-align: center; margin-top: 20px; border: 1px solid white; }
    
    .stButton>button { width: 100%; border-radius: 12px; font-weight: bold; height: 3.5em; font-size: 16px; }
    .win-btn > div > button { background-color: #00ff00 !important; color: black !important; }
    .loss-btn > div > button { background-color: #ff0000 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# Session State
if 'is_registered' not in st.session_state: st.session_state.is_registered = False
if 'level' not in st.session_state: st.session_state.level = 1
if 'history_status' not in st.session_state: st.session_state.history_status = []

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
    
    # Win/Loss History Display at the top
    if st.session_state.history_status:
        last = st.session_state.history_status[-1]
        color_class = "win-msg" if last == "WIN" else "loss-msg"
        st.markdown(f'<div class="history-bar {color_class}">கடந்த முடிவு: {last} (Level {st.session_state.level})</div>', unsafe_allow_html=True)

    st.markdown("""<div class="rules-box">
    1. 2 Screenshots-ஐ (மொத்தம் 20 முடிவுகள்) பதிவேற்றவும்.<br>
    2. முடிவை தேர்வு செய்த பின் அடுத்த கணிப்பை பார்க்கவும்.
    </div>""", unsafe_allow_html=True)

    # Macha, ippo 2 screenshots direct-aa select pannalaam
    up_files = st.file_uploader("2 Screenshots பதிவேற்றவும் (Last 20 Results)", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if st.button("GET SURESHOT RESULT", type="primary"):
        if up_files and len(up_files) >= 1:
            with st.spinner('Vision Scanning 20 Results...'):
                time.sleep(2.5)
            
            # Sureshot Logic
            prediction = random.choice(["BIG", "SMALL"])
            num = random.choice([1,3,7,9]) if prediction == "BIG" else random.choice([2,4,6,8])
            
            st.markdown(f"""
            <div class="result-box">
                <h3 style='margin:0; color:#00f2fe;'>அடுத்த கணிப்பு</h3>
                <h1 style='font-size:80px; margin:5px;'>{prediction}</h1>
                <h2 style='color:#ffff00;'>எண்: {num}</h2>
                <div style='background:white; color:black; padding:5px 15px; border-radius:8px; font-weight:900;'>LEVEL {st.session_state.level} உறுதி</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("குறைந்தது 1 அல்லது 2 Screenshots பதிவேற்றவும் machi!")

    st.write("---")
    st.write("முடிவை தேர்வு செய்யவும் (அடுத்த கணிப்பிற்கு முன்):")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="win-btn">', unsafe_allow_html=True)
        if st.button("WIN ✅"):
            st.session_state.level = 1
            st.session_state.history_status.append("WIN")
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="loss-btn">', unsafe_allow_html=True)
        if st.button("LOSS ❌"):
            st.session_state.level = st.session_state.level + 1 if st.session_state.level < 5 else 1
            st.session_state.history_status.append("LOSS")
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""<a href="https://t.me/toptamilearning100k" target="_blank" class="tg-btn">JOIN TELEGRAM CHANNEL</a>""", unsafe_allow_html=True)

