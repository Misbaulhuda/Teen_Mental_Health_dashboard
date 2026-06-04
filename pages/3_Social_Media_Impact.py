import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("📱 Social Media Impact")

fig = px.scatter(
    df,
    x="daily_social_media_hours",
    y="stress_level",
    color="platform_usage",
    size="addiction_level",
    title="Social Media vs Stress"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.scatter(
    df,
    x="daily_social_media_hours",
    y="academic_performance",
    color="gender",
    title="Academic Performance Impact"
)

st.plotly_chart(fig2,use_container_width=True)
