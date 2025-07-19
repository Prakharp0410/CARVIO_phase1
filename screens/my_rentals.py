import streamlit as st
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from filehandling.rentals_io import *

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

my_rentals_title="""<h1 style='color:white; font-size:70px;
display:flex;
justify-content:center;
text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
margin-bottom: 25px;'>  MY RENTALS </h1>"""

max_width="""<style>
.stMainBlockContainer.block-container.st-emotion-cache-1w723zb.e4man114 {
    max-width: 100%;
}</style>"""

background_css="""<style>
section.stMain.st-emotion-cache-4rsbii.e4man111 {
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url(https://mobiag.com/wp-content/uploads/2019/06/car-rental-fleet.jpg);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    color: white;
}
</style>"""

button_css="""<style>
button.st-emotion-cache-1rwb540.el4r43z2{
    background: #2E86AB;
    color: white;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: bold;
    transition: all 0.1s ease;
}
button.st-emotion-cache-1rwb540.el4r43z2:hover {
    background: #ff9800;
    color: white;
    border: 2px solid #ff9800;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(255, 152, 0, 0.4);
}
</style>"""

def my_rentals_page_function():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    
    back_dashboard_button=st.button("← Back to Dashboard")
    if back_dashboard_button:                           #back to dashboard 
        st.session_state.page="home_page"
        st.session_state.current_page="none"
        st.rerun()
    
    st.markdown(my_rentals_title,unsafe_allow_html=True)
    st.markdown(max_width,unsafe_allow_html=True)
    st.markdown(background_css,unsafe_allow_html=True)
    st.markdown(button_css,unsafe_allow_html=True)

    current_rentals=show_user_current_rentals(st.session_state.username)
    past_rentals=show_user_past_rentals(st.session_state.username)

    current_rental_button=st.button(" Current/Ongoing Rentals")
    past_rentals_button=st.button(" Past Rentals")

    if current_rental_button:
        st.markdown("""<div style="background: rgba(76, 175, 80, 0.2); border-radius: 10px; 
                    padding: 15px; margin: 20px 0; border-left: 4px solid #4CAF50; text-align: center;">
                    <h1 style='color:white; margin:0;'> CURRENT RENTALS</h1></div>""", unsafe_allow_html=True)
        if len(current_rentals) == 0:
            st.markdown("""<div style="background: rgba(255, 152, 0, 0.1); border-radius: 10px; 
                        padding: 20px; margin: 20px 0; border: 2px solid #ff9800; text-align: center;">
                        <h2 style='color:white; margin:0;'> No current rentals found.</h2></div>""",
                        unsafe_allow_html=True)
        else:    
            for user in current_rentals:
                column1,column2,image=st.columns([2,2,1])
                with column1:
                    st.markdown(f"####  Car name: {user['car brand']} {user['car name']}")
                    st.markdown(f"####  Car no: {user['car no']}")
                    st.markdown(f"####  Amount: ₹{user['total_amount']:,}")
                with column2:
                    st.markdown(f"####  Start Date: {user['rental start']}")
                    st.markdown(f"####  End Date: {user['rental end']}")
                    st.markdown(f"#### Duration: {user['duration']} days")
                with image:
                    st.markdown( f"""
                            <div style="width:200px; height:150px;
                                    overflow:hidden; display:inline-block; 
                                    alige1msl4mp2n-items:center; justify-content:center; 
                                    background:rgba(255,255,255,0.1); border-radius:10px; 
                                    margin-bottom:8px; border:2px solid rgba(255,255,255,0.2);">
                                    <img src="{user['car_image']}" style="width:100%; height:100%; 
                                    object-fit:cover; border-radius:8px; justify-content:center;">
                            </div>
                            """,
                            unsafe_allow_html=True)
            
                st.markdown("""<style>
                    .stHorizontalBlock.st-emotion-cache-rra9ig.e1msl4mp2 {
                                            border-style: solid;
                                            border-color: rgba(255, 255, 255, 0.2);
                                            border-width: 1px;
                                            border-radius: 8px;
                                            }
                    .stColumn.st-emotion-cache-5ux0lt.e1msl4mp1 {
                        border-style: solid;
                        border-bottom: none;
                        border-left: none;
                        border-top: none;
                        border-color: rgba(255, 255, 255, 0.2);
                        padding-top: 20px;
                            }</style>"""  , unsafe_allow_html=True)  #car current rentals details containers
                
    if past_rentals_button:
            st.markdown("""<div style="background: rgba(255, 152, 0, 0.2); border-radius: 10px; 
                        padding: 15px; margin: 20px 0; border-left: 4px solid #ff9800; text-align: center;">
                        <h1 style='color:white; margin:0;'> PAST RENTALS</h1></div>""", unsafe_allow_html=True)
            if len(past_rentals) == 0:
                st.markdown("""<div style="background: rgba(255, 152, 0, 0.1); border-radius: 10px; 
                            padding: 20px; margin: 20px 0; border: 2px solid #ff9800; text-align: center;">
                            <h2 style='color:white; margin:0;'> No past rentals found.</h2></div>""", unsafe_allow_html=True)
            else:    
                for user in past_rentals:
                    st.markdown('<div class="rental-card">', unsafe_allow_html=True)
                    column1,column2,image=st.columns([2,2,1])
                    with column1:
                        st.markdown(f"####  Car name: {user['car brand']} {user['car name']}")
                        st.markdown(f"####  Car no: {user['car no']}")
                        st.markdown(f"####  Amount: ₹{user['total_amount']:,}")
                    with column2:
                        st.markdown(f"####  Start Date: {user['rental start']}")
                        st.markdown(f"####  End Date: {user['rental end']}")
                        st.markdown(f"####  Duration: {user['duration']} days")
                    with image:
                        st.markdown(f"""
                                <div style="width:200px; height:150px;
                                        overflow:hidden; display:inline-block; 
                                        align-items:center; justify-content:center; 
                                        background:rgba(255,255,255,0.1); border-radius:10px; 
                                        margin-bottom:8px; border:2px solid rgba(255,255,255,0.2);">
                                        <img src="{user['car_image']}" style="width:100%;
                                        height:100%; object-fit:cover; border-radius:8px;">
                                </div>""", unsafe_allow_html=True)
        
            st.markdown("""<style>
                    .stHorizontalBlock.st-emotion-cache-rra9ig.e1msl4mp2 {
    border-style: solid;
    border-color: rgba(255, 255, 255, 0.2);
    border-width: 1px;
    border-radius: 8px;
    margin-bottom: 20px;
}
                    .stColumn.st-emotion-cache-5ux0lt.e1msl4mp1{
                    border-style: solid;
                    border-bottom: none;
                    border-left: none;
                    border-top: none;
                    border-color: rgba(255, 255, 255, 0.2);
                    padding-top: 20px;
                    }
                    </style>""", unsafe_allow_html=True) #car past rentals containers