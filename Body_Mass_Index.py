"""BMI = (weight in kilograms) / (height in inches)^2 x 703"""
import streamlit as st

st.title('Body Mass Index Calculator')

NAME = st.text_input("Enter your Name:-")
weight = st.number_input("Enter your Weight  in (kg) :- ", 10, 200)
height = st.number_input("Enter your Height  in (inches) :- ", 10, 200)

weight_conver = weight * 2.2046
BMI=((weight_conver*703)/(height * height) )

st.info('Hi ' + NAME + ", your BODY MASS INDEX is " + str(BMI))

if BMI>0:
    if(BMI<18.5):
        st.error("Classification : Underweight ")
        st.error("Health Risk : Minimal")
    elif(BMI<=24.9):
        st.success("Classification : Normal weight")
        st.success("Health Risk : Minimal")
    elif(BMI<=29.9):
        st.success("Classification : Overweight ")
        st.success("Health Risk : Increased")
    elif(BMI<=34.9):
        st.warning("Classification : Obese ")
        st.warning("Health Risk : High")
    elif(BMI<=39.9):
        st.error("Classification : Severely Obese ")
        st.warning("Health Risk : Very High ")
    else:
        st.error("Classification : Morbidly Obese ")
        st.error("Health Risk : extremely High ")
else:
    st.error("Enter Valid Input")        



