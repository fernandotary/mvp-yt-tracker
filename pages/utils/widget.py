import streamlit as st
from datetime import datetime
from datetime import date


# Channel


def get_channel_input():
    channel_name = st.selectbox(
        'Which channel do you want to search?',
        ['Teleamazonas', 'Ecuavisa', 'TC Televisión', 'Café la Posta', 'BN Periodismo'])
    return channel_name


# Date
def get_date_input():
    d_col1, d_col2 = st.columns(2)
    with d_col1:
        st_begin_date = st.date_input(
            "Select a start date", min_value=date(2024, 1, 5))
    with d_col2:
        st_finish_date = st.date_input(
            "Select an end date")

    begin_date, finish_date = format_dates(st_begin_date, st_finish_date)

    return begin_date, finish_date


def format_dates(st_begin_date, st_finish_date):
    if st_begin_date and st_finish_date:
        begin_date = datetime.combine(
            st_begin_date, datetime.min.time()).strftime("%Y-%m-%dT%H:%M:%SZ")
        finish_date = datetime.combine(
            st_finish_date, datetime.min.time()).strftime("%Y-%m-%dT%H:%M:%SZ")
    return begin_date, finish_date
