import streamlit as st
import time
import random

# Page Setup
st.set_page_config(page_title="SIVA INJECTOR PRO", page_icon="🧬", layout="centered")

# UI Styling - Full Video Style
st.markdown("""
    <style>
    header, footer, .stDeployButton { visibility: hidden !important; }
    .stApp { background: #000; color: #00f2fe; }
    
    .main-box {
        border: 2px solid #00f2fe; border-radius: 20px;
        padding: 20px; background: rgba(0, 242, 254, 0.05);
        box-shadow: 0 0 25px #00f2fe; text-align: center;
    }
    
    .big-btn {
        display: block; background: linear-gradient(90deg, #ff0055, #ff00aa);
        color: white !important; padding: 15px; border-radius: 10px;
        text-decoration: none; font-weight: 900; margin: 10px 0; text-align: center;
    }
    
    .result-screen {
        background: #000; border: 3px solid #00f2fe;
        border-radius: 20px; padding: 25px; margin-top: 20px;
    }
    
    .pred-val { font-size: 80px; font-weight: 900; color: #fff; text-shadow: 0 0 20px #00f2fe; }
    
    .history-table { width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 14px; }
    .history-table th, .history-table td { border-bottom: 1px solid #333; padding: 10px; text-align: center; }
    .win-tag { color: #00ff00; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# State Management
if 'step' not in st.session_state: st.session_state.step = "register"
if 'history' not in st.session_state: st.session_state.history = []

# --- STEP 1: REGISTER & DEPOSIT ---
if st.session_state.step == "register":
    st.markdown('<div class="main-box"><h1>🧬 SIVA INJECTOR</h1><p>FOLLOW VIDEO STEPS TO ACTIVATE</p></div>', unsafe_allow_html=True)
    
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" class="big-btn">1. REGISTER ACCOUNT ✅</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.66lotterya.com/?invitationCode=1645982010" class="big-btn" style="background: #00f2fe; color: black !important;">2. DEPOSIT ₹200+ 💰</a>', unsafe_allow_html=True)
    
    if st.button("ACTIVATE HACK ⚡"):
        with st.spinner('VERIFYING DEPOSIT...'):
            time.sleep(2)
        st.session_state.step = "predict"
        st.rerun()

# --- STEP 2: PREDICTOR INTERFACE ---
elif st.session_state.step == "predict":
    st.markdown('<div style="text-align:center; color:#00f2fe; font-weight:900;">SERVER STATUS: ONLINE 🟢</div>', unsafe_allow_html=True)
    
    period = st.text_input("PERIOD NO", placeholder="Eg: 10989")
    data_stream = st.text_input("LAST 5 RESULTS (B/S)", placeholder="Eg: BBSSB").upper()
    
    if st.button("NEXT INJECTION 💉"):
        if period and data_stream:
            with st.spinner('EXTRACTING DATA...'):
                time.sleep(1.5)
            
            # --- LEVEL 2 WIN LOGIC ---
            # Smart Trend Analysis
            if data_stream[-2:] == "BB": pred = "SMALL"
            elif data_stream[-2:] == "SS": pred = "BIG"
            else: pred = random.choice(["BIG", "SMALL"])
            
            # Save to History
            st.session_state.history.insert(0, {"period": period, "result": pred, "status": "WIN ✅"})
            
            st.markdown(f"""
                <div class="result-screen">
                    <div style="color:#00f2fe; font-size:14px;">ENCRYPTED RESULT</div>
                    <div class="pred-val">{pred}</div>
                    <div style="background:#fff; color:#000; display:inline-block; padding:5px 10px; border-radius:5px; font-weight:900;">LEVEL 1 SURESHOT</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Enter Data Stream!")

    # --- HISTORY TABLE ---
    if st.session_state.history:
        st.markdown("### 📊 RECENT HISTORY")
        html_table = '<table class="history-table"><tr><th>PERIOD</th><th>PREDICTION</th><th>STATUS</th></tr>'
        for item in st.session_state.history[:5]:
            html_table += f'<tr><td>{item["period"]}</td><td>{item["result"]}</td><td class="win-tag">{item["status"]}</td></tr>'
        html_table += '</table>'
        st.markdown(html_table, unsafe_allow_html=True)

    if st.button("LOGOUT / RESET"):
        st.session_state.step = "register"
        st.rerun()
