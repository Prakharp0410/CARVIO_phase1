import streamlit as st
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from screens.sessionstate_folder.session_state import *
from filehandling.cars_io import update_cars
from filehandling.rentals_io import add_rentals

background_image="""<style>
                    .stMainBlockContainer.block-container.st-emotion-cache-1w723zb.elbt1zu4 {
        background-image:url(https://mobiag.com/wp-content/uploads/2019/06/car-rental-fleet.jpg);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
}
</style>
"""

font_style="""
<style>
.stColumn.st-emotion-cache-1becg64.eertqu01 {
    color: white;
}
.stMainBlockContainer.block-container.st-emotion-cache-1w723zb.elbt1zu4 {
    color: white;
}

</style>"""

button_css="""<style>
button.st-emotion-cache-1rwb540.e1e4lema2 {
    background-color: green;
    color: white;
    }
    </style>"""

def billing_page_function():

    st.markdown(background_image, unsafe_allow_html=True)  #background image
    st.markdown(font_style, unsafe_allow_html=True)        #font style
    st.markdown(button_css, unsafe_allow_html=True)         #button css

    back_dashboard_button=st.button("Back to dashboard")   #back to dashboard button
    if back_dashboard_button:
       st.session_state.page="home_page"
       st.session_state.current_page="none"
       st.rerun()

    if(st.session_state.car_brand=="none"):                 #if no car is selected
            st.markdown("# PLEASE SELECT A CAR FROM RENT A CAR PAGE")
    else:        
        st.markdown("<h1 style='color:white'>YOUR BILLING DETAILS ARE GIVEN BELOW</h1>",
                    unsafe_allow_html=True)
        col1,col2,col3=st.columns([2,2,1])
        with col1:
            st.markdown(f"<h2 style='font-family:Roboto'>{st.session_state.car_brand}  {st.session_state.car_name}</h2>",
                        unsafe_allow_html=True)
            st.markdown(f"**Car No**: {st.session_state.car_no}")
            st.markdown(f"**Type**: {st.session_state.car_type}")
            st.markdown(f"**Start Date**: {st.session_state.start_date}")
            st.markdown(f"**End Date**: {st.session_state.end_date}")
        with col2:       
                        st.markdown("<br><br>", unsafe_allow_html=True)             
                        st.markdown(f"**Color**: {st.session_state.car_color}")
                        st.markdown(f"**Rate per day**: ₹{st.session_state.rate}")
                        st.markdown(f"**Fuel Type**: {st.session_state.car_fuel_type}")
                        st.markdown(f"**Duration**: {st.session_state.duration}")
        with col3:
                st.markdown( f"""
                        <div style="width:200px; height:200px;
                                overflow:hidden; display:flex; 
                                align-items:center; justify-content:center; 
                                background:#eee; border-radius:8px; margin-bottom:8px;">
                                <img src="{st.session_state.car_image}" style="width:100%; height:100%; object-fit:cover;">
                        </div>
                        """,
                        unsafe_allow_html=True,)
        price_without_discount=(st.session_state.rate)*(st.session_state.duration)
        Invoice_col1,Invoice_col2=st.columns([2,1])
        discount=0
        with Invoice_col1:
            st.markdown("## The Total Price is: ",unsafe_allow_html=True)
            st.markdown("## Discount ",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("# Net Amount Payable:", unsafe_allow_html=True)
        with Invoice_col2:
            st.markdown(f"## {price_without_discount}")  
            if(30>st.session_state.duration>=7):
                discount=0.1*(price_without_discount)
            elif(st.session_state.duration>=30):
                discount=0.2*(price_without_discount)
            else:
                discount=0
            st.markdown(f"## {discount}", unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown(f"# {price_without_discount-discount}", unsafe_allow_html=True)
            st.session_state.total_amount=price_without_discount-discount
        button1,pay_button=st.columns([7,1])
        with pay_button:
              payment_button=st.button("PAY")
              if payment_button:
                    update_cars(st.session_state.car_name, st.session_state.car_no, False) #update car_availability
                    add_rentals(st.session_state.username, st.session_state.car_name, #add to the rentals.json
                                st.session_state.car_brand, st.session_state.car_no,
                                st.session_state.start_date,st.session_state.end_date,
                                st.session_state.duration, False, st.session_state.total_amount,
                                st.session_state.car_image)
                    st.success("PAYMENT SUCCESSFUL!!!")
              
