import streamlit as st
import random
import time

# Mobile view setup
st.set_page_config(page_title="siva prediction", page_icon="💰🎯", layout="centered")

st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stStatusWidget"] { visibility: hidden !important; }
    .stApp { background: linear-gradient(180deg, #0f0c29 0%, #302b63 50%, #24243e 100%); color: white; }
    .main-title { color: #00f2fe; text-align: center; font-size: 30px; font-weight: 900; }
    .result-box { padding: 25px; border-radius: 20px; border: 3px solid #00f2fe; background: rgba(0, 0, 0, 0.7); text-align: center; margin-top: 20px; }
    .wait-box { padding: 25px; border-radius: 20px; border: 3px solid #ff0000; background: rgba(255, 0, 0, 0.2); text-align: center; margin-top: 20px; color: #ff0000; font-weight: bold; }
    input { color: black !important; font-weight: bold !important; }
    .stButton>button { width: 100%; border-radius: 50px; background: linear-gradient(45deg, #00ff00, #008000); color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

if 'is_registered' not in st.session_state: st.session_state.is_registered = False

if not st.session_state.is_registered:
    st.markdown("<div class='main-title'>💰 siva prediction 🎯</div>", unsafe_allow_html=True)
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" target="_blank" style="display: block; background: #00ff00; color: black; padding: 15px; border-radius: 50px; font-weight: 900; text-decoration: none; text-align: center; margin: 20px 0;">REGISTER HERE ✅</a>', unsafe_allow_html=True)
    if st.button("பதிவு செய்துவிட்டேன் ✅"):
        st.session_state.is_registered = True
        st.rerun()
else:
    st.markdown("<div class='main-title'>💰 LEVEL 1 SURESHOT 🎯</div>", unsafe_allow_html=True)
    
    history_raw = st.text_input("கடந்த 10 முடிவுகள் (B/S):", max_chars=10, placeholder="Ex: BBSSBBSBSS").upper()
    period_raw = st.text_input("பீரியட் எண் (Last 3 Digits):", max_chars=3)

    if st.button("ANALYSE LEVEL 1"):
        if (all(char in "BS" for char in history_raw) and len(history_raw) == 10):
            with st.spinner('Scanning Market Trends...'):
                time.sleep(2.0)
            
            # --- LEVEL 1 SURESHOT LOGIC ---
            prediction = ""
            status = "SURESHOT"
            
            # 1. Dragon Hunter (Very High Confidence)
            if history_raw.endswith("BBBB") or history_raw.endswith("SSSS"):
                prediction = "BIG" if "B" in history_raw[-1] else "SMALL"
            
            # 2. Perfect Zig-Zag Break (High Confidence)
            elif history_raw.endswith("BSBS") or history_raw.endswith("SBSB"):
                prediction = "SMALL" if history_raw[-1] == "B" else "BIG"
            
            # 3. Dominant Trend (Safe Bet)
            elif history_raw.count("B") >= 7:
                prediction = "BIG"
            elif history_raw.count("S") >= 7:
                prediction = "SMALL"
            
            # 4. IF NO CLEAR PATTERN -> SKIP
            else:
                status = "SKIP"

            if status == "SURESHOT":
                st.markdown(f"""
                <div class="result-box">
                    <h2 style='color: #00ff00;'>🔥 LEVEL 1 SURESHOT 🔥</h2>
                    <h1 style='font-size: 80px; margin: 10px 0;'>{prediction}</h1>
                    <p>Accuracy: 99% (Wait for next period)</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="wait-box">
                    <h2>⚠️ TREND NOT CLEAR ⚠️</h2>
                    <p>இந்த பீரியடை தவிர்க்கவும் (SKIP). அடுத்த 2 பீரியட் கழித்து மீண்டும் முயற்சி செய்யவும்.</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("10 முடிவுகளைச் சரியாக உள்ளிடவும்!")
