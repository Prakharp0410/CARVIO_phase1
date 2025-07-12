import streamlit as st
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from filehandling.rentals_io import *
from filehandling.reviews_io import *
from filehandling.cars_io import *


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

background_styling="""<style>
.stMainBlockContainer.block-container.st-emotion-cache-1w723zb.elbt1zu4 {
    max-width: 100%;
    background-image:url(https://mobiag.com/wp-content/uploads/2019/06/car-rental-fleet.jpg);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    color:white;
}        </style>"""

border_styling="""
<style>
.stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03 {
    margin-bottom: 50px;
    margin-top: 20px;
    border: 1px;
    border-style: solid;
    border-radius: 10px;
    padding-right: 20px;
    padding-left: 20px;
}
.stColumn.st-emotion-cache-195cadd.eertqu01 {
    border-style: solid;
    border-bottom: none;
    border-left: none;
    border-top: none;
    padding-bottom: 20px;
}
</style>"""

button_css="""  <style>
            .stButton.st-emotion-cache-8atqhb.e1mlolmg0 {
    display: flex;
    justify-content: center;
    margin-top: 20px;
                }
              button.st-emotion-cache-1rwb540.e1e4lema2 {
    background: red;
                }  </style>"""

text_input_css="""<style>
p {
    color: white;
}
</style>
"""

def return_and_review_page():
    st.markdown(remove_header_footer, unsafe_allow_html=True)  #removes header and footer
    st.markdown(background_styling, unsafe_allow_html=True)    #background css
    st.markdown(border_styling, unsafe_allow_html=True)        #border css
    st.markdown(button_css, unsafe_allow_html=True)            #button css
    st.markdown(text_input_css, unsafe_allow_html=True)        #text field heading css
    
    ongoing_rentals=show_user_current_rentals(st.session_state.username)  #fetching ongoing rentals of the user
    if(len(ongoing_rentals)==0):
        st.markdown("# NO ONGOING RENTALS HERE",unsafe_allow_html=True)
        st.markdown(remove_header_footer,unsafe_allow_html=True)
        back_dashboard_button=st.button("Back to dashboard")  #back to dashboard button
        if back_dashboard_button:                        
            st.session_state.page="home_page"
            st.session_state.current_page="none"
            st.rerun()   #if no ongoing rentals
    
    else:
        st.markdown("## Select the car you want to return")
        for user in ongoing_rentals:
            checked=False
            checkbox,detail1,detail2,image=st.columns([0.5,2,2,1])
            with checkbox:
                checked=st.checkbox("Select", key=user["car no"])
            with detail1:
                st.markdown(f" ### Car Name:{user["car brand"]} {user["car name"]}")
                st.markdown(f" ### Car No. :{user["car no"]}")
                st.markdown(f"### Amount Paid:{user["total_amount"]}")
            with detail2:
                st.markdown(f"### Start date:{user["rental start"]}") 
                st.markdown(f"### End date:{user["rental end"]}") 
                return_button=st.button("Return this car", key=user["car name"])
            if checked:
                review_text=st.text_area("Enter the review of this car:", key=user["total_amount"])
                rating_value=st.slider("Enter the rating",0,5,3, key=user["car brand"])
            with image:
                st.markdown( f"""
                            <div style="width:200px; height:200px;
                                    overflow:hidden; display:flex; 
                                    align-items:center; justify-content:center; 
                                    background:#eee; border-radius:8px; margin-bottom:8px;">
                                    <img src="{user["car_image"]}" style="width:100%; height:100%; object-fit:cover;">
                            </div>
                            """,
                            unsafe_allow_html=True,)
            if return_button:
                add_review(user["username"], user["car name"], user["car brand"],user["rental start"],
                           user["rental end"], review_text,rating_value)
                mark_returned(user["username"], user["car no"], True)
                update_cars(user["car name"],user["car no"], True)    #marking the car as available
                st.success("Successfully returned this car")
                st.session_state.page="home_page"
                st.session_state.current_page="none"
                st.rerun()  #to refresh the page and show updated rentals




    