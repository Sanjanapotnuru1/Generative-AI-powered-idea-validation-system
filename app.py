import streamlit as st
from main import full_analysis
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Idea Validator", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.block-container { padding-top: 2rem; }

/* Hero */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #6b7280;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Feature Cards */
.feature-card {
    background: #ffffff;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #e5e7eb;
    transition: 0.3s;
}
.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

/* Colored Cards */
.card-blue {background:#e0f2fe;padding:18px;border-radius:14px;}
.card-green {background:#ecfdf5;padding:18px;border-radius:14px;}
.card-yellow {background:#fef9c3;padding:18px;border-radius:14px;}
.card-pink {background:#fce7f3;padding:18px;border-radius:14px;}
.card-gray {background:#f3f4f6;padding:18px;border-radius:14px;}

.big-text {
    font-size: 17px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("<div class='title'>🚀 AI Idea Validator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Turn your startup ideas into actionable insights</div>", unsafe_allow_html=True)

# ---------------- FEATURES ----------------
col1, col2, col3 = st.columns(3)

col1.markdown("""
<div class='feature-card'>
<h3>💡 Idea Analysis</h3>
<p>Understand feasibility, users, and business potential.</p>
</div>
""", unsafe_allow_html=True)

col2.markdown("""
<div class='feature-card'>
<h3>📊 Smart Insights</h3>
<p>Identify risks, challenges, and opportunities.</p>
</div>
""", unsafe_allow_html=True)

col3.markdown("""
<div class='feature-card'>
<h3>📅 Execution Plan</h3>
<p>Get actionable roadmap to build your idea.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------- INPUT ----------------
st.subheader("💡 Enter Your Idea")
idea = st.text_area("Describe your startup idea in 1–2 lines:")

# ---------------- BUTTON ----------------
if st.button("✨ Analyze Idea"):

    if idea.strip() == "":
        st.warning("Please enter an idea")
        st.stop()

    # ---------------- LOADING ----------------
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)
        time.sleep(0.01)

    data = full_analysis(idea)
    st.success("Analysis Complete ✅")

    scores = data.get("scores", {})

    # ---------------- TABS ----------------
    tab1, tab2, tab3 = st.tabs(["📊 Overview", "🧠 Insights", "📅 Plan"])

    # =========================
    # 📊 OVERVIEW
    # =========================
    with tab1:

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("⭐ Final", data.get("final", ""))
        c2.metric("⚙ Feasibility", scores.get("feasibility", ""))
        c3.metric("🚀 Innovation", scores.get("innovation", ""))
        c4.metric("📈 Market", scores.get("market", ""))

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"<div class='card-blue big-text'><b>Tech:</b><br>{data.get('tech','')}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card-green big-text'><b>Business:</b><br>{data.get('business','')}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card-yellow big-text'><b>User:</b><br>{data.get('user','')}</div>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"<div class='card-pink big-text'><b>Investor:</b><br>{data.get('investor','')}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card-gray big-text'><b>Risk:</b><br>{data.get('risk','')}</div>", unsafe_allow_html=True)

    # =========================
    # 🧠 INSIGHTS
    # =========================
    with tab2:

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"<div class='card-yellow big-text'><b>Challenges:</b><br>{data.get('challenges','')}</div>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"<div class='card-blue big-text'><b>Dependencies:</b><br>{data.get('dependencies','')}</div>", unsafe_allow_html=True)

        st.divider()

        st.subheader("🚀 Improvements")
        for imp in data.get("improve", []):
            st.markdown(f"<div class='card-green big-text'>• {imp}</div>", unsafe_allow_html=True)

        st.subheader("🎯 Solution")
        st.markdown(f"<div class='card-blue big-text'>{data.get('solution','')}</div>", unsafe_allow_html=True)

        st.subheader("👉 Next Steps")
        for step in data.get("next_steps", []):
            st.markdown(f"<div class='card-gray big-text'>• {step}</div>", unsafe_allow_html=True)

    # =========================
    # 📅 PLAN (DIFFERENT FROM NEXT STEPS)
    # =========================
    with tab3:

        st.subheader("📅 Execution Plan")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div style="background:#e0f2fe;padding:18px;border-radius:12px;">
            <b>Phase 1: Validation</b><br>
            Test idea with users and validate demand using small experiments.<br><br>
            ⏳ Timeline: 2–3 weeks<br>
            🔥 Priority: High
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="background:#ecfdf5;padding:18px;border-radius:12px;">
            <b>Phase 2: MVP Development</b><br>
            Build a basic product version focusing on core features and usability.<br><br>
            ⏳ Timeline: 3–5 weeks<br>
            ⚡ Priority: Medium
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        st.subheader("📊 Strategic Insight")

        st.markdown(f"""
        <div class='card-gray big-text'>
        {data.get("score_insight","")}
        </div>
        """, unsafe_allow_html=True)

        verdict = data.get("verdict", "").lower()

        if verdict == "good":
            st.success(f"🏁 Verdict: {verdict.capitalize()} — Strong potential 🚀")
        else:
            st.warning(f"🏁 Verdict: {verdict.capitalize()} — Needs improvement ⚠️")