import streamlit as st
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from screens.sessionstate_folder.session_state import *
from filehandling.cars_io import update_cars
from filehandling.rentals_io import add_rentals

background_image="""<style>
                    .stMainBlockContainer.block-container.st-emotion-cache-1w723zb.e4man114{
                    max-width: 100%;
                    }
                    section.stMain.st-emotion-cache-4rsbii.e4man111{
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url(https://mobiag.com/wp-content/uploads/2019/06/car-rental-fleet.jpg);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
}
</style>
"""

font_style="""
<style>
.stMainBlockContainer.block-container.st-emotion-cache-1w723zb.e4man114 {
    color: white;
}
.price-row {
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    padding: 5px 0;
}
.total-amount {
    background: linear-gradient(45deg, #4CAF50, #45a049);
    color: white;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
    margin-top: 10px;
}
</style>"""

button_css="""<style>
button.st-emotion-cache-1rwb540.el4r43z2 {
    background: #2E86AB;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
}
button.st-emotion-cache-1rwb540.el4r43z2:hover {
    background: orange;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4);
}
</style>"""

def billing_page_function():

    st.markdown(background_image, unsafe_allow_html=True)  #background image
    
    back_dashboard_button=st.button("← Back to Dashboard")   #back to dashboard button
    if back_dashboard_button:
       st.session_state.page="home_page"
       st.session_state.current_page="none"
       st.rerun()
    
    st.markdown(font_style, unsafe_allow_html=True)        #font style
    st.markdown(button_css, unsafe_allow_html=True)        #button css


    if(st.session_state.car_brand=="none"):                 #if no car is selected
            st.markdown("""
            <div style="background: rgba(255, 0, 0, 0.1); border-radius: 10px; padding: 20px; 
                       text-align: center; border: 2px solid #ff4444; margin: 20px 0;">
                <h1 style='color: #ff6b6b; margin: 0;'> PLEASE SELECT A CAR FROM RENT A CAR PAGE</h1>
            </div>
            """, unsafe_allow_html=True)
    else:        
        st.markdown("<h1 style='color:white; text-align:center; margin-bottom:30px;'> YOUR BILLING DETAILS ARE GIVEN BELOW</h1>",
                    unsafe_allow_html=True)
        
        col1,col2,col3=st.columns([2,2,1])
        
        with col1:
            st.markdown('<div class="car-info">', unsafe_allow_html=True)
            st.markdown(f"<h2 style='font-family:Roboto; color:#4CAF50; margin-bottom:15px;'>🚗 {st.session_state.car_brand} {st.session_state.car_name}</h2>",
                        unsafe_allow_html=True)
            st.markdown(f"Car No: {st.session_state.car_no}")
            st.markdown(f"Type: {st.session_state.car_type}")
            st.markdown(f"Start Date: {st.session_state.start_date}")
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown(f" End Date: {st.session_state.end_date}")
            
        with col2:       
            st.markdown('<div class="car-info">', unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)             
            st.markdown(f" Color: {st.session_state.car_color}")
            st.markdown(f" Rate per day: ₹{st.session_state.rate:,}")
            st.markdown(f" Fuel Type: {st.session_state.car_fuel_type}")
            st.markdown(f" Duration: {st.session_state.duration} days")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col3:
                st.markdown( f"""
                        <div style="width:200px; height:200px;
                                overflow:hidden; display:flex; 
                                align-items:center; justify-content:center; 
                                background:rgba(255,255,255,0.1); border-radius:10px; 
                                margin-bottom:8px; border:2px solid rgba(255,255,255,0.2);">
                                <img src="{st.session_state.car_image}" style="width:100%; height:100%; object-fit:cover; border-radius:8px;">
                        </div>
                        """,
                        unsafe_allow_html=True,)
        st.markdown('</div>', unsafe_allow_html=True)
        
        price_without_discount=(st.session_state.rate)*(st.session_state.duration)
        
        st.markdown("<h2 style='color:#4CAF50; text-align:center; margin-bottom:20px;'> PAYMENT SUMMARY</h2>", unsafe_allow_html=True)
        
        Invoice_col1,Invoice_col2=st.columns([2,1])
        discount=0
        
        with Invoice_col1:
            st.markdown('<div class="price-row">', unsafe_allow_html=True)
            st.markdown("##  Total Price:", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="price-row">', unsafe_allow_html=True)
            st.markdown("## Discount:", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("#  Net Amount Payable:", unsafe_allow_html=True)
            
        with Invoice_col2:
            st.markdown('<div class="price-row">', unsafe_allow_html=True)
            st.markdown(f"## ₹{price_without_discount:,}")  
            st.markdown('</div>', unsafe_allow_html=True)
            
            if(30>st.session_state.duration>=7):
                discount=0.1*(price_without_discount)
                discount_text = "10% (Weekly Discount)"
            elif(st.session_state.duration>=30):
                discount=0.2*(price_without_discount)
                discount_text = "20% (Monthly Discount)"
            else:
                discount=0
                discount_text = "No Discount"
                
            st.markdown('<div class="price-row">', unsafe_allow_html=True)
            if discount > 0:
                st.markdown(f"## -₹{discount:,.0f}")
                st.markdown(f"<small style='color:#ff9800;'>{discount_text}</small>", unsafe_allow_html=True)
            else:
                st.markdown(f"## ₹{discount}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("<br>",unsafe_allow_html=True)
            final_amount = price_without_discount - discount
            st.markdown(f'<div class="total-amount"><h1 style="margin:0;">₹{final_amount:,.0f}</h1></div>', unsafe_allow_html=True)
            st.session_state.total_amount = final_amount
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        button1,pay_button=st.columns([7,1])
        with pay_button:
              payment_button=st.button(" PAY NOW")
              if payment_button:
                    update_cars(st.session_state.car_name, st.session_state.car_no, False) #update car_availability
                    add_rentals(st.session_state.rental_id,st.session_state.username,st.session_state.car_name,          #add to the rentals.json
                                st.session_state.car_brand, st.session_state.car_no,
                                st.session_state.start_date,st.session_state.end_date,
                                st.session_state.duration, False, st.session_state.total_amount,
                                st.session_state.car_image)
                    st.session_state.rental_id += 1   #increment rental_id for next rental
                    st.success(" PAYMENT SUCCESSFUL!!!")
                    st.balloons()