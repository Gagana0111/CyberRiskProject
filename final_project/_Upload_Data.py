import streamlit as st
import pandas as pd

st.title("📤 Upload Scan Report")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("✅ File Uploaded Successfully")
    st.dataframe(df)

    # ✅ FIX (persist data)
    st.session_state["data"] = df

    st.info("👉 Now go to Charts page")

else:
    st.warning("⚠️ Please upload a CSV file")