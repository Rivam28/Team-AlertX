import streamlit as st
import pandas as pd
import folium
from streamlit.components.v1 import html
from datetime import datetime

# Page setup
st.set_page_config(layout="wide", page_title="AlertX Demo")
st.title("🌍 AlertX — Disaster Alert Billboard Simulator")

# Sidebar controls
st.sidebar.header("Simulation Controls")
lat = st.sidebar.slider("Village Latitude", 8.0, 37.0, 22.5)
lon = st.sidebar.slider("Village Longitude", 68.0, 97.0, 78.0)
rain = st.sidebar.slider("Rainfall (mm in last 3h)", 0, 300, 50)

# Risk calculation
def get_risk_color(mm):
    if mm < 20: return "green", "LOW"
    if mm < 100: return "orange", "MEDIUM"
    return "red", "HIGH"

color, level = get_risk_color(rain)

# Map with folium
m = folium.Map(location=[lat, lon], zoom_start=8)
folium.CircleMarker(
    location=[lat, lon],
    radius=30,
    color=color,
    fill=True,
    fill_opacity=0.7,
    popup=f"Rain: {rain} mm | Risk: {level}"
).add_to(m)
map_html = m._repr_html_()
html(map_html, height=400)

# Billboard simulator
st.markdown("### 📢 Digital Billboard Output")
safe_zone = "Community Hall, Village Center"
contacts = "Emergency Helpline: 101 / 112"
time_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

billboard_html = f"""
<div style="background:#111;color:white;padding:25px;border-radius:10px;text-align:center;">
  <h1 style="font-size:42px;margin:0;">ALERT LEVEL: {level}</h1>
  <p style="font-size:22px;margin:10px 0;">Rainfall Detected: {rain} mm</p>
  <p style="font-size:20px;margin:10px 0;">Safe Zone: <b>{safe_zone}</b></p>
  <p style="font-size:20px;margin:10px 0;">Contact: {contacts}</p>
  <p style="font-size:14px;margin-top:12px;color:#bbb;">Last Update: {time_str}</p>
</div>
"""
st.markdown(billboard_html, unsafe_allow_html=True)

