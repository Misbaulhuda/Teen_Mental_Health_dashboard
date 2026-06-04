import streamlit as st

st.set_page_config(
    page_title="Teen Mental Health Analytics",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Teen Mental Health Analytics Dashboard")

st.markdown("""
### Deep Analytics on Teen Social Media & Mental Health

Analyze:

- Depression Trends
- Anxiety Patterns
- Social Media Addiction
- Sleep Impact
- Academic Performance
- Stress Levels
""")

st.image(
"https://images.unsplash.com/photo-1506126613408-eca07ce68773",
use_container_width=True
)

st.success("Select a page from the sidebar.")
