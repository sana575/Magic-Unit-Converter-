import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

# Load animations
lottie_header = load_lottieurl("https://lottie.host/44247b50-3d28-4933-a3d5-c93a6663f4e5/F4zUqJHbKB.json")
lottie_currency = load_lottieurl("https://lottie.host/14162949-c393-4329-a5b3-3871e104cc34/GqPgxrVd7D.json")
lottie_length = load_lottieurl("https://lottie.host/7468410c-0b17-4e9a-a50f-b65a94a0d503/1Fl23WYj8i.json")
lottie_weight = load_lottieurl("https://lottie.host/ea4a3566-6bd5-422e-9aa6-5d70d35422bf/ZvTQdl0HA7.json")
lottie_temperature = load_lottieurl("https://lottie.host/dcc10d02-7119-484c-9358-e04acf4b5fb2/tJOx84AiVJ.json")
lottie_success = load_lottieurl("https://lottie.host/0d2693c8-1d74-43af-9390-cb796aab11c8/Ir474aaP1c.json")

# Page configuration
st.set_page_config(
    page_title="🌈 Magic Unit Converter 🌈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Responsive theme styling
st.markdown("""
<style>
    /* Base styling for both themes */
    .stButton > button {
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 7px 14px rgba(0, 0, 0, 0.15);
    }
    
    .stButton > button:active {
        transform: translateY(1px);
    }
    
    .convert-button {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input,
    .stSelectbox > div > div {
        border-radius: 6px;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus,
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div:focus {
        transform: scale(1.02);
    }
    
    a {
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-out forwards;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    .result-container {
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        transition: all 0.5s ease;
    }
    
    /* Light Theme Styling */
    [data-theme="light"] [data-testid="stAppViewContainer"],
    [data-theme="light"] [data-testid="stHeader"] {
        background: linear-gradient(135deg, #f5f7fa, #e4e8f0);
    }
    
    [data-theme="light"] [data-testid="stSidebar"] {
        background: #f0f2f6;
        border-right: 1px solid #4361ee;
        box-shadow: 2px 0 10px rgba(0, 0, 0, 0.05);
    }
    
    [data-theme="light"] .stButton > button {
        background: linear-gradient(135deg, #4361ee, #3046eb);
        color: #ffffff;
        border: none;
    }
    
    [data-theme="light"] .stButton > button:hover {
        background: linear-gradient(135deg, #3046eb, #2034d6);
    }
    
    [data-theme="light"] .stNumberInput > div > div > input,
    [data-theme="light"] .stTextInput > div > div > input {
        background-color: #ffffff !important;
        color: #262730 !important;
        border: 1px solid #4361ee !important;
    }
    
    [data-theme="light"] .stSelectbox > div > div {
        background-color: #ffffff !important;
        color: #262730 !important;
        border: 1px solid #4361ee !important;
    }
    
    [data-theme="light"] .stSuccess {
        background-color: rgba(67, 97, 238, 0.1);
        border: 1px solid #4361ee;
        color: #262730;
    }
    
    [data-theme="light"] h1, 
    [data-theme="light"] h2, 
    [data-theme="light"] h3, 
    [data-theme="light"] h4, 
    [data-theme="light"] h5, 
    [data-theme="light"] h6 {
        color: #262730 !important;
    }
    
    [data-theme="light"] p, 
    [data-theme="light"] label, 
    [data-theme="light"] .stMarkdown {
        color: #262730 !important;
    }
    
    [data-theme="light"] .stSlider > div > div {
        background-color: #4361ee !important;
    }
    
    [data-theme="light"] a {
        color: #4361ee !important;
    }
    
    [data-theme="light"] .element-container .stMarkdown {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #4361ee;
        margin: 5px 0;
    }
    
    [data-theme="light"] .result-container {
        background-color: #e8f0fe;
        border: 1px solid #4361ee;
    }
    
    /* Dark Theme Styling */
    [data-theme="dark"] [data-testid="stAppViewContainer"],
    [data-theme="dark"] [data-testid="stHeader"] {
        background: linear-gradient(135deg, #0e1117, #1b1f27);
    }
    
    [data-theme="dark"] [data-testid="stSidebar"] {
        background: #262730;
        border-right: 1px solid #4361ee;
        box-shadow: 2px 0 10px rgba(0, 0, 0, 0.2);
    }
    
    [data-theme="dark"] .stButton > button {
        background: linear-gradient(135deg, #4361ee, #3046eb);
        color: #ffffff;
        border: none;
    }
    
    [data-theme="dark"] .stButton > button:hover {
        background: linear-gradient(135deg, #3046eb, #2034d6);
    }
    
    [data-theme="dark"] .stNumberInput > div > div > input,
    [data-theme="dark"] .stTextInput > div > div > input {
        background-color: #262730 !important;
        color: #ffffff !important;
        border: 1px solid #4361ee !important;
    }
    
    [data-theme="dark"] .stSelectbox > div > div {
        background-color: #262730 !important;
        color: #ffffff !important;
        border: 1px solid #4361ee !important;
    }
    
    [data-theme="dark"] .stSuccess {
        background-color: rgba(67, 97, 238, 0.2);
        border: 1px solid #4361ee;
        color: #ffffff;
    }
    
    [data-theme="dark"] h1, 
    [data-theme="dark"] h2, 
    [data-theme="dark"] h3, 
    [data-theme="dark"] h4, 
    [data-theme="dark"] h5, 
    [data-theme="dark"] h6 {
        color: #ffffff !important;
    }
    
    [data-theme="dark"] p, 
    [data-theme="dark"] label, 
    [data-theme="dark"] .stMarkdown {
        color: #fafafa !important;
    }
    
    [data-theme="dark"] .stSlider > div > div {
        background-color: #4361ee !important;
    }
    
    [data-theme="dark"] a {
        color: #4361ee !important;
    }
    
    [data-theme="dark"] .element-container .stMarkdown {
        background-color: #262730;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #4361ee;
        margin: 5px 0;
    }
    
    [data-theme="dark"] .result-container {
        background-color: #1e2130;
        border: 1px solid #4361ee;
    }
    
    /* History and favorites items */
    .stInfo, .stSuccess {
        border-radius: 8px;
        margin: 5px 0;
        padding: 10px;
        transition: all 0.3s ease;
    }
    
    .stInfo:hover, .stSuccess:hover {
        transform: translateX(5px);
    }
    
    /* Common card styling */
    .card {
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    [data-theme="light"] .card {
        background: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    [data-theme="dark"] .card {
        background: #262730;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 5px 5px 0 0;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #4361ee !important;
        color: white !important;
    }
    
    /* Loading animation */
    @keyframes loading {
        0% { width: 0%; }
        100% { width: 100%; }
    }
    
    .loading-bar {
        height: 4px;
        background: linear-gradient(90deg, #4361ee, #2034d6);
        border-radius: 2px;
        margin: 10px 0;
        animation: loading 1s ease-in-out;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []
if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "result" not in st.session_state:
    st.session_state.result = None
if "from_value" not in st.session_state:
    st.session_state.from_value = None
if "to_value" not in st.session_state:
    st.session_state.to_value = None
if "last_conversion" not in st.session_state:
    st.session_state.last_conversion = None

# Function to perform conversion and show animation
def perform_conversion():
    # Show loading animation
    st.session_state.show_result = True
    with st.spinner("Converting..."):
        # Create a loading bar effect
        progress_placeholder = st.empty()
        progress_placeholder.markdown('<div class="loading-bar"></div>', unsafe_allow_html=True)
        time.sleep(0.5)  # Short delay for effect
        progress_placeholder.empty()

# Main Header with animation
st.markdown("<h1 style='text-align: center;' class='fade-in'> 🌈 Magic Unit Converter 🌈</h1>", unsafe_allow_html=True)
if lottie_header:
    st_lottie(lottie_header, height=200, key="header_animation")

st.markdown("""
<p style='text-align: center; font-size: 1.2em; margin-bottom: 30px;' class='fade-in'>
    Your go-to tool for quick and accurate unit conversions
</p>
""", unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.markdown("<h2 class='pulse'>⚙️ Settings & Tools</h2>", unsafe_allow_html=True)

# Precision Settings
decimal_places = st.sidebar.slider(
    "🎯 Decimal Precision",
    0, 5, 2,
    help="Set the number of decimal places for results"
)

# Auto Convert Toggle
auto_convert = st.sidebar.checkbox(
    "🔄 Auto Convert",
    value=True,
    help="Convert values automatically as you type"
)

# Main Conversion Interface
st.markdown("<div class='card fade-in'>", unsafe_allow_html=True)
conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Weight", "Temperature", "Currency"]
)
st.markdown("</div>", unsafe_allow_html=True)

# Conversion Logic
st.markdown("<div class='card fade-in'>", unsafe_allow_html=True)
if conversion_type == "Length":
    st.header("📏 Length Converter")
    if lottie_length:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_lottie(lottie_length, height=150, key="length_animation")
    
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Miles"]
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From", length_units, key="length_from")
    with col2:
        to_unit = st.selectbox("To", length_units, key="length_to")
    
    value = st.number_input("Enter Value", min_value=0.0, format=f"%.{decimal_places}f")
    
    length_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Miles": 0.000621371
    }
    
    # Always show Convert button
    convert_clicked = st.button("Convert Units", key="convert_length")
    
    if auto_convert or convert_clicked:
        perform_conversion()
        result = value * (length_factors[to_unit] / length_factors[from_unit])
        conversion_text = f"{value} {from_unit} = {result:.{decimal_places}f} {to_unit}"
        st.session_state.result = result
        st.session_state.from_value = value
        st.session_state.to_value = to_unit
        st.session_state.last_conversion = conversion_text
        
        if conversion_text not in st.session_state.history:
            st.session_state.history.append(conversion_text)

elif conversion_type == "Weight":
    st.header("⚖️ Weight Converter")
    if lottie_weight:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_lottie(lottie_weight, height=150, key="weight_animation")
    
    weight_units = ["Grams", "Kilograms", "Pounds", "Ounces"]
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From", weight_units, key="weight_from")
    with col2:
        to_unit = st.selectbox("To", weight_units, key="weight_to")
    
    value = st.number_input("Enter Value", min_value=0.0, format=f"%.{decimal_places}f")
    
    weight_factors = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Pounds": 0.00220462,
        "Ounces": 0.035274
    }
    
    # Always show Convert button
    convert_clicked = st.button("Convert Units", key="convert_weight")
    
    if auto_convert or convert_clicked:
        perform_conversion()
        result = value * (weight_factors[to_unit] / weight_factors[from_unit])
        conversion_text = f"{value} {from_unit} = {result:.{decimal_places}f} {to_unit}"
        st.session_state.result = result
        st.session_state.from_value = value
        st.session_state.to_value = to_unit
        st.session_state.last_conversion = conversion_text
        
        if conversion_text not in st.session_state.history:
            st.session_state.history.append(conversion_text)

elif conversion_type == "Temperature":
    st.header("🌡️ Temperature Converter")
    if lottie_temperature:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_lottie(lottie_temperature, height=150, key="temp_animation")
    
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From", temp_units, key="temp_from")
    with col2:
        to_unit = st.selectbox("To", temp_units, key="temp_to")
    
    value = st.number_input("Enter Value", format=f"%.{decimal_places}f")
    
    # Always show Convert button
    convert_clicked = st.button("Convert Units", key="convert_temp")
    
    if auto_convert or convert_clicked:
        perform_conversion()
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif to_unit == "Kelvin":
                result = value + 273.15
            else:
                result = value
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            else:
                result = value
        else:  # Kelvin
            if to_unit == "Celsius":
                result = value - 273.15
            elif to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
                
        conversion_text = f"{value} {from_unit} = {result:.{decimal_places}f} {to_unit}"
        st.session_state.result = result
        st.session_state.from_value = value
        st.session_state.to_value = to_unit
        st.session_state.last_conversion = conversion_text
        
        if conversion_text not in st.session_state.history:
            st.session_state.history.append(conversion_text)

elif conversion_type == "Currency":
    st.header("💱 Currency Converter")
    if lottie_currency:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_lottie(lottie_currency, height=150, key="currency_animation")
    
    currencies = ["USD", "EUR", "GBP", "INR", "PKR"]
    col1, col2 = st.columns(2)
    
    with col1:
        from_currency = st.selectbox("From", currencies, key="currency_from")
    with col2:
        to_currency = st.selectbox("To", currencies, key="currency_to")
    
    value = st.number_input("Enter Amount", min_value=0.0, format=f"%.{decimal_places}f")
    
    currency_rates = {
        "USD": 1,
        "EUR": 0.85,
        "GBP": 0.75,
        "INR": 75,
        "PKR": 250
    }
    
    # Always show Convert button
    convert_clicked = st.button("Convert Currency", key="convert_currency")
    
    if auto_convert or convert_clicked:
        perform_conversion()
        result = value * (currency_rates[to_currency] / currency_rates[from_currency])
        conversion_text = f"{value} {from_currency} = {result:.{decimal_places}f} {to_currency}"
        st.session_state.result = result
        st.session_state.from_value = value
        st.session_state.to_value = to_currency
        st.session_state.last_conversion = conversion_text
        
        if conversion_text not in st.session_state.history:
            st.session_state.history.append(conversion_text)

# Display result with animation
if st.session_state.show_result and st.session_state.last_conversion:
    st.markdown("<div class='result-container fade-in'>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    with col1:
        st.success(f"✅ {st.session_state.last_conversion}")
    with col2:
        if lottie_success:
            st_lottie(lottie_success, height=80, key="success_animation")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Quick Conversion Tabs
st.markdown("<div class='card fade-in'>", unsafe_allow_html=True)
st.subheader("🚀 Quick Conversions")
tabs = st.tabs(["Common Length", "Common Weight", "Common Temperature"])

with tabs[0]:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("1 Meter to Feet"):
            result = 1 * 3.28084
            st.info(f"1 Meter = {result:.{decimal_places}f} Feet")
    with col2:
        if st.button("1 Kilometer to Miles"):
            result = 1 * 0.621371
            st.info(f"1 Kilometer = {result:.{decimal_places}f} Miles")
    with col3:
        if st.button("1 Inch to Centimeters"):
            result = 1 * 2.54
            st.info(f"1 Inch = {result:.{decimal_places}f} Centimeters")

with tabs[1]:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("1 Kilogram to Pounds"):
            result = 1 * 2.20462
            st.info(f"1 Kilogram = {result:.{decimal_places}f} Pounds")
    with col2:
        if st.button("1 Pound to Grams"):
            result = 1 * 453.592
            st.info(f"1 Pound = {result:.{decimal_places}f} Grams")
    with col3:
        if st.button("1 Ounce to Grams"):
            result = 1 * 28.3495
            st.info(f"1 Ounce = {result:.{decimal_places}f} Grams")

with tabs[2]:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("0°C to Fahrenheit"):
            result = (0 * 9/5) + 32
            st.info(f"0°C = {result:.{decimal_places}f}°F")
    with col2:
        if st.button("100°F to Celsius"):
            result = (100 - 32) * 5/9
            st.info(f"100°F = {result:.{decimal_places}f}°C")
    with col3:
        if st.button("Room Temp (72°F) to Celsius"):
            result = (72 - 32) * 5/9
            st.info(f"72°F = {result:.{decimal_places}f}°C")

st.markdown("</div>", unsafe_allow_html=True)

# History Section
st.sidebar.markdown("---")
st.sidebar.markdown("<h3 class='fade-in'>📜 Recent Conversions</h3>", unsafe_allow_html=True)
if st.session_state.history:
    for entry in reversed(st.session_state.history[-5:]):
        st.sidebar.info(entry)
else:
    st.sidebar.markdown("<p style='opacity: 0.7;'>No conversions yet</p>", unsafe_allow_html=True)

# Favorites Section
st.sidebar.markdown("---")
st.sidebar.markdown("<h3 class='fade-in'>⭐ Favorites</h3>", unsafe_allow_html=True)

save_favorite = st.sidebar.button("Save Current Conversion", key="save_favorite")
if save_favorite:
    if st.session_state.history and st.session_state.last_conversion:
        if st.session_state.last_conversion not in st.session_state.favorites:
            st.session_state.favorites.append(st.session_state.last_conversion)
            st.sidebar.success("Saved to favorites!")
        else:
            st.sidebar.warning("Already in favorites!")

if st.session_state.favorites:
    for fav in st.session_state.favorites:
        st.sidebar.success(fav)
else:
    st.sidebar.markdown("<p style='opacity: 0.7;'>No favorites saved</p>", unsafe_allow_html=True)

# Theme detection notice
st.sidebar.markdown("---")
st.sidebar.info("🎨 This app supports both light and dark themes. Change your Streamlit theme in settings.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;' class='fade-in'>
    <h4>Built with ❤️ by Sana</h4>
    <p>Using <a href='https://streamlit.io/' target='_blank'>Streamlit</a> 
    for a dynamic user experience</p>
    <div class="pulse" style="display: inline-block;">
        <p style='font-size: 0.8em; opacity: 0.7;'>Version 3.0 | Last Updated: February 2025</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Add confetti effect for first conversion
if 'first_conversion' not in st.session_state:
    st.session_state.first_conversion = False
    
if st.session_state.history and not st.session_state.first_conversion:
    st.balloons()
    st.session_state.first_conversion = True