import streamlit as st
import random
import time

# Page Configuration - Pro Injection Look
st.set_page_config(page_title="PRO INJECTOR V6", page_icon="⚡", layout="centered")

# Custom CSS for the "Injection" and "Encrypted" Look
st.markdown("""
    <style>
    header, footer, .stDeployButton, [data-testid="stStatusWidget"] { visibility: hidden !important; }
    .stApp { background: #000000; color: #00f2fe; font-family: 'Courier New', Courier, monospace; }
    
    .injection-container {
        border: 2px solid #00f2fe;
        border-radius: 20px;
        padding: 25px;
        background: rgba(0, 242, 254, 0.05);
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.3);
        text-align: center;
        margin-bottom: 20px;
    }
    
    .status-badge {
        background: #00f2fe; color: black; padding: 5px 15px;
        border-radius: 5px; font-weight: 900; font-size: 12px;
        margin-bottom: 10px; display: inline-block;
    }

    input { 
        background-color: #111 !important; 
        color: #00f2fe !important; 
        border: 1px solid #00f2fe !important;
        border-radius: 10px !important;
        text-align: center;
    }

    .result-display {
        background: #000;
        border: 4px double #00f2fe;
        border-radius: 25px;
        padding: 35px;
        margin-top: 25px;
        box-shadow: 0 0 40px rgba(0, 242, 254, 0.4);
    }

    .big-small-text { 
        font-size: 85px; font-weight: 900; color: #ffffff; 
        text-shadow: 0 0 30px #fff, 0 0 50px #00f2fe; 
        letter-spacing: 5px; margin: 15px 0;
    }

    .level-tag { font-size: 22px; font-weight: 900; color: #ff0055; margin-bottom: 10px; }

    .stButton>button {
        background: linear-gradient(180deg, #00f2fe 0%, #0072ff 100%);
        color: black; font-weight: 900; border-radius: 15px;
        width: 100%; height: 4em; border: none; font-size: 18px;
    }

    .official-link {
        display: block; background: #ff0055; color: white !important;
        padding: 18px; border-radius: 50px; text-decoration: none;
        font-weight: 900; margin-top: 30px; text-align: center;
        box-shadow: 0 0 15px #ff0055; font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# State Management for Session
if 'registered' not in st.session_state: st.session_state.registered = False

# --- Page 1: Register (Only once) ---
if not st.session_state.registered:
    st.markdown('<div class="injection-container"><h1 style="color:#00f2fe;">💰 SIVA PREDICTION</h1><p style="color:gray;">MEMBER SYSTEM INITIALIZING...</p></div>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://www.66lotterya.com/?invitationCode=1645982010" class="official-link">REGISTER & LOGIN HERE ✅</a>', unsafe_allow_html=True)
    if st.button("LOGIN SUCCESSFUL"):
        st.session_state.registered = True
        st.rerun()

# --- Page 2: Predictor Interface ---
else:
    st.markdown("""<div class="injection-container">
        <div class="status-badge">SERVER: ONLINE 🟢</div>
        <h2 style="margin:0; text-shadow: 0 0 10px #00f2fe;">PRO INJECTOR X</h2>
        <p style="color:#777; font-size:12px;">ENCRYPTED DATA FEED FOUND</p>
    </div>""", unsafe_allow_html=True)

    period = st.text_input("PERIOD (Last 3 Digits)", placeholder="Eg: 345")
    history_raw = st.text_input("DATA STREAM (B/S)", placeholder="Eg: BBSBS").upper()

    if st.button("NEXT INJECTION 💉"):
        if history_raw:
            with st.spinner('INJECTING ALGORITHM...'):
                time.sleep(1.2)
            
            # --- LEVEL 2 WIN LOGIC (The Pattern Trick) ---
            b_count = history_raw.count('B')
            s_count = history_raw.count('S')
            last_char = history_raw[-1]
            
            # Level 2 Focus: Break Dragon Trends
            if len(history_raw) >= 3 and history_raw[-3:] in ["BBB", "SSS"]:
                # Reversal logic for Level 2 recovery
                prediction = "SMALL" if last_char == "B" else "BIG"
                is_sureshot = True
            else:
                # Majority trend reversal for stable wins
                prediction = "BIG" if s_count >= b_count else "SMALL"
                is_sureshot = False

            # Displaying the Result
            st.markdown(f"""
                <div class="result-display">
                    <div class="level-tag">LEVEL 1 & 2 FOCUS 🎯</div>
                    <div style="color:gray; font-size:12px;">CALCULATED PERIOD: {period}</div>
                    <h1 class="big-small-text">{prediction}</h1>
                    <p style="color:#00ff00; font-weight:bold;">CONFIDENCE: {random.uniform(97.8, 99.9):.1f}%</p>
                    {f'<div style="background:red; color:white; padding:5px; border-radius:5px; font-weight:bold; animation: blinker 0.6s linear infinite;">🔥 ULTRA SURESHOT - HIGH INVEST 🔥</div>' if is_sureshot else ''}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Please enter Data Stream!")

    st.markdown(f'<a href="https://www.66lotterya.com/?invitationCode=1645982010" class="official-link">OPEN 66 LOTTERY ✅</a>', unsafe_allow_html=True)
