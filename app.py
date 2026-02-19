import streamlit as st
import time
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="siva prediction", page_icon="🐉", layout="centered")

# --- CUSTOM CSS (APK INTERFACE STYLE) ---
st.markdown("""
    <style>
    header, footer, .stDeployButton { visibility: hidden !important; }
    .stApp { background: #000000; color: #00f2fe; font-family: 'Courier New', Courier, monospace; }
    
    /* Main Container */
    .main-card {
        border: 2px solid #00f2fe; border-radius: 20px;
        padding: 25px; background: rgba(0, 242, 254, 0.05);
        box-shadow: 0 0 35px rgba(0, 242, 254, 0.3); text-align: center;
        margin-top: 10px;
    }
    
    .glow-text { font-size: 35px; font-weight: 900; color: #00f2fe; text-shadow: 0 0 15px #00f2fe; margin-bottom: 10px; }

    /* Buttons */
    .link-btn {
        display: block; background: linear-gradient(180deg, #ff0055 0%, #aa0033 100%);
        color: white !important; padding: 18px; border-radius: 50px;
        text-decoration: none; font-weight: 900; margin: 15px 0; text-align: center;
        font-size: 18px; box-shadow: 0 4px 15px rgba(255, 0, 85, 0.4);
    }
    
    /* Prediction Box */
    .result-box {
        background: #000; border: 4px double #00f2fe;
        border-radius: 30px; padding: 30px; margin-top: 25px;
        box-shadow: inset 0 0 20px #00f2fe;
    }

    .pred-text { font-size: 90px; font-weight: 900; color: #ffffff; text-shadow: 0 0 30px #ffffff; margin: 10px 0; }
    
    .status-bar { background: #00f2fe; color: #000; font-weight: 900; border-radius: 5px; padding: 5px; font-size: 12px; margin-bottom: 20px; }
    
    /* History List */
    .history-item { background: #111; padding: 10px; border-radius: 10px; margin-top: 8px; border-left: 5px solid #00ff00; text-align: left; display: flex; justify-content: space-between; }
    </style>
    """, unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if 'activated' not in st.session_state: st.session_state.activated = False
if 'history' not in st.session_state: st.session_state.history = []

# --- PHASE 1: VIP ACTIVATION (As seen in Video) ---
if not st.session_state.activated:
    st.markdown('<div class="main-card"><h1 class="glow-text">siva prediction</h1><p style="color:gray;">SYSTEM: LOCKED 🔒</p></div>', unsafe_allow_html=True)
    
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" class="link-btn">STEP 1: REGISTER ACCOUNT ✅</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" class="link-btn" style="background:#00f2fe; color:black !important;">STEP 2: DEPOSIT ₹500+ FOR VIP 💰</a>', unsafe_allow_html=True)
    
    if st.button("STEP 3: ACTIVATE DRAGON INJECTOR 🐉"):
        with st.spinner('CONNECTING TO SERVER...'):
            time.sleep(2.5)
        st.session_state.activated = True
        st.rerun()

# --- PHASE 2: DRAGON VIP PREDICTOR ---
else:
    st.markdown('<div style="text-align:center;"><span style="color:#00ff00; font-weight:900;">● VIP STATUS: ACTIVE</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="main-card"><h4>INJECTION MODULE V1.2</h4></div>', unsafe_allow_html=True)
    
    period = st.text_input("PERIOD (Last 3 Digits)", placeholder="Eg: 567", max_chars=3)
    history_data = st.text_input("HISTORY (B/S only)", placeholder="Eg: BBSSB").upper()

    if st.button("START INJECTION 💉"):
        if period.isdigit() and history_data:
            with st.spinner('CALCULATING NEXT TREND...'):
                time.sleep(1.5)
            
            # --- LEVEL 2 WIN LOGIC (The Core Hack) ---
            # Rule: Break dragon trends and follow alternating patterns
            if len(history_data) >= 2:
                if history_data[-2:] == "BB": pred = "SMALL"
                elif history_data[-2:] == "SS": pred = "BIG"
                else: pred = "BIG" if history_data.count("S") >= history_data.count("B") else "SMALL"
            else:
                pred = random.choice(["BIG", "SMALL"])

            # Save to History
            st.session_state.history.insert(0, {"p": period, "r": pred})

            # Display Result
            st.markdown(f"""
                <div class="result-box">
                    <div class="status-bar">INJECTION SUCCESSFUL</div>
                    <p style="color:#00f2fe; margin-bottom:0;">NEXT PREDICTION</p>
                    <h1 class="pred-text">{pred}</h1>
                    <div style="background:#00ff00; color:black; padding:5px 15px; border-radius:8px; font-weight:900; display:inline-block;">LEVEL 1/2 SURESHOT 🔥</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Please enter correct data!")

    # --- HISTORY SECTION ---
    if st.session_state.history:
        st.markdown("### 📊 RECENT INJECTIONS")
        for item in st.session_state.history[:5]:
            st.markdown(f'''
                <div class="history-item">
                    <span>Period: <b>{item["p"]}</b></span>
                    <span>Result: <b>{item["r"]}</b></span>
                    <span style="color:#00ff00;">WIN ✅</span>
                </div>
            ''', unsafe_allow_html=True)

    st.markdown(f'<a href="https://www.66lotterya.com/?invitationCode=1645982010" class="link-btn" style="background:#222; box-shadow:none;">GO TO 66 LOTTERY ✅</a>', unsafe_allow_html=True)
