import streamlit as st

st.title("Tary Analytics 📊")
st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat")


st.header("Tary Researching")

col_prj1, col_prj2, col_prj3, col_prj4 = st.columns(4, gap="large")

with col_prj1:
    st.subheader("Youtube Tracker")
    st.caption("Lorem ipsum dolor sit amet, consectetur ")
with col_prj2:
    st.subheader("Second Project")
    st.caption("Lorem ipsum dolor sit amet, consectetur ")

with col_prj3:
    st.subheader("Third Project")
    st.caption("Lorem ipsum dolor sit amet, consectetur ")

with col_prj4:
    st.subheader("Fourth Project")
    st.caption("Lorem ipsum dolor sit amet, consectetur ")

st.divider()

col_mission, col_vision = st.columns(2, gap="large")

with col_mission:
    st.header("Our Mission")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.")

with col_vision:
    st.header("Our Vision")
    st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nSed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, \nquis nostrud exercitation ullamco laboris \nnisi ut aliquip ex ea commodo consequat")

st.divider()

st.title("Contact Us")
st.write("Need help or guidance with your Data Science project? Contact us!")

# Contact button
if st.button("Contact via Email"):
    st.write("Contacted")

