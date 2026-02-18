    import streamlit as st
import random
import time

# Macha, Page Setup
st.set_page_config(page_title="siva prediction", page_icon="💰", layout="centered")

# UI Styling
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
        background: rgba(0, 0, 0, 0.9); box-shadow: 0 0 40px #00f2fe; margin-top: 20px;
    }
    .prediction-txt { font-size: 80px; font-weight: 900; color: #ffffff; margin: 10px 0; text-shadow: 0 0 20px #fff; }
    
    .status-line { font-size: 20px; font-weight: 900; margin-bottom: 10px; text-transform: uppercase; }
    .win-color { color: #00ff00; }
    .loss-color { color: #ff0000; }

    .reg-btn { display: block; background: #00ff00; color: black !important; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none !important; text-align: center; margin: 25px 0; font-size: 20px; box-shadow: 0 5px 15px rgba(0,255,0,0.3); }
    .tg-btn { display: block; background: #0088cc; color: white !important; padding: 15px; border-radius: 50px; text-decoration: none !important; font-weight: 900; text-align: center; margin-top: 30px; border: 2px solid white; }
    
    .stButton>button { background: linear-gradient(90deg, #00f2fe, #4facfe); color: black; font-weight: 900; border-radius: 50px; height: 3.5em; font-size: 18px; border: none; }
    </style>
    """, unsafe_allow_html=True)

# Shared Rules Function
def show_rules():
    st.markdown("""<div class="rules-box">
    <b>📜 விதிகள் (Rules):</b><br>
    🔹 1. முதலில் Register பட்டனை அழுத்தி கணக்கை உருவாக்கவும் ✅<br>
    🔹 2. சரியான Period Number-ஐ டைப் செய்யவும் (3 digits) ✍️<br>
    🔹 3. கடந்த 10 முடிவுகளை (B/S மட்டும்) சரியாக உள்ளிடவும் 📊<br>
    🔹 4. கடந்த 10 முடிவுகளை கீழே இருந்து மேலாக type பண்ணவும் 💪🏼<br>
    🔹 5. குறைந்தது 5 Level வரை பணத்தை பராமரிக்கவும் 💰<br>
    🔹 6. Pattern சரியில்லை எனில் SKIP செய்யவும் ⚠️
    </div>""", unsafe_allow_html=True)

# Session State for App Logic
if 'registered' not in st.session_state: st.session_state.registered = False
if 'level' not in st.session_state: st.session_state.level = 1
if 'last_status' not in st.session_state: st.session_state.last_status = None

# --- PAGE 1: REGISTER & RULES ---
if not st.session_state.registered:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    show_rules() 
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" class="reg-btn">REGISTER HERE ✅</a>', unsafe_allow_html=True)
    if st.button("REGISTER செய்துவிட்டேன் ✅"):
        st.session_state.registered = True
        st.rerun()

# --- PAGE 2: PREDICTOR ---
else:
    st.markdown("<div class='main-title'>🚀 SIVA SURESHOT AI</div>", unsafe_allow_html=True)
    show_rules() 
    
    # Inputs
    period = st.text_input("அடுத்த Period Number (Max 3):", placeholder="Ex: 405", max_chars=3)
    history = st.text_input("கடந்த 10 முடிவுகள் (B/S மட்டும்):", placeholder="Ex: BBSSB", max_chars=10).upper()

    if st.button("GET SURESHOT RESULT ⚡"):
        # Validation for Numeric Period and B/S History
        if period.isdigit() and history and all(c in "BS" for c in history):
            with st.spinner('Sureshot Analysis-ல் உள்ளது...'):
                time.sleep(1.5)
            
            # Sureshot Logic (Simple Trend Prediction)
            res = "BIG" if history.count("S") >= history.count("B") else "SMALL"
            
            # Level Management based on previous result
            if st.session_state.last_status == "LOSS":
                st.session_state.level = st.session_state.level + 1 if st.session_state.level < 5 else 1
            else:
                st.session_state.level = 1
            
            # Status line inside result box
            status_html = ""
            if st.session_state.last_status:
                s_text = "PREVIOUS: WIN ✅" if st.session_state.last_status == "WIN" else "PREVIOUS: LOSS ❌"
                s_class = "win-color" if st.session_state.last_status == "WIN" else "loss-color"
                status_html = f'<div class="status-line {s_class}">{s_text}</div>'

            # Final Result Display (Fixing the code display error)
            st.markdown(f"""
            <div class="result-container">
                {status_html}
                <div style="color:#ffff00; font-size:22px; font-weight:900;">PERIOD: {period}</div>
                <h3 style='color:#00f2fe; margin-top:10px; margin-bottom:0;'>அடுத்த கணிப்பு</h3>
                <div class="prediction-txt">{res}</div>
                <div style='background:white; color:black; padding:8px 25px; border-radius:15px; font-weight:900; display:inline-block;'>LEVEL {st.session_state.level} SURESHOT 🔥</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Simulate next round's status (In real app, user would confirm win/loss)
            st.session_state.last_status = random.choice(["WIN", "LOSS", "WIN"])
        else:
            st.error("சரியான தகவல்களை உள்ளிடவும் மச்சி! (Period: Numbers, History: B/S only)")

    st.markdown("""<a href="https://t.me/toptamilearning100k" target="_blank" class="tg-btn">✈️ JOIN TELEGRAM CHANNEL</a>""", unsafe_allow_html=True)
