import pandas as pd
import streamlit as st
import plotly.express as px

# Setting page configuration
st.set_page_config(
    page_title="Global Superstore",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

# Customized CSS inorder to style the dashboard
st.markdown(
    """
    <style>
