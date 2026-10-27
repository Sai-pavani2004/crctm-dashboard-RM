

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ------------------------------------------------------------
# CYBERSECURITY RISK COMMUNICATION THRESHOLD MODEL (CRCTM)
# Streamlit research dashboard
# ------------------------------------------------------------

st.set_page_config(
    page_title="CRCTM | Cybersecurity Risk Communication Threshold Model",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
    .stApp {
        background: #071525;
        color: #f4f7fb;
    }

    section[data-testid="stSidebar"] {
        background: #061321;
        border-right: 1px solid #17324d;
    }

    .brand {
        font-size: 26px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 2px;
    }

    .subtitle {
        color: #8ea8c0;
        font-size: 12px;
        margin-bottom: 20px;
    }

    .hero {
        background: linear-gradient(135deg, #0c2138, #0a192b);
        border: 1px solid #173a5c;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 18px;
    }

    .hero h1 {
        margin: 0;
        font-size: 28px;
        color: white;
    }

    .hero p {
        color: #a9bed1;
        margin-top: 8px;
    }

    .case-card {
        background: #0c1e31;
        border: 1px solid #1b3b59;
        border-radius: 12px;
        padding: 14px;
        text-align: center;
    }

    .case-card h3 {
        margin: 0;
        color: white;
        font-size: 18px;
    }

    .case-card p {
        margin: 4px 0 0;
        color: #8fa9c1;
    }

    .threshold-card {
        background: #0c1e31;
        border: 1px solid #214665;
        border-radius: 15px;
        padding: 17px;
        min-height: 180px;
    }

    .threshold-number {
        font-size: 13px;
        color: #8da9c2;
        font-weight: 700;
    }

    .threshold-title {
        color: white;
        font-size: 17px;
        font-weight: 800;
        margin-top: 6px;
    }

    .threshold-question {
        color: #a5b9cb;
        font-size: 12px;
        min-height: 38px;
        margin-top: 7px;
    }

    .score {
        font-size: 26px;
        font-weight: 800;
        color: white;
    }

    .bar-bg {
        height: 8px;
        background: #23384d;
        border-radius: 20px;
        margin-top: 8px;
    }

    .bar-fill {
        height: 8px;
        border-radius: 20px;
    }

    .metric-box {
        background: #0b1c2d;
        border: 1px solid #193851;
        border-radius: 12px;
        padding: 16px;
    }

    .metric-label {
        color: #91a9bd;
        font-size: 12px;
    }

    .metric-value {
        color: white;
        font-size: 25px;
        font-weight: 800;
    }

    .section-title {
        color: white;
        font-size: 20px;
        font-weight: 800;
        margin: 20px 0 10px;
    }

    .insight {
        background: #0d2033;
        border-left: 4px solid #38bdf8;
        padding: 14px;
        border-radius: 8px;
        color: #b6c9d9;
    }

    .small {
        color: #829bb2;
        font-size: 11px;
    }

    .status-good {
        color: #4ade80;
        font-weight: 800;
    }

    .status-warning {
        color: #fbbf24;
        font-weight: 800;
    }

    .status-critical {
        color: #fb7185;
        font-weight: 800;
    }

    div[data-testid="stMetric"] {
        background: #0b1c2d;
        border: 1px solid #193851;
        padding: 12px;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Research data ----------
# Scores are based on the researcher's existing 10-dimension framework.
# Replace the values with validated scores if your methodology produces
# different values. The interface treats them as researcher-entered scores.

base_data = pd.DataFrame({
    "Metric": [
        "R1 Risk Identification",
        "R2 Risk Assessment",
        "R3 Risk Communication",
        "R4 Communication Timeliness",
        "R5 Risk Escalation",
        "R6 Risk Translation",
        "R7 Decision Response",
        "R8 Remediation",
        "R9 Monitoring",
        "R10 Residual Risk Awareness"
    ],
    "Equifax": [75, 70, 45, 40, 35, 55, 50, 65, 70, 60],
    "Target": [70, 65, 55, 50, 45, 55, 50, 65, 60, 55],
    "Capital One": [75, 45, 60, 55, 50, 40, 55, 65, 70, 60]
})

thresholds = {
    "T1": {
        "name": "Identification Threshold",
        "metrics": ["R1 Risk Identification", "R2 Risk Assessment"],
        "question": "Was the cybersecurity risk recognized and assessed?"
    },
    "T2": {
        "name": "Communication Threshold",
        "metrics": ["R3 Risk Communication", "R4 Communication Timeliness"],
        "question": "Did the risk information reach the right people on time?"
    },
    "T3": {
        "name": "Escalation Threshold",
        "metrics": ["R5 Risk Escalation", "R6 Risk Translation"],
        "question": "Was the risk escalated and translated into organizational/business impact?"
    },
    "T4": {
        "name": "Leadership Decision Threshold",
        "metrics": ["R7 Decision Response", "R8 Remediation"],
        "question": "Was the risk understood and acted upon by leadership?"
    },
    "T5": {
        "name": "Monitoring Threshold",
        "metrics": ["R9 Monitoring", "R10 Residual Risk Awareness"],
        "question": "Was residual risk monitored and communicated after response?"
    }
}

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown('<div class="brand">🛡️ CRCTM</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Cybersecurity Risk Communication Threshold Model</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        ["Dashboard", "Threshold Analysis", "Case Studies", "Metrics", "Methodology"],
        label_visibility="collapsed"
    )

    st.divider()
    st.caption("Research Dashboard")
    st.caption("Multiple Case Study Analysis")
    st.caption("Equifax • Target • Capital One")

# ---------- Helpers ----------
def get_case_score(case, threshold_key):
    metric_names = thresholds[threshold_key]["metrics"]
    values = []
    for metric in metric_names:
        values.append(
            float(base_data.loc[base_data["Metric"] == metric, case].iloc[0])
        )
    return sum(values) / len(values)

def get_status(score):
    # Researcher-defined analytical thresholds.
    if score < 40:
        return "Critical"
    elif score < 60:
        return "Weak"
    elif score < 80:
        return "Adequate"
    return "Effective"

def status_class(status):
    if status == "Critical":
        return "status-critical"
    if status == "Weak":
        return "status-warning"
    return "status-good"

def score_color(score):
    if score < 40:
        return "#fb7185"
    if score < 60:
        return "#fbbf24"
    if score < 80:
        return "#38bdf8"
    return "#4ade80"

# ---------- DASHBOARD ----------
if page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <h1>Cybersecurity Risk Communication Threshold Model</h1>
        <p>
        A research dashboard for analysing where cybersecurity risk communication
        breaks down between security management and organisational leadership.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Case cards
    c1, c2, c3 = st.columns(3)
    for col, case, year in [
        (c1, "Equifax", "2017"),
        (c2, "Target", "2013"),
        (c3, "Capital One", "2019")
    ]:
        with col:
            st.markdown(
                f"""
                <div class="case-card">
                    <h3>{case}</h3>
                    <p>Case Study • {year}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown('<div class="section-title">Five-Stage Threshold Model</div>',
                unsafe_allow_html=True)

    selected_case = st.selectbox(
        "Select case for threshold analysis",
        ["Equifax", "Target", "Capital One"]
    )

    cols = st.columns(5)
    threshold_scores = {}

    for col, (key, info) in zip(cols, thresholds.items()):
        score = get_case_score(selected_case, key)
        threshold_scores[key] = score
        status = get_status(score)
        color = score_color(score)

        with col:
            st.markdown(
                f"""
                <div class="threshold-card">
                    <div class="threshold-number">{key}</div>
                    <div class="threshold-title">{info["name"]}</div>
                    <div class="threshold-question">{info["question"]}</div>
                    <div class="score">{score:.0f}%</div>
                    <div class="bar-bg">
                        <div class="bar-fill"
                             style="width:{score}%; background:{color};"></div>
                    </div>
                    <div class="{status_class(status)}"
                         style="margin-top:8px; font-size:12px;">
                         {status}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    overall_score = sum(threshold_scores.values()) / len(threshold_scores)
    overall_status = get_status(overall_score)

    st.markdown('<div class="section-title">Overall Model Status</div>',
                unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Overall Threshold Score", f"{overall_score:.0f}%")
    m2.metric("Weakest Threshold",
              min(threshold_scores, key=threshold_scores.get))
    m3.metric("Strongest Threshold",
              max(threshold_scores, key=threshold_scores.get))
    m4.metric("Model Status", overall_status)

    # Radar chart
    st.markdown('<div class="section-title">Threshold Profile</div>',
                unsafe_allow_html=True)

    radar = go.Figure()

    radar.add_trace(go.Scatterpolar(
        r=list(threshold_scores.values()) + [list(threshold_scores.values())[0]],
        theta=list(thresholds.keys()) + ["T1"],
        fill="toself",
        name=selected_case
    ))

    radar.update_layout(
        paper_bgcolor="#071525",
        plot_bgcolor="#071525",
        font_color="#dbeafe",
        polar=dict(
            bgcolor="#071525",
            radialaxis=dict(range=[0, 100], gridcolor="#29445b"),
            angularaxis=dict(gridcolor="#29445b")
        ),
        height=430,
        margin=dict(l=40, r=40, t=30, b=30)
    )

    st.plotly_chart(radar, use_container_width=True)

    # Insight
    weakest = min(threshold_scores, key=threshold_scores.get)
    strongest = max(threshold_scores, key=threshold_scores.get)

    st.markdown(
        f"""
        <div class="insight">
        <b>Research insight:</b>
        For the selected case, the lowest threshold is
        <b>{weakest} – {thresholds[weakest]["name"]}</b>
        ({threshold_scores[weakest]:.0f}%).
        The strongest threshold is
        <b>{strongest} – {thresholds[strongest]["name"]}</b>
        ({threshold_scores[strongest]:.0f}%).
        This identifies the stage at which the risk communication pathway
        shows the greatest weakness.
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- THRESHOLD ANALYSIS ----------
elif page == "Threshold Analysis":

    st.markdown('<div class="hero"><h1>Threshold Analysis</h1>'
                '<p>Examine the five thresholds and the metrics contributing to each threshold.</p>'
                '</div>', unsafe_allow_html=True)

    selected_case = st.selectbox(
        "Case Study",
        ["Equifax", "Target", "Capital One"],
        key="analysis_case"
    )

    rows = []

    for key, info in thresholds.items():
        score = get_case_score(selected_case, key)
        rows.append({
            "Threshold": f"{key} – {info['name']}",
            "Indicators": " + ".join(info["metrics"]),
            "Score": round(score, 1),
            "Status": get_status(score),
            "Threshold Question": info["question"]
        })

    df = pd.DataFrame(rows)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Score": st.column_config.ProgressColumn(
                "Score",
                min_value=0,
                max_value=100,
                format="%.0f%%"
            )
        }
    )

    st.markdown('<div class="section-title">Threshold Decision Logic</div>',
                unsafe_allow_html=True)

    threshold_to_explain = st.selectbox(
        "Select threshold",
        list(thresholds.keys()),
        format_func=lambda x: f"{x} – {thresholds[x]['name']}"
    )

    score = get_case_score(selected_case, threshold_to_explain)
    status = get_status(score)

    if score < 60:
        st.error(
            f"{threshold_to_explain} is below the researcher-defined 60% "
            f"adequacy threshold. Score: {score:.0f}% ({status})."
        )
    else:
        st.success(
            f"{threshold_to_explain} meets the researcher-defined 60% "
            f"adequacy threshold. Score: {score:.0f}% ({status})."
        )

# ---------- CASE STUDIES ----------
elif page == "Case Studies":

    st.markdown('<div class="hero"><h1>Case Studies</h1>'
                '<p>Compare the threshold profile of the three documented cases.</p>'
                '</div>', unsafe_allow_html=True)

    cases = ["Equifax", "Target", "Capital One"]

    comparison = []
    for case in cases:
        row = {"Case": case}
        for key, info in thresholds.items():
            row[key] = round(get_case_score(case, key), 1)
        row["Overall"] = round(
            sum(row[key] for key in thresholds) / len(thresholds), 1
        )
        comparison.append(row)

    comparison_df = pd.DataFrame(comparison)

    st.dataframe(
        comparison_df,
        use_container_width=True,
        hide_index=True
    )

    long_df = comparison_df.melt(
        id_vars="Case",
        value_vars=list(thresholds.keys()),
        var_name="Threshold",
        value_name="Score"
    )

    fig = px.bar(
        long_df,
        x="Threshold",
        y="Score",
        color="Case",
        barmode="group",
        range_y=[0, 100],
        text_auto=".0f"
    )

    fig.update_layout(
        paper_bgcolor="#071525",
        plot_bgcolor="#071525",
        font_color="#dbeafe",
        xaxis=dict(gridcolor="#29445b"),
        yaxis=dict(gridcolor="#29445b"),
        height=480
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        <div class="insight">
        <b>Cross-case interpretation:</b>
        The model allows the researcher to identify whether failures occur
        primarily during identification, communication, escalation,
        leadership decision-making, or monitoring.
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- METRICS ----------
elif page == "Metrics":

    st.markdown('<div class="hero"><h1>Research Metrics</h1>'
                '<p>R1–R10 dimensions used to construct the five threshold stages.</p>'
                '</div>', unsafe_allow_html=True)

    st.dataframe(
        base_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Equifax": st.column_config.ProgressColumn(
                "Equifax", min_value=0, max_value=100, format="%.0f%%"
            ),
            "Target": st.column_config.ProgressColumn(
                "Target", min_value=0, max_value=100, format="%.0f%%"
            ),
            "Capital One": st.column_config.ProgressColumn(
                "Capital One", min_value=0, max_value=100, format="%.0f%%"
            )
        }
    )

    selected_metric = st.selectbox(
        "Select metric",
        base_data["Metric"].tolist()
    )

    metric_row = base_data[base_data["Metric"] == selected_metric].iloc[0]

    a, b, c = st.columns(3)
    a.metric("Equifax", f"{metric_row['Equifax']:.0f}%")
    b.metric("Target", f"{metric_row['Target']:.0f}%")
    c.metric("Capital One", f"{metric_row['Capital One']:.0f}%")

# ---------- METHODOLOGY ----------
elif page == "Methodology":

    st.markdown('<div class="hero"><h1>Model Methodology</h1>'
                '<p>How the proposed CRCTM can be used in your multiple-case-study research.</p>'
                '</div>', unsafe_allow_html=True)

    st.markdown("### 1. Model purpose")
    st.write(
        "The proposed Cybersecurity Risk Communication Threshold Model (CRCTM) "
        "is designed to analyse where cybersecurity risk information fails to "
        "progress from identification through organisational action."
    )

    st.markdown("### 2. Five thresholds")

    methodology_rows = []
    for key, info in thresholds.items():
        methodology_rows.append({
            "Threshold": key,
            "Stage": info["name"],
            "Indicators": ", ".join(info["metrics"]),
            "Core question": info["question"]
        })

    st.table(pd.DataFrame(methodology_rows))

    st.markdown("### 3. Researcher-defined scoring")
    st.write(
        "The dashboard uses a 0–100 analytical score. These scores are "
        "researcher-entered and should be replaced or recalculated from the "
        "coding scheme developed during the case-study analysis."
    )

    st.warning(
        "For academic reporting, describe the numerical cut-offs as "
        "researcher-defined analytical thresholds unless they are empirically "
        "validated using additional cases or quantitative data."
    )

    st.markdown("### 4. Suggested research interpretation")
    st.write(
        "A threshold is considered to have a communication weakness when the "
        "available case evidence indicates that the required information, "
        "escalation, translation, leadership response, or monitoring process "
        "did not adequately progress to the next stage."
    )

    st.markdown("### 5. Suggested validation")
    st.write(
        "For stronger validation, apply the same coding framework to additional "
        "cybersecurity incidents and compare whether the same threshold stages "
        "repeatedly explain communication failures."
    )

st.divider()
st.caption(
    "CRCTM v1.0 | Proposed research interface | "
    "Equifax (2017) • Target (2013) • Capital One (2019)"
)

