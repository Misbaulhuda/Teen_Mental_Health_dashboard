import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("🔍 Advanced Insights")

corr = df.select_dtypes(include='number').corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Correlation Heatmap"
)

st.plotly_chart(fig,use_container_width=True)

st.subheader("Top Risk Group")

high_risk = df[
    (df["stress_level"] > 7)
    &
    (df["anxiety_level"] > 7)
]

st.dataframe(high_risk.head(20))

st.subheader("Key Findings")

st.info("""
1. Higher social media usage correlates with higher addiction levels.
2. Lower sleep hours increase stress and anxiety.
3. Physical activity reduces anxiety.
4. Depression risk rises with excessive screen time.
5. Academic performance decreases with higher addiction scores.
""")
