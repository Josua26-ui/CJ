import streamlit as st
import json
from datetime import datetime

# 1. INDUSTRIAL MINIMALIST UI (No Emojis, Pure Construction Vibe)
st.set_page_config(page_title="CJ System", layout="wide")

st.markdown("""
    <style>
    /* Minimalist Deep Dark Theme (Steel & Concrete vibe) */
    .stApp { 
        background-color: #09090B; 
        color: #E4E4E7; 
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    /* CJ Custom Monolithic Logo */
    .cj-logo {
        background-color: #FAFAFA;
        color: #09090B;
        font-size: 24px;
        font-weight: 900;
        padding: 6px 14px;
        display: inline-block;
        letter-spacing: -1px;
        border-radius: 2px;
        margin-bottom: 20px;
        font-family: 'SF Mono', monospace;
    }

    /* Typography */
    .sys-title { font-size: 26px; font-weight: 800; color: #FAFAFA; letter-spacing: -0.5px; text-transform: uppercase; margin-bottom: 2px; }
    .sys-subtitle { font-size: 11px; color: #71717A; font-family: 'SF Mono', monospace; letter-spacing: 1px; margin-bottom: 30px; }
    
    /* Minimalist Metric Cards */
    .industrial-card { 
        background: #09090B;
        padding: 20px; 
        border: 1px solid #27272A;
        border-left: 3px solid #3B82F6; /* Industrial Steel Blue Accent */
        border-radius: 2px;
    }
    .card-label { font-size: 10px; font-weight: 600; color: #A1A1AA; letter-spacing: 1.5px; text-transform: uppercase; }
    .card-value { font-size: 24px; font-weight: 600; color: #FAFAFA; font-family: 'SF Mono', monospace; margin-top: 8px; }
    
    /* Chat Interface - Stark & Clean */
    .chat-user { background-color: #18181B; padding: 18px; margin-bottom: 16px; border: 1px solid #27272A; color: #F4F4F5; text-align: right; margin-left: 20%; border-radius: 2px; }
    .chat-ai { background-color: #09090B; padding: 18px; margin-bottom: 16px; border: 1px solid #27272A; border-left: 3px solid #F97316; color: #D4D4D8; line-height: 1.6; margin-right: 20%; border-radius: 2px; }
    
    /* Inputs & Sidebar Formating */
    .stTextInput>div>div>input { background-color: #09090B !important; color: #FAFAFA !important; border-radius: 2px !important; border: 1px solid #27272A !important; font-family: 'SF Mono', monospace; font-size: 12px !important; }
    section[data-testid="stSidebar"] { background-color: #09090B !important; border-right: 1px solid #27272A; }
    .stButton>button { border-radius: 2px !important; border: 1px solid #27272A !important; background-color: #18181B !important; color: #FAFAFA !important; font-family: 'SF Mono', monospace; font-size: 12px !important;}
    </style>
""", unsafe_allow_html=True)

# 2. STATE MANAGEMENT (Blank Canvas)
if 'custom_app_name' not in st.session_state:
    st.session_state.custom_app_name = "SITE COMMAND CORE"

if 'project_metrics' not in st.session_state:
    st.session_state.project_metrics = {
        "location": "AWAITING GPS/INPUT...",
        "cost_total": 0,
        "cost_spent": 0,
        "time_progress": 0.0,
        "quality_rules": "UNINITIALIZED",
        "active_modules": ["CORE_ENGINE_V1"]
    }

if 'chat_stream' not in st.session_state:
    st.session_state.chat_stream = [
        {"role": "assistant", "content": "SYSTEM ONLINE. Menunggu injeksi data RAB, spesifikasi teknis, atau log lapangan. Modul adaptif (Procore, OpenSpace, DroneDeploy, viAct) dalam posisi standby."}
    ]

metrics = st.session_state.project_metrics

# 3. SIDEBAR (Dynamic System Name & Custom Logo)
with st.sidebar:
    st.markdown("<div class='cj-logo'>CJ</div>", unsafe_allow_html=True)
    
    # Input field to dynamically change the App Name
    st.markdown("<div class='card-label'>SYSTEM NAME</div>", unsafe_allow_html=True)
    new_name = st.text_input("", st.session_state.custom_app_name, label_visibility="collapsed")
    st.session_state.custom_app_name = new_name
    
    st.write("---")
    st.markdown("<div class='card-label'>ACTIVE MODULES</div>", unsafe_allow_html=True)
    for module in metrics["active_modules"]:
        st.caption(f"▪ {module}")
        
    st.write("---")
    compiled_data = {"Audit_Date": str(datetime.now()), "System_Config": metrics, "System_Logs": st.session_state.chat_stream}
    st.download_button(
        label="EXPORT DOSSIER",
        data=json.dumps(compiled_data, indent=4),
        file_name="CJ_DIGITAL_DOSSIER.json",
        mime="application/json"
    )

# 4. MAIN WORKSPACE (No Emojis, Pure Data)
st.markdown(f"<div class='sys-title'>{st.session_state.custom_app_name}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='sys-subtitle'>LOC :: {metrics['location']}</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    spent_f = f"IDR {metrics['cost_spent']:,}" if metrics['cost_spent'] > 0 else "IDR 0"
    total_f = f"IDR {metrics['cost_total']:,}" if metrics['cost_total'] > 0 else "IDR 0"
    st.markdown(f"<div class='industrial-card'><div class='card-label'>COST CONTROL (PROCORE)</div><div class='card-value'>{spent_f}</div><small style='color:#71717A'>TARGET: {total_f}</small></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='industrial-card'><div class='card-label'>SCHEDULE (S-CURVE)</div><div class='card-value'>{metrics['time_progress']}%</div><small style='color:#71717A'>PROGRESS RATE</small></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='industrial-card'><div class='card-label'>QUALITY (OPENSPACE)</div><div class='card-value' style='color:#A1A1AA; font-size:16px; margin-top:14px;'>{metrics['quality_rules']}</div><small style='color:#71717A'>BASELINE STANDARD</small></div>", unsafe_allow_html=True)

st.write("---")

# 5. CHAT PIPELINE (Terminal Style AI)
for message in st.session_state.chat_stream:
    if message["role"] == "user":
        st.markdown(f"<div class='chat-user'><b>CJ (ADMIN)</b><br><br>{message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-ai'><b>SYSTEM (AI AGENT)</b><br><br>{message['content']}</div>", unsafe_allow_html=True)

prompt_box = st.chat_input("Input data lapangan, Talk to Text, atau paste dokumen log...")

if prompt_box:
    st.session_state.chat_stream.append({"role": "user", "content": prompt_box})
    prompt_norm = prompt_box.lower()
    
    # Adaptive Logic (Terminal-style responses)
    if "proyek" in prompt_norm or "rab" in prompt_norm or "anggaran" in prompt_norm:
        metrics["location"] = "Kawasan Cibubur, Jakarta Timur"
        metrics["cost_total"] = 150000000
        metrics["cost_spent"] = 25000000
        metrics["time_progress"] = 10.0
        metrics["quality_rules"] = "SNI 03-3424-1994"
        if "PROCORE_BUDGETING" not in metrics["active_modules"]:
            metrics["active_modules"].extend(["PROCORE_BUDGETING", "PLANSWIFT_ESTIMATOR"])
            
        ai_analysis = f"ADAPTIVE INITIALIZATION SUCCESS.\\n\\nModul Procore dan PlanSwift aktif.\\n- ZONASI: {metrics['location']}\\n- COST TARGET: IDR {metrics['cost_total']:,}\\n- QUALITY BASE: {metrics['quality_rules']}\\n\\nData struktur matriks visual telah dikalibrasi ulang."

    elif "hujan" in prompt_norm or "ambles" in prompt_norm or "apd" in prompt_norm or "salah" in prompt_norm:
        if "VIACT_SAFETY_VISION" not in metrics["active_modules"]:
            metrics["active_modules"].extend(["VIACT_SAFETY_VISION", "OPENSPACE_TWIN"])
        metrics["time_progress"] = max(metrics["time_progress"] - 2.0, 0.0)
        
        ai_analysis = f"ANOMALY DETECTED (VIACT / OPENSPACE).\\n\\nAnalisis log lapangan masuk:\\n- SAFETY/QUALITY: Deviasi fisik terdeteksi. Protokol mitigasi diaktifkan.\\n- TIME: Kurva-S disesuaikan mundur ke {metrics['time_progress']}%.\\n\\nInstruksikan tim lapangan untuk audit visual pada area yang terdampak."

    elif "drone" in prompt_norm or "volume" in prompt_norm or "galian" in prompt_norm:
        if "DRONEDEPLOY_MAPPING" not in metrics["active_modules"]:
            metrics["active_modules"].append("DRONEDEPLOY_MAPPING")
        metrics["time_progress"] = min(metrics["time_progress"] + 15.0, 100.0)
        metrics["cost_spent"] += 12000000
        
        ai_analysis = f"AERIAL MAPPING ACTIVE (DRONEDEPLOY).\\n\\nCitra topografi udara berhasil disinkronisasi:\\n- MATERIAL VOLUME: Penambahan beban kas lapangan IDR 12,000,000 terkonfirmasi.\\n- SCHEDULE: Progres operasional naik ke {metrics['time_progress']}%.\\n\\nPeta spasial telah dienkripsi ke dalam sistem."

    else:
        ai_analysis = f"INPUT LOGGED.\\n\\nCatatan: '{prompt_box}'\\nSistem standby menunggu instruksi selanjutnya."

    st.session_state.chat_stream.append({"role": "assistant", "content": ai_analysis})
    st.rerun()