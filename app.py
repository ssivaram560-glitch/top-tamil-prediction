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
    input { color: #000000 !important; background-color: #FFFFFF !important; font-weight: bold !important; font-size: 18px !important; border-radius: 10px !important; }
    label { color: #00f2fe !important; font-weight: bold !important; }
    .rules-box { background: rgba(0, 242, 252, 0.1); padding: 15px; border-radius: 12px; border-left: 5px solid #00f2fe; margin-bottom: 20px; font-size: 14px; }
    .result-container { border: 4px solid #00f2fe; border-radius: 25px; padding: 25px; text-align: center; background: rgba(0, 0, 0, 0.9); box-shadow: 0 0 40px #00f2fe; margin-top: 20px; }
    .prediction-txt { font-size: 80px; font-weight: 900; color: #ffffff; margin: 10px 0; text-shadow: 0 0 20px #fff; }
    .status-line { font-size: 22px; font-weight: 900; margin-bottom: 10px; text-transform: uppercase; }
    .win-color { color: #00ff00; }
    .loss-color { color: #ff0000; }
    .alert-box { background: #ff0000; color: white; padding: 12px; border-radius: 15px; font-weight: 900; animation: blinker 0.8s linear infinite; margin-top: 15px; border: 2px solid white; }
    @keyframes blinker { 50% { opacity: 0; } }
    .reg-btn { display: block; background: #00ff00; color: black !important; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none !important; text-align: center; margin: 25px 0; font-size: 20px; }
    .tg-btn { display: block; background: #0088cc; color: white !important; padding: 15px; border-radius: 50px; text-decoration: none !important; font-weight: 900; text-align: center; margin-top: 30px; border: 2px solid white; }
    .stButton>button { background: linear-gradient(90deg, #00f2fe, #4facfe); color: black; font-weight: 900; border-radius: 50px; height: 3.5em; font-size: 18px; border: none; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

def show_rules():
    st.markdown("""<div class="rules-box">
    <b>📜 SIVA AI V5 RULES:</b><br>
    🔹 1. Register பட்டனை அழுத்தி கணக்கை உருவாக்கவும் ✅<br>
    🔹 2. <b>Ultra Sureshot</b> வந்தால் மட்டும் அதிக முதலீடு செய்யவும் 🔥<br>
    🔹 3. 7 Level Fund-ஐ எப்போதுமே கையில் வைத்திருக்கவும் 💰<br>
    🔹 4. <b>மிக முக்கியமாக Result உள்ளீடும் போது கீழே இருந்து மேலாக 10 Result ஐ Type பண்ணவும்</b>
    </div>""", unsafe_allow_html=True)

if 'registered' not in st.session_state: st.session_state.registered = False
if 'current_level' not in st.session_state: st.session_state.current_level = 1
if 'prev_pred' not in st.session_state: st.session_state.prev_pred = None
if 'outcome' not in st.session_state: st.session_state.outcome = None

if not st.session_state.registered:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    show_rules() 
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" class="reg-btn">REGISTER HERE ✅</a>', unsafe_allow_html=True)
    if st.button("REGISTER செய்துவிட்டேன் ✅"):
        st.session_state.registered = True
        st.rerun()
else:
    st.markdown("<div class='main-title'>🚀 SIVA ADVANCED AI 💥</div>", unsafe_allow_html=True)
    show_rules() 
    period = st.text_input("Period Number:", placeholder="Ex: 314", max_chars=3)
    history = st.text_input("History (Bottom to Top):", placeholder="Ex: BBSSBSBBSB", max_chars=10).upper()

    if st.button("GET SURESHOT RESULT ⚡"):
        if period.isdigit() and history and all(c in "BS" for c in history):
            with st.spinner('Analyzing Patterns & Trends...'):
                time.sleep(1.5)
            
            # --- ADVANCED CALCULATION LOGIC ---
            b_count, s_count = history.count("B"), history.count("S")
            last_3 = history[-3:]
            is_ultra = False
            
            # Trend Analysis
            if "BSBS" in history or "SBSB" in history: # Alternating Pattern
                pred = "BIG" if history[-1] == "S" else "SMALL"
                is_ultra = True
            elif last_3 == "BBB" or last_3 == "SSS": # Dragon Catching
                pred = last_3[0] # Continue Dragon
                is_ultra = True
            else: # Statistical Majority Reversal
                pred = "BIG" if s_count >= b_count else "SMALL"

            # Win/Loss Calculation (Previous vs Current History)
            latest_real = "BIG" if history[-1] == "B" else "SMALL"
            if st.session_state.prev_pred:
                if st.session_state.prev_pred == latest_real:
                    st.session_state.outcome, st.session_state.current_level = "WIN ✅", 1
                else:
                    st.session_state.outcome = "LOSS ❌"
                    st.session_state.current_level = st.session_state.current_level + 1 if st.session_state.current_level < 7 else 1
            else: st.session_state.outcome = "ANALYZING..."

            st.session_state.prev_pred = pred
            s_class = "win-color" if "WIN" in st.session_state.outcome else "loss-color"

            st.markdown(f"""
            <div class="result-container">
                <div class="status-line {s_class}">PREVIOUS: {st.session_state.outcome}</div>
                <div style="color:#ffff00; font-size:24px; font-weight:900;">PERIOD: {period}</div>
                <h3 style='color:#00f2fe; margin-top:10px;'>அடுத்த கணிப்பு</h3>
                <div class="prediction-txt">{pred}</div>
                {f'<div class="alert-box">🔥 ULTRA SURESHOT - INVEST FULL! 🔥</div>' if is_ultra else ''}
                <div style='background:white; color:black; padding:8px 30px; border-radius:15px; font-weight:900; display:inline-block; margin-top:10px;'>LEVEL {st.session_state.current_level}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("சரியான தகவல்களை உள்ளிடவும்!")

    st.markdown("""<a href="https://t.me/toptamilearning100k" target="_blank" class="tg-btn">✈️ JOIN TELEGRAM CHANNEL</a>""", unsafe_allow_html=True)
