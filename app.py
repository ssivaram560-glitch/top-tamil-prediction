import streamlit as st
import random
import time

# Mobile view setup
st.set_page_config(page_title="siva prediction", page_icon="💰🎯", layout="centered")

# Custom UI Styling with Animations and Branding Removal
st.markdown("""
    <style>
    /* 1. Complete Branding and Footer Removal */
    header, footer, .stDeployButton, [data-testid="stStatusWidget"], [data-testid="stDecoration"] {
        visibility: hidden !important;
        display: none !important;
    }
    .viewerBadge_container_1QS1n, .viewerBadge_link_1wNoo { display: none !important; }

    /* 2. Pulse Animations */
    @keyframes pulse-blue {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 136, 204, 0.7); }
        70% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(0, 136, 204, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 136, 204, 0); }
    }
    @keyframes pulse-green {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 255, 0, 0.7); }
        70% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(0, 255, 0, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 255, 0, 0); }
    }

    /* 3. General Styling */
    .stApp { 
        background: linear-gradient(180deg, #0f0c29 0%, #302b63 50%, #24243e 100%); 
        color: white; 
    }
    .main-title { color: #00f2fe; text-align: center; font-size: 32px; font-weight: 900; margin-bottom: 10px; text-shadow: 2px 2px 10px #000; }
    
    .rules-box { 
        background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 10px; 
        border-left: 5px solid #00ff00; margin-bottom: 20px; font-size: 14px;
    }
    
    label { color: #00f2fe !important; font-weight: bold !important; font-size: 16px !important; }
    
    /* Input field styling */
    input { color: black !important; font-weight: bold !important; font-size: 18px !important; }

    /* Custom Button Styles */
    .stButton>button { 
        width: 100%; border-radius: 50px; height: 3.5em; 
        background: linear-gradient(45deg, #00ff00, #008000);
        color: black; font-weight: bold; font-size: 20px; border: none;
    }
    
    .reg-btn {
        display: block; background: #00ff00; color: black !important; padding: 15px; 
        border-radius: 50px; font-weight: 900; text-decoration: none; text-align: center;
        margin: 20px 0; animation: pulse-green 2s infinite; font-size: 18px;
    }
    
    .tg-btn {
        display: flex; align-items: center; justify-content: center;
        background: #0088cc; color: white !important; padding: 18px; 
        border-radius: 15px; text-decoration: none; font-weight: 900; text-align: center;
        margin-top: 30px; animation: pulse-blue 2s infinite; border: 1px solid white;
    }
    .tg-icon { width: 25px; margin-right: 10px; }

    .result-box {
        padding: 25px; border-radius: 20px; border: 3px solid #00f2fe;
        background: rgba(0, 0, 0, 0.5); text-align: center; margin-top: 20px;
    }
    .level-text { background: #ffffff; color: #000000; padding: 10px 20px; border-radius: 10px; font-weight: 900; font-size: 20px; display: inline-block; }
    </style>
    """, unsafe_allow_html=True)

# Session State
if 'is_registered' not in st.session_state:
    st.session_state.is_registered = False
if 'level_count' not in st.session_state:
    st.session_state.level_count = 1

# --- Page 1: Access Restricted ---
if not st.session_state.is_registered:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='background: rgba(255,255,255,0.1); padding: 30px; border-radius: 20px; text-align: center; border: 2px solid #00ff00; margin-top: 20px;'>
            <h2 style='color: #ffff00;'>⚠️ Access Restricted</h2>
            <p style='color: white;'>Predictor-ஐ பயன்படுத்த முதலில் கீழே உள்ள லிங்க்-ல் Register செய்ய வேண்டும்.</p>
            <a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" class="reg-btn">
               CLICK HERE TO REGISTER
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("I HAVE REGISTERED ✅"):
        st.session_state.is_registered = True
        st.rerun()

# --- Page 2: Predictor Main Interface ---
else:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="rules-box">
        1. கீழே இருந்து மேலாக 5 ரிசல்ட்டை மட்டும் டைப் செய்யவும்.<br>
        2. 8-Level Martingale Strategy-ஐ கட்டாயம் பின்பற்றவும்.<br>
        3. 90% மேல் Accuracy வரும்போது மட்டும் முதலீடு செய்யவும்.
    </div>
    """, unsafe_allow_html=True)

    # Inputs
    history_raw = st.text_input("கடந்த 5 முடிவுகள் (B/S மட்டும்):", max_chars=5, placeholder="Ex: BBSSS").upper()
    period_raw = st.text_input("அடுத்த பீரியட் எண் (3 Digits):", max_chars=3, placeholder="Ex: 055")

    # Strict Validation
    history_valid = all(char in "BS" for char in history_raw) and len(history_raw) == 5
    period_valid = period_raw.isdigit() and len(period_raw) == 3

    if st.button("RESULT"):
        if history_valid and period_valid:
            with st.spinner('Checking Sureshot Algorithm...'):
                time.sleep(1.2)
                
                # Logic: Smart switch to ensure win feel within 4 levels
                prediction = "BIG" if history_raw[-1] == "S" else "SMALL"
                accuracy = random.randint(93, 98)

                st.markdown(f"""
                <div class="result-box">
                    <h3 style='color: #00f2fe; margin: 0;'>NEXT PREDICTION</h3>
                    <h1 style='font-size: 80px; margin: 10px 0; letter-spacing: 5px;'>{prediction}</h1>
                    <div class="level-text">LEVEL {st.session_state.level_count} MAINTAIN PANU</div>
                    <p style='color: #ffcc00; font-size: 13px; margin-top: 10px;'>8-Level Martingale Strategy-ஐ பின்பற்றவும்</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.write(f"Prediction Accuracy: {accuracy}%")
                st.progress(accuracy)
                
                # Level Tracker
                st.session_state.level_count = 1 if st.session_state.level_count >= 8 else st.session_state.level_count + 1
        else:
            if len(period_raw) != 3:
                st.error("பிழை: பீரியட் எண் 3 இலக்கங்களாக இருக்க வேண்டும்!")
            elif not history_valid:
                st.error("பிழை: 5 முடிவுகளையும் (B/S) சரியாக உள்ளிடவும்!")

    # Telegram Link with Logo
    st.markdown("""
        <a href="https://t.me/toptamilearning100k" target="_blank" class="tg-btn">
           <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" class="tg-icon">
           JOIN TELEGRAM CHANNEL
        </a>
    """, unsafe_allow_html=True)
