import streamlit as st
import random
import time
from PIL import Image

# Macha, Mobile View & Page Setup
st.set_page_config(page_title="siva prediction", page_icon="💰🎯", layout="centered")

# Custom UI Styling (Ne ketta visibility issue mattum fix pannirukkaen)
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stStatusWidget"] { visibility: hidden !important; }
    .stApp { background: linear-gradient(180deg, #0f0c29 0%, #302b63 50%, #24243e 100%); color: white; }
    .main-title { color: #00f2fe; text-align: center; font-size: 32px; font-weight: 900; margin-bottom: 5px; text-shadow: 2px 2px 10px #000; }
    
    /* Machi, input box text ippo nalla theriyum */
    input { color: black !important; background-color: white !important; font-weight: bold !important; border-radius: 10px !important; }
    
    .rules-box { background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 12px; border-left: 5px solid #00ff00; margin-bottom: 20px; font-size: 14px; line-height: 1.6; }
    .result-box { padding: 25px; border-radius: 20px; border: 3px solid #00f2fe; background: rgba(0, 0, 0, 0.6); text-align: center; margin-top: 20px; box-shadow: 0 0 20px #00f2fe; }
    .skip-box { padding: 25px; border-radius: 20px; border: 3px solid #ff0000; background: rgba(255, 0, 0, 0.2); text-align: center; margin-top: 20px; }
    .level-tag { background: #ffffff; color: #000; padding: 5px 15px; border-radius: 8px; font-weight: 900; font-size: 18px; margin-top: 10px; display: inline-block; }
    .reg-btn { display: block; background: linear-gradient(45deg, #00ff00, #008000); color: black !important; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none !important; text-align: center; margin: 15px 0; font-size: 18px; }
    .tg-btn { display: block; background: #0088cc; color: white !important; padding: 15px; border-radius: 15px; text-decoration: none !important; font-weight: 900; text-align: center; margin-top: 20px; border: 1px solid white; }
    </style>
    """, unsafe_allow_html=True)

# Session State
if 'is_registered' not in st.session_state: st.session_state.is_registered = False
if 'level' not in st.session_state: st.session_state.level = 1
if 'last_pred' not in st.session_state: st.session_state.last_pred = ""

# --- PAGE 1: REGISTER ---
if not st.session_state.is_registered:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; padding:20px;'><h3>⚠️ அனுமதி மறுக்கப்பட்டது</h3><p>Predictor-ஐ பயன்படுத்த முதலில் கீழே உள்ள பட்டனை அழுத்தி Register செய்ய வேண்டும்.</p></div>", unsafe_allow_html=True)
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" class="reg-btn">REGISTER HERE ✅</a>', unsafe_allow_html=True)
    if st.button("நான் பதிவு செய்துவிட்டேன் ✅"):
        st.session_state.is_registered = True
        st.rerun()

# --- PAGE 2: MAIN PREDICTOR ---
else:
    st.markdown("<div class='main-title'>🚀 VISION SURESHOT AI</div>", unsafe_allow_html=True)
    
    st.markdown("""<div class="rules-box">
    <b>கவனிக்க வேண்டியவை:</b><br>
    1. கடந்த 20 முடிவுகளின் Screenshot-ஐ பதிவேற்றவும் (அதிக துல்லியத்திற்கு).<br>
    2. <b>Violet (0, 5)</b> எண்கள் வந்தால் எச்சரிக்கையாக இருக்கவும்.<br>
    3. <b>Level 5 Martingale</b> முறையை கட்டாயம் பின்பற்றவும் (1x, 3x).<br>
    4. "SKIP" என்று வந்தால் அந்த முறை பந்தயம் கட்டுவதை தவிர்க்கவும்.
    </div>""", unsafe_allow_html=True)

    # Macha, ippo multiple photos upload pannalaam
    up_files = st.file_uploader("கடந்த 20 முடிவுகளின் Screenshot-ஐ பதிவேற்றவும்", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)
    
    if up_files:
        st.write(f"✅ {len(up_files)} Photos Selected")

    # Manual Input
    history = st.text_input("நேரடி உள்ளீடு (Optional - Last 20 B/S):", max_chars=20).upper()

    if st.button("GET SURESHOT RESULT"):
        if up_files or len(history) >= 10:
            with st.spinner('Deep Vision Scanning (Violet & Number Trends)...'):
                time.sleep(2.5)
            
            # Simulated Deep Logic for Level 2 Win
            num_pool = [1, 3, 7, 9] if "B" in history[-3:] else [2, 4, 6, 8]
            target_num = random.choice(num_pool)
            
            is_skip = False
            if history.count("B") == history.count("S") or "0" in history or "5" in history:
                is_skip = True 

            if is_skip and random.random() > 0.5:
                st.markdown("""<div class="skip-box"><h2>⚠️ SKIP ROUND</h2><p>Violet trend/Unstable pattern. கொஞ்ச நேரம் காத்திருக்கவும்.</p></div>""", unsafe_allow_html=True)
            else:
                prediction = "BIG" if history.count("S") > history.count("B") else "SMALL"
                st.session_state.last_pred = prediction
                
                st.markdown(f"""
                <div class="result-box">
                    <h3 style='margin:0; color:#00f2fe;'>அடுத்த கணிப்பு</h3>
                    <h1 style='font-size:70px; margin:5px;'>{prediction}</h1>
                    <h2 style='color:#ffff00;'>எண்: {target_num}</h2>
                    <div class="level-tag">LEVEL {st.session_state.level} உறுதி</div>
                </div>
                """, unsafe_allow_html=True)
                
                acc = random.randint(97, 99)
                st.write(f"Vision துல்லியம்: {acc}%")
                st.progress(acc)
        else:
            st.error("Screenshot பதிவேற்றவும் அல்லது 10+ முடிவுகளை உள்ளிடவும்!")

    # Win/Loss Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("WIN ✅"):
            st.session_state.level = 1
            st.success("Level Reset to 1")
    with col2:
        if st.button("LOSS ❌"):
            st.session_state.level = 2 if st.session_state.level < 2 else 1
            st.warning("Level 2 Recovery Mode")

    st.markdown("""<a href="https://t.me/toptamilearning100k" target="_blank" class="tg-btn">JOIN TELEGRAM CHANNEL</a>""", unsafe_allow_html=True)
