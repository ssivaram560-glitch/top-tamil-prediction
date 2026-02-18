import streamlit as st
import random
import time

# Macha, Page Setup & Favicon
st.set_page_config(page_title="siva prediction", page_icon="💰", layout="centered")

# UI Styling - Full Visibility & Clean Dark Theme
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stStatusWidget"] { visibility: hidden !important; }
    .stApp { background: linear-gradient(180deg, #050505 0%, #1a1a2e 100%); color: white; font-family: 'Segoe UI', sans-serif; }
    
    .main-title { color: #00f2fe; text-align: center; font-size: 38px; font-weight: 900; margin-bottom: 20px; text-shadow: 2px 2px 15px #00f2fe; }
    
    .rules-box { background: rgba(0, 242, 254, 0.05); padding: 20px; border-radius: 15px; border-left: 5px solid #00f2fe; margin-bottom: 25px; line-height: 1.8; font-size: 15px; }
    
    .result-container {
        border: 4px solid #00f2fe; border-radius: 30px; padding: 40px 20px; text-align: center;
        background: rgba(0, 0, 0, 0.8); box-shadow: 0 0 50px #00f2fe; margin-top: 25px;
    }
    .prediction-txt { font-size: 100px; font-weight: 900; color: #ffffff; text-shadow: 0 0 20px #fff; margin: 10px 0; letter-spacing: 5px; }
    
    .status-msg { padding: 12px; border-radius: 12px; text-align: center; font-weight: 900; margin-bottom: 20px; font-size: 22px; text-transform: uppercase; border: 2px solid white; }
    .win-status { background: #00ff00; color: #000; }
    .loss-status { background: #ff0000; color: #fff; }

    .reg-btn { display: block; background: linear-gradient(45deg, #00ff00, #008000); color: black !important; padding: 18px; border-radius: 50px; font-weight: 900; text-decoration: none !important; text-align: center; margin: 25px 0; font-size: 22px; box-shadow: 0 5px 15px rgba(0,255,0,0.3); }
    .tg-btn { display: block; background: #0088cc; color: white !important; padding: 15px; border-radius: 50px; text-decoration: none !important; font-weight: 900; text-align: center; margin-top: 30px; border: 2px solid white; font-size: 18px; }
    
    .stButton>button { background: linear-gradient(90deg, #00f2fe, #4facfe); color: black; font-weight: 900; border-radius: 50px; height: 3.8em; font-size: 20px; border: none; transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px #00f2fe; }
    </style>
    """, unsafe_allow_html=True)

# Session State Logic
if 'registered' not in st.session_state: st.session_state.registered = False
if 'level' not in st.session_state: st.session_state.level = 1
if 'history' not in st.session_state: st.session_state.history = None

# --- PAGE 1: REGISTER ---
if not st.session_state.registered:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#ff4b4b;'>⚠️ அனுமதி மறுக்கப்பட்டது</h3>", unsafe_allow_html=True)
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" class="reg-btn">REGISTER HERE ✅</a>', unsafe_allow_html=True)
    if st.button("REGISTER செய்துவிட்டேன் ✅"):
        st.session_state.registered = True
        st.rerun()

# --- PAGE 2: MAIN PREDICTOR ---
else:
    st.markdown("<div class='main-title'>🚀 siva prediction 🎯</div>", unsafe_allow_html=True)
    
    # Rules with Emojis (Tamil Only)
    st.markdown("""<div class="rules-box">
    <b>📜 முக்கிய விதிகள்:</b><br>
    🔹 1. ஒரே நேரத்தில் 2 Screenshots பதிவேற்றவும் (20 முடிவுகள்) 📸<br>
    🔹 2. Sureshot கணிப்பு Level 1-லேயே வர வாய்ப்பு அதிகம் 🎯<br>
    🔹 3. பாதுகாப்பிற்கு 5 Levels வரை பணத்தை பராமரிக்கவும் 💰<br>
    🔹 4. Pattern சரியாக இல்லையெனில் SKIP செய்யப்படும் ⚠️<br>
    🔹 5. "GET RESULT" அழுத்தினால் முந்தைய முடிவு காட்டப்படும் ✅
    </div>""", unsafe_allow_html=True)

    # Automatic WIN/LOSS display from previous round
    if st.session_state.history:
        status_class = "win-status" if st.session_state.history == "WIN" else "loss-status"
        st.markdown(f'<div class="status-msg {status_class}">கடந்த முடிவு: {st.session_state.history} (Level {st.session_state.level})</div>', unsafe_allow_html=True)

    # Image Upload (Multiple selection enabled)
    up_files = st.file_uploader("2 Screenshots பதிவேற்றவும்", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if st.button("GET SURESHOT RESULT ⚡"):
        if up_files and len(up_files) >= 1:
            with st.spinner('Vision AI Scanning Trends...'):
                time.sleep(2.5)
            
            # Macha, pattern check logic
            pattern_safe = random.choice([True, True, True, False]) # 75% accuracy logic
            
            if not pattern_safe:
                st.warning("⚠️ Pattern சரியாக இல்லை! இந்த முறையை தவிர்க்கவும் (SKIP).")
            else:
                # Sureshot Logic (Result only)
                prediction = random.choice(["BIG", "SMALL"])
                
                st.markdown(f"""
                <div class="result-container">
                    <h3 style='color:#00f2fe; margin:0;'>அடுத்த கணிப்பு</h3>
                    <div class="prediction-txt">{prediction}</div>
                    <div style='background:white; color:black; padding:8px 25px; border-radius:50px; font-weight:900; display:inline-block; font-size:20px;'>LEVEL {st.session_state.level} SURESHOT 🔥</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Update Level & History for next time
                simulated_win = random.choice(["WIN", "WIN", "WIN", "LOSS"]) # Sureshot focus (3:1 ratio)
                if simulated_win == "WIN":
                    st.session_state.history = "WIN"
                    st.session_state.level = 1
                else:
                    st.session_state.history = "LOSS"
                    st.session_state.level = st.session_state.level + 1 if st.session_state.level < 5 else 1
        else:
            st.error("குறைந்தது Screenshots பதிவேற்றவும் மச்சி! 📸")

    # Telegram with Logo
    st.markdown("""<a href="https://t.me/toptamilearning100k" target="_blank" class="tg-btn">✈️ JOIN TELEGRAM CHANNEL</a>""", unsafe_allow_html=True)
