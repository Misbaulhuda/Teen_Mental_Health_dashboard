# utils/charts.py

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# ---------------------------------------------------
# Age Distribution
# ---------------------------------------------------
def age_distribution(df):
    fig = px.histogram(
        df,
        x="age",
        color="gender",
        nbins=15,
        title="Age Distribution",
        template="plotly_dark"
    )

    fig.update_layout(height=500)

    return fig


# ---------------------------------------------------
# Gender Distribution
# ---------------------------------------------------
def gender_distribution(df):
    fig = px.pie(
        df,
        names="gender",
        title="Gender Distribution",
        hole=0.5
    )

    return fig


# ---------------------------------------------------
# Depression Distribution
# ---------------------------------------------------
def depression_distribution(df):
    fig = px.histogram(
        df,
        x="depression_label",
        color="depression_label",
        title="Depression Distribution",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Anxiety Distribution
# ---------------------------------------------------
def anxiety_distribution(df):
    fig = px.histogram(
        df,
        x="anxiety_level",
        title="Anxiety Level Distribution",
        color="anxiety_level",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Stress Distribution
# ---------------------------------------------------
def stress_distribution(df):
    fig = px.histogram(
        df,
        x="stress_level",
        color="stress_level",
        title="Stress Level Distribution",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Sleep vs Stress
# ---------------------------------------------------
def sleep_vs_stress(df):
    fig = px.scatter(
        df,
        x="sleep_hours",
        y="stress_level",
        color="gender",
        size="social_media_hours",
        title="Sleep Hours vs Stress Level",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Sleep vs Anxiety
# ---------------------------------------------------
def sleep_vs_anxiety(df):
    fig = px.scatter(
        df,
        x="sleep_hours",
        y="anxiety_level",
        color="gender",
        title="Sleep Hours vs Anxiety",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Social Media vs Stress
# ---------------------------------------------------
def social_media_vs_stress(df):
    fig = px.scatter(
        df,
        x="social_media_hours",
        y="stress_level",
        color="gender",
        size="addiction_level",
        hover_data=df.columns,
        title="Social Media Usage vs Stress",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Social Media vs Anxiety
# ---------------------------------------------------
def social_media_vs_anxiety(df):
    fig = px.scatter(
        df,
        x="social_media_hours",
        y="anxiety_level",
        color="gender",
        size="addiction_level",
        title="Social Media Usage vs Anxiety",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Social Media vs Academic Performance
# ---------------------------------------------------
def social_media_vs_academic(df):
    fig = px.scatter(
        df,
        x="social_media_hours",
        y="academic_performance",
        color="gender",
        title="Social Media vs Academic Performance",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Addiction Level Analysis
# ---------------------------------------------------
def addiction_distribution(df):
    fig = px.histogram(
        df,
        x="addiction_level",
        color="addiction_level",
        title="Addiction Level Distribution",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Platform Usage
# ---------------------------------------------------
def platform_usage(df):
    fig = px.pie(
        df,
        names="platform_usage",
        title="Social Media Platform Usage",
        hole=0.4
    )

    return fig


# ---------------------------------------------------
# Physical Activity vs Anxiety
# ---------------------------------------------------
def physical_activity_vs_anxiety(df):
    fig = px.scatter(
        df,
        x="physical_activity",
        y="anxiety_level",
        color="gender",
        title="Physical Activity vs Anxiety",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Physical Activity vs Depression
# ---------------------------------------------------
def physical_activity_vs_depression(df):
    fig = px.box(
        df,
        x="depression_label",
        y="physical_activity",
        color="depression_label",
        title="Physical Activity vs Depression",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Academic Performance Distribution
# ---------------------------------------------------
def academic_distribution(df):
    fig = px.histogram(
        df,
        x="academic_performance",
        title="Academic Performance Distribution",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Correlation Heatmap
# ---------------------------------------------------
def correlation_heatmap(df):

    numeric_df = df.select_dtypes(include="number")

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r",
        title="Correlation Heatmap"
    )

    fig.update_layout(height=800)

    return fig


# ---------------------------------------------------
# Risk Category Chart
# ---------------------------------------------------
def risk_category_chart(df):

    risk_score = (
        df["stress_level"] +
        df["anxiety_level"] +
        df["addiction_level"]
    )

    categories = pd.cut(
        risk_score,
        bins=[0, 10, 20, 30],
        labels=["Low", "Medium", "High"]
    )

    risk_df = categories.value_counts().reset_index()

    risk_df.columns = ["Risk", "Count"]

    fig = px.bar(
        risk_df,
        x="Risk",
        y="Count",
        color="Risk",
        title="Mental Health Risk Categories",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Depression vs Sleep
# ---------------------------------------------------
def depression_vs_sleep(df):
    fig = px.box(
        df,
        x="depression_label",
        y="sleep_hours",
        color="depression_label",
        title="Sleep Hours vs Depression",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Stress vs Academic Performance
# ---------------------------------------------------
def stress_vs_academic(df):
    fig = px.scatter(
        df,
        x="stress_level",
        y="academic_performance",
        color="gender",
        title="Stress vs Academic Performance",
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Radar Chart
# ---------------------------------------------------
def mental_health_radar(df):

    avg_stress = df["stress_level"].mean()
    avg_anxiety = df["anxiety_level"].mean()
    avg_addiction = df["addiction_level"].mean()
    avg_sleep = df["sleep_hours"].mean()

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[
            avg_stress,
            avg_anxiety,
            avg_addiction,
            avg_sleep
        ],
        theta=[
            "Stress",
            "Anxiety",
            "Addiction",
            "Sleep"
        ],
        fill="toself"
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        title="Mental Health Radar Analysis"
    )

    return fig
