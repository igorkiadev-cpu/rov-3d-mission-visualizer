import streamlit as st
import pandas as pd
import plotly.express as px

st.title("ROV 3D Mission Path Visualizer")

st.write("Interactive 3D visualization of ROV trajectory during mission.")

data = pd.read_csv("data/mission_path.csv")

fig = px.line_3d(
    data,
    x="x",
    y="y",
    z="depth",
    title="ROV Mission Trajectory"
)

st.plotly_chart(fig)
