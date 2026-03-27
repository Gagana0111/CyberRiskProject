import streamlit as st


st.set_page_config(
    page_title="Cyber Risk Dashboard",
    layout="wide",
)

# SIDEBAR (PROJECT INFO)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3064/3064197.png", width=90)

    st.markdown("## 🔐 Cyber Risk Dashboard")

    st.markdown("""
    ### 📌 About Project
    
    This project focuses on:
    
    ✔ Identifying open ports  
    ✔ Analyzing vulnerabilities  
    ✔ Calculating risk scores  
    ✔ Visualizing cyber threats  
    ✔ Sending email alerts  
    
    """)

    st.markdown("---")

    st.markdown("### 🛠 Tools Used")
    st.markdown("""
    - Python 🐍  
    - Nmap 🔍  
    - Streamlit 📊  
    - Plotly 📈  
    """)

    st.markdown("---")

    st.markdown("### 📊 Features")
    st.markdown("""
    ✔ Upload Scan Reports  
    ✔ Risk Analysis  
    ✔ Interactive Charts  
    ✔ Download Reports  
    """)

    st.markdown("---")

    st.success("🚀 Secure Your Network")



st.markdown("""
<style>
MainMenu {visibility: hidden;}
header {visibility: hidden;}

.main {
    background-color: #0b0f19;
}

/* Title */
h1 {
    color: #00E5FF;
    text-align: center;
}

/* Cards */
.card {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    color: white;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    font-size: 16px;
    font-weight: bold;
    background: linear-gradient(135deg, #1f4037, #99f2c8);
    color: white;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🔐 Cyber Risk Assessment Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Analyze • Detect • Protect</h4>", unsafe_allow_html=True)

st.markdown("---")

# TOP NAVIGATION (NO SIDEBAR)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home"):
        st.switch_page("dashboard.py")

with col2:
    if st.button("📤 Upload & Analyze"):
        st.switch_page("pages/_Upload_Data.py")

with col3:
    if st.button("📊 Charts & Insights"):
        st.switch_page("pages/_Charts.py")

with col4:
    if st.button("📋 Detailed Results"):
        st.switch_page("pages/_Detailed_Result.py")

st.markdown("---")

# HERO SECTION

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
    ### 👋 Welcome
    
    This platform helps you:
    
    ✔ Detect network vulnerabilities  
    ✔ Analyze risk levels  
    ✔ Visualize cyber threats  
    ✔ Get instant email alerts  
    
    👉 Start by uploading your scan data.
    """)

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/3064/3064197.png")


# FEATURES

st.markdown("## 🚀 Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">📊<br><br><b>Interactive Charts</b><br>Visualize risks easily</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">📧<br><br><b>Email Alerts</b><br>Instant notifications</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">🔍<br><br><b>Deep Analysis</b><br>Detailed insights</div>', unsafe_allow_html=True)


# HOW IT WORKS

st.markdown("## ⚙️ How It Works")

st.markdown("""
1️⃣ Upload scan report  
2️⃣ Analyze risks  
3️⃣ View charts  
4️⃣ Take action  
""")


# FOOTER

st.markdown("---")
st.markdown("<center>🔐 Cyber Security Project Dashboard</center>", unsafe_allow_html=True)