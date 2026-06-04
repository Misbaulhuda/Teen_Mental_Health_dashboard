# utils/insights.py

import pandas as pd
import numpy as np


# =====================================================
# BASIC KPI METRICS
# =====================================================

def get_kpis(df):

    kpis = {
        "Total Records": len(df),
        "Average Age": round(df["age"].mean(), 2),
        "Average Stress": round(df["stress_level"].mean(), 2),
        "Average Anxiety": round(df["anxiety_level"].mean(), 2),
        "Average Sleep": round(df["sleep_hours"].mean(), 2),
        "Average Addiction": round(df["addiction_level"].mean(), 2)
    }

    return kpis


# =====================================================
# HIGH RISK STUDENTS
# =====================================================

def get_high_risk_students(df):

    high_risk = df[
        (df["stress_level"] >= 8)
        &
        (df["anxiety_level"] >= 8)
        &
        (df["addiction_level"] >= 7)
    ]

    return high_risk


# =====================================================
# LOW RISK STUDENTS
# =====================================================

def get_low_risk_students(df):

    low_risk = df[
        (df["stress_level"] <= 4)
        &
        (df["anxiety_level"] <= 4)
        &
        (df["addiction_level"] <= 4)
    ]

    return low_risk


# =====================================================
# RISK SCORE
# =====================================================

def calculate_risk_score(df):

    risk_score = (
        df["stress_level"] * 0.4
        +
        df["anxiety_level"] * 0.4
        +
        df["addiction_level"] * 0.2
    )

    return risk_score.round(2)


# =====================================================
# RISK CATEGORIES
# =====================================================

def risk_segmentation(df):

    temp_df = df.copy()

    temp_df["risk_score"] = calculate_risk_score(temp_df)

    temp_df["risk_category"] = pd.cut(
        temp_df["risk_score"],
        bins=[0, 4, 7, 10],
        labels=["Low", "Medium", "High"]
    )

    return temp_df


# =====================================================
# DEPRESSION RATE
# =====================================================

def depression_rate(df):

    if "depression_label" not in df.columns:
        return 0

    depressed = (
        df["depression_label"]
        .astype(str)
        .str.lower()
        .isin(["yes", "1", "true", "depressed"])
        .sum()
    )

    rate = (depressed / len(df)) * 100

    return round(rate, 2)


# =====================================================
# STRESS ANALYSIS
# =====================================================

def stress_analysis(df):

    avg_stress = df["stress_level"].mean()

    if avg_stress < 4:
        status = "Low Stress Population"

    elif avg_stress < 7:
        status = "Moderate Stress Population"

    else:
        status = "High Stress Population"

    return {
        "average_stress": round(avg_stress, 2),
        "status": status
    }


# =====================================================
# ANXIETY ANALYSIS
# =====================================================

def anxiety_analysis(df):

    avg_anxiety = df["anxiety_level"].mean()

    if avg_anxiety < 4:
        status = "Low Anxiety"

    elif avg_anxiety < 7:
        status = "Moderate Anxiety"

    else:
        status = "High Anxiety"

    return {
        "average_anxiety": round(avg_anxiety, 2),
        "status": status
    }


# =====================================================
# SLEEP ANALYSIS
# =====================================================

def sleep_analysis(df):

    avg_sleep = df["sleep_hours"].mean()

    if avg_sleep < 6:
        category = "Poor Sleep"

    elif avg_sleep < 8:
        category = "Average Sleep"

    else:
        category = "Healthy Sleep"

    return {
        "average_sleep": round(avg_sleep, 2),
        "category": category
    }


# =====================================================
# SOCIAL MEDIA ANALYSIS
# =====================================================

def social_media_analysis(df):

    avg_usage = df["social_media_hours"].mean()

    if avg_usage < 2:
        category = "Low Usage"

    elif avg_usage < 5:
        category = "Moderate Usage"

    else:
        category = "Heavy Usage"

    return {
        "average_usage": round(avg_usage, 2),
        "category": category
    }


# =====================================================
# TOP PLATFORM
# =====================================================

def most_used_platform(df):

    if "platform_usage" not in df.columns:
        return "Unknown"

    return df["platform_usage"].mode()[0]


# =====================================================
# CORRELATION INSIGHTS
# =====================================================

def correlation_insights(df):

    numeric = df.select_dtypes(include=np.number)

    corr = numeric.corr()

    insights = {}

    try:
        insights["Sleep vs Stress"] = round(
            corr.loc["sleep_hours", "stress_level"],
            2
        )
    except:
        pass

    try:
        insights["Sleep vs Anxiety"] = round(
            corr.loc["sleep_hours", "anxiety_level"],
            2
        )
    except:
        pass

    try:
        insights["Social Media vs Stress"] = round(
            corr.loc["social_media_hours", "stress_level"],
            2
        )
    except:
        pass

    try:
        insights["Social Media vs Anxiety"] = round(
            corr.loc["social_media_hours", "anxiety_level"],
            2
        )
    except:
        pass

    return insights


# =====================================================
# AUTO GENERATED FINDINGS
# =====================================================

def generate_findings(df):

    findings = []

    avg_sleep = df["sleep_hours"].mean()
    avg_stress = df["stress_level"].mean()
    avg_anxiety = df["anxiety_level"].mean()

    if avg_sleep < 6:
        findings.append(
            "Students are getting less than recommended sleep."
        )

    if avg_stress > 6:
        findings.append(
            "Stress levels are significantly high."
        )

    if avg_anxiety > 6:
        findings.append(
            "Anxiety levels are above normal range."
        )

    if "social_media_hours" in df.columns:

        avg_social = df["social_media_hours"].mean()

        if avg_social > 5:
            findings.append(
                "Social media usage is very high."
            )

    return findings


# =====================================================
# RECOMMENDATIONS
# =====================================================

def generate_recommendations(df):

    recommendations = []

    if df["sleep_hours"].mean() < 7:
        recommendations.append(
            "Encourage better sleep habits."
        )

    if df["stress_level"].mean() > 6:
        recommendations.append(
            "Provide stress management workshops."
        )

    if df["anxiety_level"].mean() > 6:
        recommendations.append(
            "Offer mental health counseling."
        )

    if df["social_media_hours"].mean() > 5:
        recommendations.append(
            "Promote digital wellness awareness."
        )

    if df["physical_activity"].mean() < 3:
        recommendations.append(
            "Increase physical activity programs."
        )

    return recommendations


# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

def executive_summary(df):

    summary = {
        "Total Students": len(df),
        "High Risk Students":
            len(get_high_risk_students(df)),
        "Low Risk Students":
            len(get_low_risk_students(df)),
        "Depression Rate (%)":
            depression_rate(df),
        "Most Used Platform":
            most_used_platform(df)
    }

    return summary
