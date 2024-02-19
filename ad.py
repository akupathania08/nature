import streamlit as st
st.title("COLLEGE ADMISSION")
percentage=st.number_input("enter your percentage")
st.button("check your eligibility")
if percentage>70:
    st.success(f"congratulations!,you are eligible with {percentage}%.")
    st.balloons()    
else:
    st.error(f"sorry , you are not eligible with {percentage}%.")     