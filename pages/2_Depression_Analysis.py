import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("😔 Depression Analysis")

fig = px.histogram(
    df,
    x="depression_label",
    color="gender",
    title="Depression Distribution"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.box(
    df,
    x="depression_label",
    y="daily_social_media_hours",
    color="depression_label",
    title="Social Media Usage vs Depression"
)

st.plotly_chart(fig2,use_container_width=True)

fig3 = px.box(
    df,
    x="depression_label",
    y="sleep_hours",
    title="Sleep Hours Impact"
)

st.plotly_chart(fig3,use_container_width=True)
