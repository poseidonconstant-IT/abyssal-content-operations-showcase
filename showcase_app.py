"""Standalone, portfolio-safe architecture visualization.

This demo deliberately contains no credentials, production data, network calls,
or publishing controls.
"""

import streamlit as st


st.set_page_config(page_title="The Abyssal Capital | Case Study", page_icon="◈", layout="wide")

st.markdown("""
<style>
.stApp { background: #f6f8fb; color: #172033; }
.block-container { max-width: 1180px; padding-top: 2.5rem; }
.hero, .panel { background: #fff; border: 1px solid #d6deea; box-shadow: 0 4px 14px rgba(21,35,58,.06); }
.hero { border-left: 7px solid #176b73; padding: 2.4rem; }
.panel { border-top: 3px solid #176b73; padding: 1.25rem; min-height: 170px; }
.kicker { color: #0f6972; font: 700 .78rem monospace; letter-spacing: .13em; }
.flow { border-left: 4px solid #176b73; background: #fff; margin: .55rem 0; padding: .9rem 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<section class="hero">
<div class="kicker">PYTHON · AI AUTOMATION · PRODUCTION OPERATIONS</div>
<h1>The Abyssal Capital</h1>
<p>Portfolio-safe architecture visualization for an AI-assisted financial-content operations platform.</p>
</section>
""", unsafe_allow_html=True)

st.write("")
left, right = st.columns([1.15, 1], gap="large")
with left:
    st.subheader("Delivery pipeline")
    for step in (
        "RSS ingestion → duplicate suppression → topic routing",
        "Gemini-assisted drafting → quality gates → human approval / HOLD",
        "Output-language validation → platform-specific presentation",
        "Telegram + Facebook + X delivery → per-channel retry → audit log",
    ):
        st.markdown(f'<div class="flow">{step}</div>', unsafe_allow_html=True)
with right:
    st.subheader("Scheduling and controls")
    st.markdown("""<div class="panel"><h3>Deterministic release windows</h3>
    <p><b>Preparation:</b> 05:30 · 11:30 · 17:30 ICT</p>
    <p><b>Publishing:</b> 06:00 · 12:00 · 18:00 ICT</p>
    <p><b>Review:</b> human HOLD window before release</p></div>""", unsafe_allow_html=True)

st.subheader("Engineering evidence")
cards = st.columns(3, gap="large")
items = (
    ("Safe AI output", "Validation blocks unchecked output before delivery."),
    ("Failure isolation", "Retries target only the failed destination; successful channels are not duplicated."),
    ("Operational design", "Authenticated controls are separated from this read-only portfolio view."),
)
for column, (title, text) in zip(cards, items):
    with column:
        st.markdown(f'<div class="panel"><h3>{title}</h3><p>{text}</p></div>', unsafe_allow_html=True)

st.caption("Educational financial content only. No credentials, production data, post text, or publishing controls are included in this public demonstration.")
