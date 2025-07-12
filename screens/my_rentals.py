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

my_rentals_title="""<h1 style='color:white; font-size:80px;
display:flex;
justify-content:center;'> MY RENTALS </h1>"""

max_width="""<style>
.stMainBlockContainer.block-container.st-emotion-cache-1w723zb.elbt1zu4 {
    max-width: 100%;
}</style>"""

background_css="""<style>
section.stMain.st-emotion-cache-z4kicb.elbt1zu1 {
        background-image:url(https://mobiag.com/wp-content/uploads/2019/06/car-rental-fleet.jpg);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    color: white;
}
</style>"""

button_css="""<style>
button.st-emotion-cache-1rwb540.e1e4lema2 {
    background: green;
}
button.st-emotion-cache-1rwb540.e1e4lema2:hover {
    background: red;
    color:white;
}
</style>"""
def my_rentals_page_function():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    
    back_dashboard_button=st.button("Back to dashboard")
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

    current_rental_button=st.button("Current/Ongoing Rentals")
    past_rentals_button=st.button("Past Rentals")

    if current_rental_button:
        st.markdown("<h1 style='color:white'>CURRENT RENTALS</h1>", unsafe_allow_html=True)
        if len(current_rentals) == 0:
            st.markdown("<h2 style='color:white'>No current rentals found.</h2>",
                        unsafe_allow_html=True)
        else:    
            for user in current_rentals:
                column1,column2,image=st.columns([2,2,1])
                with column1:
                    st.markdown(f"#### Car name:{user["car brand"]}  {user["car name"]}")
                    st.markdown(f"#### Car no:{user["car no"]}")
                    st.markdown(f"#### Amount : {user["total_amount"]}")
                with column2:
                    st.markdown(f"#### Start Date:{user["rental start"]}")
                    st.markdown(f"#### End Date:{user["rental end"]}")
                    st.markdown(f"#### Duration:{user["duration"]} days")
                with image:
                    st.markdown( f"""
                            <div style="width:200px; height:150px;
                                    overflow:hidden; display:inline-block; 
                                    align-items:center; justify-content:center; 
                                    background:#eee; border-radius:8px; margin-bottom:8px;">
                                    <img src="{user["car_image"]}" style="width:100%; height:100%; object-fit:cover;">
                            </div>
                            """,
                            unsafe_allow_html=True)
            
                st.markdown("""<style>
                    .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03 {
                                            border-style: solid;
                                            }
                    .stColumn.st-emotion-cache-1becg64.eertqu01 {
                        border-style: solid;
                        border-bottom: none;
                        border-left: none;
                        border-top: none;
                        padding-top: 20px;
                            }</style>"""  , unsafe_allow_html=True) 
                
    if past_rentals_button:
            st.markdown("<h1 style='color:white'>PAST RENTALS</h1>", unsafe_allow_html=True)
            if len(past_rentals) == 0:
                st.markdown("<h2 style='color:white'>No past rentals found.</h2>", unsafe_allow_html=True)
            else:    
                for user in past_rentals:
                    column1,column2,image=st.columns([2,2,1])
                    with column1:
                        st.markdown(f"#### Car name:{user["car brand"]}  {user["car name"]}")
                        st.markdown(f"#### Car no:{user["car no"]}")
                        st.markdown(f"#### Amount : {user["total_amount"]}")
                    with column2:
                        st.markdown(f"#### Start Date:{user["rental start"]}")
                        st.markdown(f"#### End Date:{user["rental end"]}")
                        st.markdown(f"#### Duration:{user["duration"]} days")
                    with image:
                        st.markdown(f"""
                                <div style="width:200px; height:150px;
                                        overflow:hidden; display:inline-block; 
                                        align-items:center; justify-content:center; 
                                        background:#eee; border-radius:8px; margin-bottom:8px;">
                                        <img src="{user["car_image"]}" style="width:100%;
                                        height:100%; object-fit:cover;">
                                </div>""", unsafe_allow_html=True)
        
            st.markdown("""<style>
                    .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03 {
    border-style: solid;
    margin-bottom: 20px;
}
                    .stColumn.st-emotion-cache-1becg64.eertqu01{
                    border-style: solid;
                    border-bottom: none;
                    border-left: none;
                    border-top: none;
                    padding-top: 20px;   s
                    }
                    </style>""", unsafe_allow_html=True)