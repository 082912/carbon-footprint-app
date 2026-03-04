"""
🌱 AI-Powered Carbon Footprint Intelligence System
===================================================
Author: AI/ML Engineer
Description: A Streamlit app that predicts carbon footprint using dropdown inputs,
             displays eco score, and provides personalized sustainability recommendations.
"""

import streamlit as st
import random

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🌱 Carbon Footprint Intelligence",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM CSS — Soft green eco-style UI with modern fonts
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Playfair+Display:wght@700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif;
    }

    /* ── Soft green background ── */
    .stApp {
        background: linear-gradient(160deg, #f0faf0, #e8f5e9, #f5fdf5);
    }

    /* ── Title — Playfair Display, dark green ── */
    h1 {
        font-family: 'Playfair Display', serif !important;
        color: #1b5e20 !important;
        -webkit-text-fill-color: #1b5e20 !important;
        font-size: 2.6rem !important;
        font-weight: 700 !important;
        text-align: center;
        letter-spacing: -0.5px;
        padding-bottom: 0.2rem;
    }

    /* ── Subheadings — dark green ── */
    h2, h3 {
        font-family: 'Nunito', sans-serif !important;
        color: #2e7d32 !important;
        font-weight: 800 !important;
    }

    /* ── Paragraph text ── */
    p, li, label {
        color: #1b5e20 !important;
        font-family: 'Nunito', sans-serif !important;
    }

    /* ── Selectbox label ── */
    .stSelectbox label {
        color: #2e7d32 !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
    }

    /* ── Selectbox dropdown ── */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 2px solid #66bb6a !important;
        border-radius: 12px !important;
        color: #1b5e20 !important;
        font-family: 'Nunito', sans-serif !important;
        font-weight: 600 !important;
    }

    /* ── Eco Style Button ── */
    .stButton > button {
        background: linear-gradient(135deg, #2e7d32, #43a047, #66bb6a);
        color: #ffffff !important;
        font-family: 'Nunito', sans-serif !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        border: none;
        border-radius: 50px;
        padding: 0.75rem 2rem;
        width: 100%;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(46, 125, 50, 0.35);
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(46, 125, 50, 0.5);
        background: linear-gradient(135deg, #1b5e20, #2e7d32, #43a047);
    }

    /* ── Recommendation Cards ── */
    .recommend-card {
        background: #ffffff;
        border-left: 5px solid #43a047;
        border-radius: 12px;
        padding: 1rem 1.3rem;
        margin: 0.6rem 0;
        color: #1b5e20 !important;
        font-size: 0.95rem;
        font-family: 'Nunito', sans-serif;
        box-shadow: 0 2px 10px rgba(46, 125, 50, 0.1);
    }

    /* ── Divider ── */
    .section-divider {
        border: none;
        border-top: 2px solid #c8e6c9;
        margin: 1.5rem 0;
    }

    /* ── Metric labels ── */
    [data-testid="stMetricLabel"] {
        color: #2e7d32 !important;
        font-weight: 700 !important;
    }

    [data-testid="stMetricValue"] {
        color: #1b5e20 !important;
        font-weight: 800 !important;
    }

    /* ── Progress bar ── */
    .stProgress > div > div {
        background: linear-gradient(90deg, #43a047, #66bb6a) !important;
        border-radius: 10px !important;
    }

    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# DROPDOWN → NUMERICAL MAPPING LOGIC
# ─────────────────────────────────────────────────────────────────────────────
FUEL_MAP = {
    "Electric": 1,
    "Hybrid":   2,
    "Diesel":   3,
    "Petrol":   4
}

TRANSPORT_MAP = {
    "Train":   1,
    "Bus":     2,
    "Bike":    3,
    "Car":     4,
    "Flight":  5
}

FOOD_MAP = {
    "Vegetarian":     1,
    "Non-Vegetarian": 2
}

ELECTRICITY_MAP = {
    "Low":    1,
    "Medium": 2,
    "High":   3
}

LPG_MAP = {
    "Low":    1,
    "Medium": 2,
    "High":   3
}

FREQUENCY_MAP = {
    "Rare":       1,
    "Occasional": 2,
    "Frequent":   3
}


# ─────────────────────────────────────────────────────────────────────────────
# CARBON FOOTPRINT PREDICTION LOGIC
# ─────────────────────────────────────────────────────────────────────────────
def predict_carbon_footprint(fuel, transport, food, electricity, lpg, frequency):
    WEIGHTS = {
        "fuel":        18.0,
        "transport":   25.0,
        "food":        20.0,
        "electricity": 15.0,
        "lpg":         10.0,
        "frequency":   12.0
    }
    score = (
        fuel        * WEIGHTS["fuel"]        +
        transport   * WEIGHTS["transport"]   +
        food        * WEIGHTS["food"]        +
        electricity * WEIGHTS["electricity"] +
        lpg         * WEIGHTS["lpg"]         +
        frequency   * WEIGHTS["frequency"]
    )
    variance = score * random.uniform(-0.05, 0.05)
    return round(score + variance, 2)


# ─────────────────────────────────────────────────────────────────────────────
# ECO SCORE CALCULATION
# ─────────────────────────────────────────────────────────────────────────────
def calculate_eco_score(carbon_kg):
    MAX_CARBON = 1000
    MIN_CARBON = 100
    carbon_kg = max(MIN_CARBON, min(MAX_CARBON, carbon_kg))
    eco_score = 100 - ((carbon_kg - MIN_CARBON) / (MAX_CARBON - MIN_CARBON)) * 100
    return round(eco_score, 1)


def get_eco_tier(eco_score):
    if eco_score >= 80:
        return "🌟 Excellent"
    elif eco_score >= 60:
        return "🌿 Good"
    elif eco_score >= 40:
        return "⚡ Average"
    elif eco_score >= 20:
        return "⚠️ Poor"
    else:
        return "🔴 Critical"


# ─────────────────────────────────────────────────────────────────────────────
# RECOMMENDATION ENGINE
# ─────────────────────────────────────────────────────────────────────────────
def get_recommendations(fuel_label, transport_label, food_label,
                         electricity_label, lpg_label, frequency_label):
    tips = []

    if fuel_label in ["Petrol", "Diesel"]:
        tips.append("🚗 **Switch to Electric or Hybrid** — Electric vehicles produce zero tailpipe emissions. Even a hybrid can cut your fuel emissions by 30–50%.")
    elif fuel_label == "Hybrid":
        tips.append("🔋 **Great choice on Hybrid!** Consider upgrading to a fully Electric vehicle for your next purchase to eliminate fuel emissions entirely.")
    else:
        tips.append("⚡ **Excellent! You're on Electric.** Ensure you charge using renewable energy (solar/wind) to maximise your green impact.")

    if transport_label == "Flight":
        tips.append("✈️ **Reduce Air Travel** — A single long-haul flight can emit 1–3 tonnes of CO2. Consider trains for shorter trips or video conferencing for business meetings.")
    elif transport_label == "Car":
        tips.append("🚌 **Try Public Transport 2–3 days/week** — Switching even partially to bus or train can cut your transport emissions by up to 40%.")
    elif transport_label == "Bike":
        tips.append("🛵 **Consider carpooling or EVs** — Switching from a petrol bike to an e-scooter or e-bike is a smart, low-cost upgrade.")
    elif transport_label == "Bus":
        tips.append("🚆 **You're doing great with public transport!** Trains are even greener — try combining bus + train routes where possible.")
    else:
        tips.append("🚆 **Train travel is one of the greenest choices!** Keep it up and encourage others to use rail over road or air.")

    if food_label == "Non-Vegetarian":
        tips.append("🥦 **Try Meatless Mondays** — Beef and lamb are the most carbon-intensive foods. Reducing red meat twice a week can lower your food footprint by ~20%. Explore lentils, tofu, and chickpeas.")
    else:
        tips.append("🌱 **Plant-based diet — amazing!** You're already making one of the biggest individual impacts. Also buy local and seasonal produce to further cut transport emissions.")

    if electricity_label == "High":
        tips.append("💡 **Reduce Electricity Usage** — Switch to LED bulbs (75% less energy), unplug idle devices, use 5-star rated appliances, and consider rooftop solar panels.")
    elif electricity_label == "Medium":
        tips.append("🔌 **Optimise Energy Use** — Set your AC to 24°C+, use timers on geysers, and switch off lights in unoccupied rooms. Small habits add up to big savings.")
    else:
        tips.append("⚡ **Low electricity use — well done!** Consider investing in solar panels to become energy self-sufficient and even sell surplus back to the grid.")

    if lpg_label == "High":
        tips.append("🍳 **Reduce LPG Consumption** — Use pressure cookers (save up to 70% energy), switch to induction cooking for some meals, and avoid cooking on unnecessarily high flame.")
    elif lpg_label == "Medium":
        tips.append("🔥 **Moderate LPG use is manageable.** Try batch cooking and using lids on pots to retain heat — this noticeably reduces gas usage.")
    else:
        tips.append("🌿 **Great LPG discipline!** If you haven't already, an induction cooktop as a complement will further reduce your fossil fuel dependence at home.")

    if frequency_label == "Frequent":
        tips.append("🗓️ **Travel Less Frequently** — Consolidate trips, work remotely when possible, and use carbon offset programs for unavoidable travel. One fewer flight per year makes a measurable difference.")
    elif frequency_label == "Occasional":
        tips.append("🌍 **Occasional traveller — good balance.** When you do travel, choose trains over planes and stay in eco-certified accommodations.")
    else:
        tips.append("🏡 **Rare traveller — excellent!** Your low travel frequency significantly helps your carbon score. Encourage telecommuting and virtual meetings in your network too.")

    return tips


# ─────────────────────────────────────────────────────────────────────────────
# MAIN APP UI
# ─────────────────────────────────────────────────────────────────────────────

st.title("🌿 Carbon Footprint Intelligence")
st.markdown(
    "<p style='text-align:center; color:#388e3c; font-size:1.05rem; font-family:Nunito,sans-serif;'>"
    "AI-powered analysis of your personal carbon footprint with actionable sustainability insights."
    "</p>",
    unsafe_allow_html=True
)

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

st.subheader("📋 Your Lifestyle Profile")
st.markdown(
    "<p style='color:#2e7d32;'>Select the options that best describe your daily habits.</p>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    fuel_label = st.selectbox(
        "⛽ Fuel Type",
        options=list(FUEL_MAP.keys()),
        help="What type of fuel does your primary vehicle use?"
    )
    food_label = st.selectbox(
        "🍽️ Food Habit",
        options=list(FOOD_MAP.keys()),
        help="Your typical diet pattern"
    )
    lpg_label = st.selectbox(
        "🔥 LPG Usage Level",
        options=list(LPG_MAP.keys()),
        help="Low = minimal cooking gas, High = heavy daily use"
    )

with col2:
    transport_label = st.selectbox(
        "🚗 Primary Transport Mode",
        options=list(TRANSPORT_MAP.keys()),
        help="Your most frequently used mode of transport"
    )
    electricity_label = st.selectbox(
        "💡 Electricity Usage Level",
        options=list(ELECTRICITY_MAP.keys()),
        help="Low <100 units, Medium 100–300, High >300 units/month"
    )
    frequency_label = st.selectbox(
        "✈️ Travel Frequency",
        options=list(FREQUENCY_MAP.keys()),
        help="How often do you travel (by any mode)?"
    )

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🌱 Analyse My Carbon Footprint"):

    fuel_val        = FUEL_MAP[fuel_label]
    transport_val   = TRANSPORT_MAP[transport_label]
    food_val        = FOOD_MAP[food_label]
    electricity_val = ELECTRICITY_MAP[electricity_label]
    lpg_val         = LPG_MAP[lpg_label]
    frequency_val   = FREQUENCY_MAP[frequency_label]

    carbon_kg  = predict_carbon_footprint(fuel_val, transport_val, food_val, electricity_val, lpg_val, frequency_val)
    eco_score  = calculate_eco_score(carbon_kg)
    tier_label = get_eco_tier(eco_score)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
    st.subheader("📊 Your Carbon Footprint Report")

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(
            label="🌫️ Monthly CO₂ Emissions",
            value=f"{carbon_kg} kg",
            delta=f"{round(carbon_kg * 12 / 1000, 1)} tonnes/year",
            delta_color="inverse"
        )
    with m2:
        st.metric(
            label="🌿 Eco Score",
            value=f"{eco_score} / 100",
            help="Higher is better. 80+ is excellent."
        )
    with m3:
        st.metric(
            label="🏆 Sustainability Tier",
            value=tier_label,
            help="Based on your eco score out of 100"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if eco_score >= 70:
        st.success(f"✅ **{tier_label}** — You have a low carbon footprint! Your choices are making a real difference for the planet.")
    elif eco_score >= 40:
        st.warning(f"⚡ **{tier_label}** — Your footprint is moderate. Small lifestyle adjustments can significantly improve your impact.")
    else:
        st.error(f"🔴 **{tier_label}** — Your carbon footprint is high. Please review the recommendations below to reduce your environmental impact.")

    st.markdown("<p style='color:#2e7d32; font-weight:700; margin-bottom:4px;'>Eco Score Progress (0 = worst, 100 = best)</p>", unsafe_allow_html=True)
    st.progress(int(eco_score))

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
    st.subheader("🗂️ Your Profile Summary")
    st.markdown("<p style='color:#2e7d32;'>Here's how your choices mapped to numerical scores used in the prediction:</p>", unsafe_allow_html=True)

    summary_col1, summary_col2 = st.columns(2)
    with summary_col1:
        st.markdown(f"- ⛽ **Fuel Type:** `{fuel_label}` → Score: `{fuel_val}`")
        st.markdown(f"- 🚗 **Transport:** `{transport_label}` → Score: `{transport_val}`")
        st.markdown(f"- 🍽️ **Food Habit:** `{food_label}` → Score: `{food_val}`")
    with summary_col2:
        st.markdown(f"- 💡 **Electricity:** `{electricity_label}` → Score: `{electricity_val}`")
        st.markdown(f"- 🔥 **LPG Usage:** `{lpg_label}` → Score: `{lpg_val}`")
        st.markdown(f"- ✈️ **Travel Freq:** `{frequency_label}` → Score: `{frequency_val}`")

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
    st.subheader("💡 Personalised Sustainability Recommendations")
    st.markdown(
        "<p style='color:#2e7d32;'>Based on your specific inputs, here are targeted steps to reduce your carbon footprint:</p>",
        unsafe_allow_html=True
    )

    recommendations = get_recommendations(fuel_label, transport_label, food_label, electricity_label, lpg_label, frequency_label)

    for i, tip in enumerate(recommendations, 1):
        st.markdown(
            f"<div class='recommend-card'><strong>#{i}</strong> &nbsp; {tip}</div>",
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; color:#388e3c; font-size:0.85rem;'>"
        "🌍 Every small action counts. Together we can build a sustainable future.<br>"
        "Share your eco score and inspire others around you!"
        "</p>",
        unsafe_allow_html=True
    )

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#388e3c; font-size:0.8rem;'>"
    "🌱 AI-Powered Carbon Footprint Intelligence System &nbsp;|&nbsp; Built with Streamlit"
    "</p>",
    unsafe_allow_html=True
)
