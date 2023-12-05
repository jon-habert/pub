import streamlit as st
from datetime import datetime, timedelta

# Initialize session_state
if 'mar_checkboxes' not in st.session_state:
    st.session_state.mar_checkboxes = {}
if 'jon_checkboxes' not in st.session_state:
    st.session_state.jon_checkboxes = {}

def display_calendar():
    st.title("Habert Daily Calendar")
    today = datetime.today()

    # Display day of the week, month, and day as the page header
    st.markdown(f"<h2 style='text-align: center;'>{today.strftime('%A, %b %d')}</h2>", unsafe_allow_html=True)
    st.write("")

    # Calculate hours from 7:00 am to 6:00 pm in half-hour intervals
    hours = [
        datetime(today.year, today.month, today.day, 7, 0) + timedelta(minutes=30 * i)
        for i in range(24)
        if 7 <= (datetime(today.year, today.month, today.day, 7, 0) + timedelta(minutes=30 * i)).hour < 18
    ]

    # Adjust width to fit more rows and add some padding
    st.markdown("<style>.st-dg {width: auto !important; padding: 5px;}</style>", unsafe_allow_html=True)

    # Display rows in a formatted table
    st.markdown("<style>.table {width: 100%;}</style>", unsafe_allow_html=True)
    st.write("<style>.row:hover {background-color: #f5f5f5;}</style>", unsafe_allow_html=True)

    # Display table headers with outlined columns
    st.markdown("""
        <style>
            .header {color: white; background-color: #333; font-weight: bold; padding: 8px; border: 1px solid #000;}
            .col1, .col2, .col3 {width: 33.33%; text-align: center; border: 1px solid #000; padding: 8px;}
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='header col1'>Time</div><div class='header col2'>Mar</div><div class='header col3'>Jon</div>", unsafe_allow_html=True)

    # Display rows with outlined columns
    for idx, hour in enumerate(hours):
        st.markdown("<div class='row'>", unsafe_allow_html=True)

        st.markdown(f"<div class='col1'>{hour.strftime('%I:%M %p')}</div>", unsafe_allow_html=True)

        mar_key = f'mar_input_{idx}'
        mar_input = st.checkbox(label='', key=mar_key, value=st.session_state.mar_checkboxes.get(mar_key, False))
        st.session_state.mar_checkboxes[mar_key] = mar_input
        st.markdown(f"<div class='col2'>{mar_input}</div>", unsafe_allow_html=True)

        jon_key = f'jon_input_{idx}'
        jon_input = st.checkbox(label='', key=jon_key, value=st.session_state.jon_checkboxes.get(jon_key, False))
        st.session_state.jon_checkboxes[jon_key] = jon_input
        st.markdown(f"<div class='col3'>{jon_input}</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    display_calendar()
