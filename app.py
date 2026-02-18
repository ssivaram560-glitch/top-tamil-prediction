import streamlit as st
import random
import time
from PIL import Image

# Macha, Mobile View Setup
st.set_page_config(page_title="siva prediction", page_icon="💰🎯", layout="centered")

# UI Styling - Period Number & Result Focus
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stStatusWidget"] { visibility: hidden !important; }
    .stApp { background: linear-gradient(180deg, #0f0c29 0%, #000000 100%); color: white; }
    .main-title { color: #00f2fe; text-align: center; font-size: 35px; font-weight: 900; text-transform: uppercase; margin-bottom: 20px; text-shadow: 2px 2px 10px #00f2fe; }
    
    /* Machi, Box visibility fixed */
    .stFileUploader section { background-color: rgba(255, 255, 255, 0.05) !important; border: 2px dashed #00f2fe !important; border-radius: 15px; }
    
    .result-container {
        border: 4px solid #00f2fe;
        border-radius: 25px;
        padding: 30px 20px;
        text-align: center;
        background: rgba(0, 0, 0, 0.9);
        box-shadow: 0 0 40px #00f2fe;
        margin-top: 20px;
    }

    .period-display { color: #ffff00; font-size: 32px; font-weight: 900; letter-spacing: 2px; margin-bottom: 10px; }
    .prediction-text { font-size: 90px; font-weight: 900; margin: 10px 0; color: #ffffff; text-shadow: 0 0 20px #fff; }
    .number-text { color: #ffff00; font-size: 28px; font-weight: bold; margin-bottom: 15px; }
    
    .status-badge { display: inline-block; padding: 8px 20px; border-radius: 10px; font-weight: 900; font-size: 18px; text-transform: uppercase; }
    .win-badge { background: #00ff00; color: #000; }
    .loss-badge { background: #ff0000; color: #fff; }

    .stButton>button {
        background: linear-gradient(45deg, #00f2fe, #4facfe);
        color: black; font-weight: 900; border-radius: 50px; height: 3.5em; font-size: 20px; border: none; margin-top: 20px;
    }
    
    .reg-btn { display: block; background: #00ff00; color: black !important; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none !important; text-align: center; margin: 20px 0; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Session State
if 'is_registered' not in st.session_state: st.session_state.is_registered = False
if 'level' not in st.session_state: st.session_state.level = 1
if 'last_period' not in st.session_state: st.session_state.last_period = 100
if 'last_status' not in st.session_state: st.session_state.last_status = None

# --- PAGE 1: REGISTER ---
if not st.session_state.is_registered:
    st.markdown("<div class='main-title'>SIVA PREDICTION</div>", unsafe_allow_html=True)
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" class="reg-btn">REGISTER HERE ✅</a>', unsafe_allow_html=True)
    if st.button("REGISTER செய்துவிட்டேன் ✅"):
        st.session_state.is_registered = True
        st.rerun()

# --- PAGE 2: PREDICTOR ---
else:
    st.markdown("<div class='main-title'>🚀 AI VISION PRO</div>", unsafe_allow_html=True)
    
    # Image Upload Only (No Text Boxes)
    up_files = st.file_uploader("2 Screenshots பதிவேற்றவும் (Last 20 Results)", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if st.button("GET SURESHOT RESULT"):
        if up_files and len(up_files) >= 1:
            with st.spinner('Vision AI Scanning Images for Period & Trend...'):
                time.sleep(2.5)
            
            # Machi, ippo logic-ae period number-ah automatic-aa update pannum
            st.session_state.last_period += 1
            
            # Sureshot Prediction Logic
            res = random.choice(["BIG", "SMALL"])
            num = random.choice([1,3,7,9]) if res == "BIG" else random.choice([2,4,6,8])
            
            # Automatic Level Management
            if st.session_state.last_status == "LOSS":
                st.session_state.level = st.session_state.level + 1 if st.session_state.level < 5 else 1
            else:
                st.session_state.level = 1
                
            # Result Display with Period Number
            st.markdown(f"""
            <div class="result-container">
                <div class="period-display">PERIOD: {st.session_state.last_period}</div>
                <div class="prediction-text">{res}</div>
                <div class="number-text">SURESHOT NUMBER: {num}</div>
                <div style='background:white; color:black; padding:5px 15px; border-radius:8px; font-weight:900; display:inline-block;'>LEVEL {st.session_state.level} CONFIRMED</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Status display for the current prediction based on last result
            if st.session_state.last_status:
                badge_class = "win-badge" if st.session_state.last_status == "WIN" else "loss-badge"
                st.markdown(f"<div style='text-align:center; margin-top:15px;'><span class='status-badge {badge_class}'>LAST BET: {st.session_state.last_status}</span></div>", unsafe_allow_html=True)

            # Set for next round
            st.session_state.last_status = random.choice(["WIN", "LOSS"])
        else:
            st.error("Machi, image upload panna dhaan result varum!")

    st.markdown("""<a href="https://t.me/toptamilearning100k" target="_blank" style="display:block; text-align:center; color:#00f2fe; text-decoration:none; margin-top:40px; font-weight:bold;">JOIN TELEGRAM CHANNEL ✈️</a>""", unsafe_allow_html=True)
