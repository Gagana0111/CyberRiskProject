import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Analysis", layout="wide")

st.title("📊 Detailed Analysis Dashboard")

st.markdown("---")

# LOAD DATA

if "data" not in st.session_state:
    st.warning("⚠️ Upload data first")
    st.stop()

df = st.session_state["data"]


# SIDEBAR

with st.sidebar:
    st.markdown("## 🛡️ Cyber Dashboard")
    st.success("📊 Analysis Mode")

    # FILTERS
    st.markdown("### 🔎 Filters")

    selected_service = st.multiselect(
        "Filter by Service",
        df["service"].unique()
    )

    if selected_service:
        df = df[df["service"].isin(selected_service)]


# KPIs (TOP METRICS)

col1, col2, col3, col4 = st.columns(4)

col1.metric("🌐 Hosts", df["ip"].nunique())
col2.metric("🔌 Open Ports", len(df))
col3.metric("⚠️ Max Risk", df["risk_score"].max())
col4.metric("📊 Total Risk", df["risk_score"].sum())

st.markdown("---")

# TOP RISKY PORTS

st.subheader("🔥 Top Risky Ports")

top = df.sort_values(by="risk_score", ascending=False)

fig = px.bar(
    top,
    x="port",
    y="risk_score",
    color="service",
)

fig.update_layout(template="plotly_dark", height=400)

st.plotly_chart(fig, use_container_width=True)


# RISK DISTRIBUTION (DONUT)

st.subheader("🍩 Risk Distribution")

df["risk_level"] = df["risk_score"].apply(
    lambda x: "Low" if x < 4 else ("Medium" if x < 7 else "High")
)

fig_donut = px.pie(df, names="risk_level", hole=0.5)
fig_donut.update_layout(template="plotly_dark")

st.plotly_chart(fig_donut, use_container_width=True)


# SERVICE ANALYSIS

st.subheader("📡 Service Analysis")

fig_service = px.histogram(
    df,
    x="service",
    color="service"
)

fig_service.update_layout(template="plotly_dark")

st.plotly_chart(fig_service, use_container_width=True)


# DATA TABLE

st.markdown("---")
st.subheader("📋 Full Data")

st.dataframe(df, use_container_width=True)


# DOWNLOAD BUTTON

st.markdown("### 📥 Download Report")

st.download_button(
    label="⬇ Download CSV",
    data=df.to_csv(index=False),
    file_name="cyber_risk_report.csv",
    mime="text/csv"
)