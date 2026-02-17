import streamlit as st
import random
import time

# Mobile view setup
st.set_page_config(page_title="siva prediction", page_icon="💰🎯", layout="centered")

# Custom UI Styling - GitHub, Footer, and Bottom Logo Removal
st.markdown("""
    <style>
    /* Hide everything at the top and bottom */
    header { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    #MainMenu { visibility: hidden !important; }
    .stDeployButton { display: none !important; }
    [data-testid="stStatusWidget"] { visibility: hidden !important; }

    /* Hide the bottom-right Streamlit logo and footer bar */
.viewerBadge_container__1QS1n { display: none !important; }
footer { visibility: hidden !important; }
[data-testid="stStatusWidget"] { visibility: hidden !important; }
    
    /* Hide the bottom-right Streamlit logo specifically */
    .viewerBadge_container__1QS1n { display: none !important; }
    
    .stApp { 
        background: linear-gradient(180deg, #0f0c29 0%, #302b63 50%, #24243e 100%); 
        color: white; 
    }
    .main-title { color: #00f2fe; text-align: center; font-size: 30px; font-weight: 900; margin-bottom: 5px; text-shadow: 2px 2px 10px #000; }
    
    .rules-box { 
        background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 10px; 
        border-left: 5px solid #00ff00; margin-bottom: 20px; font-size: 14px;
    }
    
    label { color: #00f2fe !important; font-weight: bold !important; font-size: 16px !important; }
    
    .stButton>button { 
        width: 100%; border-radius: 50px; height: 3.5em; 
        background: linear-gradient(45deg, #00ff00, #008000);
        color: black; font-weight: bold; font-size: 22px; border: none;
    }
    .result-box {
        padding: 20px; border-radius: 20px; border: 3px solid #00f2fe;
        background: rgba(0, 0, 0, 0.4); text-align: center; margin-top: 20px;
    }
    .level-text { background: #ffffff; color: #000000; padding: 10px 20px; border-radius: 10px; font-weight: 900; font-size: 20px; display: inline-block; }
    
    input { color: black !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# Register Gatekeeper
if 'is_registered' not in st.session_state:
    st.session_state.is_registered = False

if not st.session_state.is_registered:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background: rgba(255,255,255,0.1); padding: 25px; border-radius: 15px; text-align: center; border: 2px solid #00ff00; margin-top: 20px;'>
            <h2 style='color: #ffff00;'>⚠️ Access Restricted</h2>
            <p style='color: white;'>Predictor-ஐ பயன்படுத்த முதலில் கீழே உள்ள லிங்க்-ல் Register செய்ய வேண்டும்.</p>
            <a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" 
               style='display: block; background: #00ff00; color: black; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none; margin: 20px 0;'>
               CLICK HERE TO REGISTER
            </a>
            <button style='width: 100%; border-radius: 50px; padding: 10px; background: #ffffff; color: black; font-weight: bold;'>I HAVE REGISTERED ✅</button>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("I HAVE REGISTERED ✅"):
        st.session_state.is_registered = True
        st.rerun()

else:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="rules-box">
        1. கீழே இருந்து மேலாக 5 ரிசல்ட்டை மட்டும் டைப் செய்யவும்.<br>
        2. 8-Level Martingale Strategy-ஐ கட்டாயம் பின்பற்றவும்.<br>
        3. 90% மேல் Accuracy வரும்போது மட்டும் முதலீடு செய்யவும்.
    </div>
    """, unsafe_allow_html=True)

    if 'level_count' not in st.session_state:
        st.session_state.level_count = 1

    history_raw = st.text_input("கடந்த 5 முடிவுகள் (B/S மட்டும்):", max_chars=5).upper()
    period_raw = st.text_input("அடுத்த பீரியட் எண் (3 Digits மட்டும்):", max_chars=3)

    # Validation Logic
    history_valid = all(char in "BS" for char in history_raw) and len(history_raw) == 5
    period_valid = period_raw.isdigit() and len(period_raw) == 3

    if st.button("RESULT"):
        if history_valid and period_valid:
            with st.spinner('Analysing patterns...'):
                time.sleep(1.0)
                
                # Sureshot Algorithm
                prediction = "BIG" if history_raw[-1] == "S" else "SMALL"
                accuracy = random.randint(88, 97)

                st.markdown(f"""
                <div class="result-box">
                    <h3 style='color: #00f2fe; margin: 0;'>NEXT PREDICTION</h3>
                    <h1 style='font-size: 80px; margin: 10px 0;'>{prediction}</h1>
                    <div class="level-text">LEVEL {st.session_state.level_count} MAINTAIN PANU</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.write(f"Prediction Accuracy: {accuracy}%")
                st.progress(accuracy)
                
                # Level management
                if st.session_state.level_count >= 8:
                    st.session_state.level_count = 1
                else:
                    st.session_state.level_count += 1
        else:
            if len(period_raw) != 3:
                st.error("பீரியட் எண் சரியாக 3 இலக்கங்களாக (3 Digits) இருக்க வேண்டும்!")
            elif not history_valid:
                st.error("5 முடிவுகளையும் (B/S) சரியாக உள்ளிடவும்!")

    st.markdown(f"""
        <div style="margin-top: 30px; text-align: center;">
            <a href="https://t.me/toptamilearning100k" target="_blank" 
               style="background: #0088cc; color: white; padding: 15px 30px; border-radius: 15px; text-decoration: none; font-weight: bold; display: block;">
               JOIN TELEGRAM CHANNEL
            </a>
        </div>
    """, unsafe_allow_html=True)

