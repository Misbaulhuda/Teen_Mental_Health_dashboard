import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("😰 Stress & Anxiety")

fig = px.scatter(
    df,
    x="sleep_hours",
    y="stress_level",
    color="social_interaction_level",
    title="Sleep vs Stress"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.scatter(
    df,
    x="physical_activity",
    y="anxiety_level",
    color="gender",
    title="Physical Activity vs Anxiety"
)

st.plotly_chart(fig2,use_container_width=True)

fig3 = px.box(
    df,
    x="social_interaction_level",
    y="stress_level",
    color="social_interaction_level"
)

st.plotly_chart(fig3,use_container_width=True)
