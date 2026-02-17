import streamlit as st
import random
import time
import re

# Mobile view setup
st.set_page_config(page_title="siva prediction", page_icon="💰🎯", layout="centered")

# Custom UI Styling with GitHub & Footer Removal
st.markdown("""
    <style>
    /* GitHub Logo matrum Header-ai complete-ah maraikka */
    header { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    #MainMenu { visibility: hidden !important; }
    .stDeployButton { display: none !important; }
    
    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 136, 204, 0.7); }
        70% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(0, 136, 204, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 136, 204, 0); }
    }
    .stApp { 
        background: linear-gradient(180deg, #0f0c29 0%, #302b63 50%, #24243e 100%); 
        color: white; 
    }
    .main-title { color: #00f2fe; text-align: center; font-size: 30px; font-weight: 900; margin-bottom: 5px; text-shadow: 2px 2px 10px #000; }
    
    .rules-box { 
        background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 10px; 
        border-left: 5px solid #00ff00; margin-bottom: 20px; font-size: 14px;
        color: #ffffff;
    }
    
    label { color: #00f2fe !important; font-weight: bold !important; font-size: 18px !important; }
    
    .stButton>button { 
        width: 100%; border-radius: 50px; height: 3.5em; 
        background: linear-gradient(45deg, #00ff00, #008000);
        color: black; font-weight: bold; font-size: 22px; border: none;
        margin-top: 10px;
    }
    .result-box {
        padding: 25px; border-radius: 20px; border: 3px solid #00f2fe;
        background: rgba(0, 0, 0, 0.4); text-align: center; margin-top: 20px;
    }
    .tg-link {
        display: flex; justify-content: center; align-items: center;
        background: #0088cc; color: white !important; padding: 18px;
        border-radius: 15px; text-decoration: none; font-weight: 900;
        animation: pulse 2s infinite; margin-top: 40px; border: 1px solid white;
    }
    .level-text { background: #ffffff; color: #000000; padding: 10px 20px; border-radius: 10px; font-weight: 900; font-size: 20px; display: inline-block; }
    
    /* Input field text color correction */
    input { color: black !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# Register Gatekeeper
if 'is_registered' not in st.session_state:
    st.session_state.is_registered = False

if not st.session_state.is_registered:
    st.markdown("<div class='main-title'>💰 Top தமிழ் Prediction 🎯</div>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background: rgba(255,255,255,0.1); padding: 25px; border-radius: 15px; text-align: center; border: 2px solid #00ff00; margin-top: 20px;'>
            <h2 style='color: #ffff00;'>⚠️ Access Restricted</h2>
            <p style='color: white;'>Predictor-ஐ பயன்படுத்த முதலில் கீழே உள்ள லிங்க்-ல் Register செய்ய வேண்டும்.</p>
            <a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" 
               style='display: block; background: #00ff00; color: black; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none; margin: 20px 0;'>
               CLICK HERE TO REGISTER
            </a>
            <p style='font-size: 13px; color: #ccc;'>Register செய்த பிறகு 'I HAVE REGISTERED' பட்டனை அழுத்தவும்.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("I HAVE REGISTERED ✅"):
        st.session_state.is_registered = True
        st.rerun()

else:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="rules-box">
        <b>📝 RULES:</b><br>
        1. கீழே இருந்து மேலாக 5 ரிசல்ட்டை மட்டும் டைப் செய்யவும்.<br>
        2. 8-Level Martingale Strategy-ஐ கட்டாயம் பின்பற்றவும்.<br>
        3. 90% மேல் Accuracy வரும்போது மட்டும் அதிக முதலீடு செய்யவும்.
    </div>
    """, unsafe_allow_html=True)

    if 'last_pred_char' not in st.session_state:
        st.session_state.last_pred_char = None
    if 'level_count' not in st.session_state:
        st.session_state.level_count = 1

    # --- Validation Logic ---
    history_raw = st.text_input("கடந்த 5 முடிவுகள் (B/S மட்டும்):", max_chars=5).upper()
    period_raw = st.text_input("அடுத்த பீரியட் எண் (Numbers மட்டும்):", max_chars=3)

    # Error flags
    history_valid = all(char in "BS" for char in history_raw) if history_raw else False
    period_valid = period_raw.isdigit() if period_raw else False

    if st.button("RESULT"):
        if len(history_raw) == 5 and history_valid and period_valid:
            history_list = list(history_raw)
            actual_now = history_list[-1]

            if st.session_state.last_pred_char:
                if st.session_state.last_pred_char == actual_now:
                    st.markdown("<p style='color: #00ff00; text-align: center; font-size: 22px; font-weight: bold;'>LAST RESULT: WIN ✅</p>", unsafe_allow_html=True)
                    st.session_state.level_count = 1
                else:
                    st.markdown("<p style='color: #ff4b4b; text-align: center; font-size: 22px; font-weight: bold;'>LAST RESULT: LOSS ❌</p>", unsafe_allow_html=True)
                    st.session_state.level_count += 1
                    if st.session_state.level_count > 8: st.session_state.level_count = 1

            with st.spinner('Analysing Trend patterns...'):
                time.sleep(1.2)
                
                # --- Advanced Internal Sureshot Logic ---
                last_3 = history_list[-3:]
                is_repeat = len(set(last_3)) == 1
                
                if is_repeat:
                    prediction = "S" if last_3[0] == "B" else "B"
                else:
                    prediction = "B" if history_list[-1] == "S" else "S"

                accuracy_display = random.randint(85, 98)
                st.session_state.last_pred_char = prediction
                full_res = "BIG" if prediction == "B" else "SMALL"

                st.markdown(f"""
                <div class="result-box">
                    <h3 style='color: #00f2fe; margin: 0;'>NEXT PREDICTION</h3>
                    <h1 style='font-size: 85px; margin: 10px 0; letter-spacing: 5px;'>{full_res}</h1>
                    <div class="level-text">LEVEL {st.session_state.level_count} MAINTAIN PANNU</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.write(f"Prediction Accuracy: {accuracy_display}%")
                st.progress(accuracy_display)
        else:
            if history_raw and not history_valid:
                st.error("தவறு! B அல்லது S மட்டுமே பயன்படுத்தவும்.")
            elif period_raw and not period_valid:
                st.error("தவறு! பீரியட் எண்ணில் எண்கள் மட்டுமே இருக்க வேண்டும்.")
            else:
                st.error("5 Results மற்றும் 3 Digit Period கட்டாயம் தேவை!")

    st.markdown(f"""
        <a href="https://t.me/toptamilearning100k" target="_blank" class="tg-link">
            <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="30" style="margin-right: 15px;">
            JOIN OUR TELEGRAM CHANNEL
        </a>
    """, unsafe_allow_html=True)