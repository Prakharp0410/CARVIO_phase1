import streamlit as st
from filehandling.user_io import *
import base64
def main_page_bl():

    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_background(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    set_background("D:/PROJECT/CARVIO_v1/static/image/bgimage_final.png")

    st.markdown("""
                <h1 style='color:white;'> Welcome to CARVIO </h1>
                <h2 style='color:white;'> Your car, Your pace, Your Savings </h2>
                <h3 style='color:white;'>Renting a car has never been this easier!!</h3>
            <style>
                section[data-testid="stVerticalBlock"]{
                justify-content:center;
                align-items:center;
                }
                </style>

                
                """,unsafe_allow_html=True)

    col1,col2=st.columns([1,1], gap="medium")

    with col1:
       signup_button=st.button("Sign up")

    with col2:
        login_button=st.button("Log in")
    
    
    if signup_button:
        st.session_state.page="signup"
        st.rerun()
  
    if login_button:
        st.session_state.page="login"
        st.rerun()

