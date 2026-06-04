import streamlit as st
from utils.data_loader import load_data
import plotly.express as px

df = load_data()

st.title("📊 Dataset Overview")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Records", len(df))
col2.metric("Avg Age", round(df["age"].mean(),1))
col3.metric("Avg Stress", round(df["stress_level"].mean(),1))
col4.metric("Avg Anxiety", round(df["anxiety_level"].mean(),1))

fig = px.histogram(
    df,
    x="age",
    color="gender",
    title="Age Distribution"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.pie(
    df,
    names="platform_usage",
    title="Platform Usage Distribution"
)

st.plotly_chart(fig2,use_container_width=True)
