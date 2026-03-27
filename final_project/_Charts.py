import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title("📊 Advanced Cyber Risk Insights")


# CHECK DATA

if "data" not in st.session_state:
    st.warning("⚠️ Please upload data first")
    st.stop()

df = st.session_state["data"]

df["risk_level"] = df["risk_score"].apply(
    lambda x: "Low" if x < 4 else ("Medium" if x < 7 else "High")
)

col1, col2 = st.columns(2)

# 📊 BAR CHART
with col1:
    st.subheader("📊 Risk per Host")

    fig_bar = px.bar(
        df,
        x="ip",
        y="risk_score",
        color="risk_score",
        color_continuous_scale="Blues"
    )
    fig_bar.update_traces(width=0.3)
    st.plotly_chart(fig_bar, use_container_width=True)

# 📈 LINE CHART
with col2:
    st.subheader("📈 Risk Trend")

    fig_line = px.line(
        df,
        x="ip",
        y="risk_score",
        markers=True,
        color="service"
    )
    st.plotly_chart(fig_line, use_container_width=True)

col3, col4 = st.columns(2)

# 🍩 DONUT
with col3:
    st.subheader("🍩 Risk Distribution")

    fig_donut = px.pie(
        df,
        names="risk_level",
        hole=0.5,
        color="risk_level",
        color_discrete_map={
            "Low": "#10b981",
            "Medium": "#f59e0b",
            "High": "#ef4444"
        }
    )
    st.plotly_chart(fig_donut, use_container_width=True)

# 🎯 GAUGE
with col4:
    st.subheader("🎯 Total Risk Meter")

    total_risk = df["risk_score"].sum()

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=total_risk,
        title={'text': "Total Risk"},
        gauge={
            'axis': {'range': [0, 30]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0, 10], 'color': "green"},
                {'range': [10, 20], 'color': "orange"},
                {'range': [20, 30], 'color': "red"},
            ],
        }
    ))

    st.plotly_chart(fig_gauge, use_container_width=True)

col5, col6 = st.columns(2)



# 📦 BOX PLOT
with col6:
    st.subheader("📦 Risk Distribution")

    fig_box = px.box(
        df,
        x="service",
        y="risk_score",
        color="service"
    )

    st.plotly_chart(fig_box, use_container_width=True)

col7, col8 = st.columns(2)

# 🧭 SUNBURST
with col7:
    st.subheader("🧭 Risk Hierarchy")

    fig_sunburst = px.sunburst(
        df,
        path=["ip", "service", "port"],
        values="risk_score"
    )

    st.plotly_chart(fig_sunburst, use_container_width=True)

# 🫧 BUBBLE
with col8:
    st.subheader("🫧 Risk Bubble")

    fig_bubble = px.scatter(
        df,
        x="port",
        y="risk_score",
        size="risk_score",
        color="service",
        hover_name="ip"
    )

    st.plotly_chart(fig_bubble, use_container_width=True)