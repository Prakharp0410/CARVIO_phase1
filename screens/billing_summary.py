import streamlit as st
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from screens.sessionstate_folder.session_state import *
from utils.billing import billing_page_function
# from filehandling.rentals_io import save_rentals,delete_rentals

#here I have rate,duration,car nae,car brand, fuel type and car tye in session state

remove_header_footer = """  
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Hide the orange loading progress bar */
        div[data-testid="stDecoration"] {
            display: none !important;
        }

        /* Remove top padding to avoid white space */
        .block-container {
            padding-top: 0rem !important;
        }
    </style>
"""
def billing_page():
    st.markdown(remove_header_footer, unsafe_allow_html=True)
    billing_page_function()                               #billing page from utils.billing



