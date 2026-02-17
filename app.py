import streamlit as st
import random
import time
import base64

# Mobile view setup
st.set_page_config(page_title="siva prediction", page_icon="💰🎯", layout="centered")

# --- Voice Function ---
def speak(text):
    # Text-to-Speech using a simple HTML5 hidden audio
    # Note: Browsers may block auto-play without user interaction
    b64 = base64.b64encode(text.encode()).decode()
    md = f"""
        <iframe allow="autoplay" src="https://translate.google.com/translate_tts?ie=UTF-8&q={text}&tl=ta&client=tw-ob" style="display:none"></iframe>
    """
    st.markdown(md, unsafe_allow_html=True)

# Custom UI Styling
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stStatusWidget"], [data-testid="stDecoration"] {
        visibility: hidden !important; display: none !important;
    }
    .viewerBadge_container_1QS1n, .viewerBadge_link_1wNoo { display: none !important; }

    @keyframes pulse-blue { 0% { transform: scale(1); } 70% { transform: scale(1.05); } 100% { transform: scale(1); } }
    @keyframes pulse-green { 0% { transform: scale(1); } 70% { transform: scale(1.05); } 100% { transform: scale(1); } }

    .stApp { background: linear-gradient(180deg, #0f0c29 0%, #302b63 50%, #24243e 100%); color: white; }
    .main-title { color: #00f2fe; text-align: center; font-size: 32px; font-weight: 900; margin-bottom: 10px; text-shadow: 2px 2px 10px #000; }
    .rules-box { background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #00ff00; margin-bottom: 20px; font-size: 14px; }
    
    label { color: #00f2fe !important; font-weight: bold !important; font-size: 16px !important; }
    input { color: black !important; font-weight: bold !important; font-size: 18px !important; }

    .stButton>button { width: 100%; border-radius: 50px; height: 3.5em; background: linear-gradient(45deg, #00ff00, #008000); color: black; font-weight: bold; font-size: 20px; border: none; }
    
    .status-display { padding: 15px; border-radius: 15px; text-align: center; font-size: 24px; font-weight: 900; margin-bottom: 10px; }
    .win-msg { background: rgba(0, 255, 0, 0.3); border: 2px solid #00ff00; color: #00ff00; }
    .loss-msg { background: rgba(255, 0, 0, 0.3); border: 2px solid #ff0000; color: #ff0000; }

    .reg-btn { display: block; background: #00ff00; color: black !important; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none; text-align: center; margin: 20px 0; animation: pulse-green 2s infinite; font-size: 18px; }
    .tg-btn { display: flex; align-items: center; justify-content: center; background: #0088cc; color: white !important; padding: 18px; border-radius: 15px; text-decoration: none; font-weight: 900; text-align: center; margin-top: 30px; animation: pulse-blue 2s infinite; border: 1px solid white; }
    .tg-icon { width: 25px; margin-right: 10px; }

    .result-box { padding: 25px; border-radius: 20px; border: 3px solid #00f2fe; background: rgba(0, 0, 0, 0.5); text-align: center; margin-top: 20px; }
    .level-text { background: #ffffff; color: #000000; padding: 10px 20px; border-radius: 10px; font-weight: 900; font-size: 20px; display: inline-block; }
    </style>
    """, unsafe_allow_html=True)

# Session State
if 'is_registered' not in st.session_state: st.session_state.is_registered = False
if 'level_count' not in st.session_state: st.session_state.level_count = 1
if 'last_prediction' not in st.session_state: st.session_state.last_prediction = ""

# --- Page 1: Registration ---
if not st.session_state.is_registered:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    st.markdown(f"""<div style='background: rgba(255,255,255,0.1); padding: 30px; border-radius: 20px; text-align: center; border: 2px solid #00ff00; margin-top: 20px;'><h2 style='color: #ffff00;'>⚠️ அனுமதி மறுக்கப்பட்டது</h2><p style='color: white;'>Predictor-ஐ பயன்படுத்த முதலில் கீழே உள்ள லிங்க்கில் Register செய்ய வேண்டும்.</p><a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" class="reg-btn">இங்கே கிளிக் செய்து பதிவிடவும்</a></div>""", unsafe_allow_html=True)
    if st.button("நான் பதிவு செய்துவிட்டேன் ✅"):
        st.session_state.is_registered = True
        # Voice alert for instructions
        speak("பதிவு செய்ததற்கு நன்றி. இப்போது கடந்த ஐந்து முடிவுகளை உள்ளிட்டு பலனை அறியவும். டெலிகிராம் சேனலில் இணைய மறக்காதீர்கள்.")
        st.rerun()

# --- Page 2: Predictor Interface ---
else:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    st.markdown("""<div class="rules-box">
    📢 <b>முக்கிய விதிகள்:</b><br>
    1. கடந்த 5 முடிவுகளை (B/S) சரியாக டைப் செய்யவும்.<br>
    2. 2-Level Martingale-ஐ பயன்படுத்தவும்.<br>
    3. 95% Accuracy வரும்போது மட்டும் விளையாடவும்.
    </div>""", unsafe_allow_html=True)

    history_raw = st.text_input("கடந்த 5 முடிவுகள் (Ex: BBSSS):", max_chars=5).upper()
    period_raw = st.text_input("அடுத்த பீரியட் எண் (3 Digits):", max_chars=3)

    if st.button("RESULT"):
        if (all(char in "BS" for char in history_raw) and len(history_raw) == 5) and (period_raw.isdigit() and len(period_raw) == 3):
            last_actual = "BIG" if history_raw[-1] == "B" else "SMALL"
            
            # Win/Loss Audio Alert
            if st.session_state.last_prediction != "":
                if last_actual == st.session_state.last_prediction:
                    st.markdown(f'<div class="status-display win-msg">LAST RESULT: WIN ✅</div>', unsafe_allow_html=True)
                    speak("வெற்றி கிடைத்துள்ளது. லெவல் ஒன்றுக்கு செல்லவும்.")
                    st.session_state.level_count = 1
                else:
                    st.markdown(f'<div class="status-display loss-msg">LAST RESULT: LOSS ❌</div>', unsafe_allow_html=True)
                    speak("இந்த முறை தோல்வி. அடுத்த லெவல் பயன்படுத்தவும்.")
                    st.session_state.level_count = st.session_state.level_count + 1 if st.session_state.level_count < 8 else 1
            
            # 2-Level Logic (Dragon/Alternate)
            if history_raw.endswith("BBB") or history_raw.endswith("SSS"):
                prediction = "BIG" if last_actual == "BIG" else "SMALL"
            else:
                prediction = "BIG" if last_actual == "SMALL" else "SMALL"
            
            st.session_state.last_prediction = prediction
            
            # Final Result Voice
            speak(f"அடுத்த கணிப்பு {prediction}. லெவல் {st.session_state.level_count}-ஐ பயன்படுத்தவும்.")
            
            accuracy = random.randint(95, 99)
            st.markdown(f"""
            <div class="result-box">
                <h3 style='color: #00f2fe; margin: 0;'>NEXT PREDICTION</h3>
                <h1 style='font-size: 80px; margin: 10px 0;'>{prediction}</h1>
                <div class="level-text">LEVEL {st.session_state.level_count} MAINTAIN PANU</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Inputs-ஐ சரியாக உள்ளிடவும்!")

    st.markdown("""<a href="https://t.me/toptamilearning100k" target="_blank" class="tg-btn"><img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" class="tg-icon">TELEGRAM சேனலில் இணையுங்கள்</a>""", unsafe_allow_html=True)
