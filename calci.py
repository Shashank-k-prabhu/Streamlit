#run stream lit web app

import streamlit as st
st.title("Basic calucaltor")

a=st.slider("Enter 1st number",0,1000,500)
b=st.slider("Enter 2nd number")

select = st.selectbox("What would you want to do",("addition","subtraction","multiplication","division"))
st.write(select)
if(select=="addition"):
    add=int(a)+int(b)
    st.title(f'The sum of {a} and {b} is {add}')
elif(select=="subtraction"):
    sub=int(a)-int(b)
    st.title(f'The subtraction of {a} and {b} is {sub}')
elif(select=="multiplication"):
    mult=int(a)*int(b)
    st.title(f'The multiplication of {a} and {b} is {mult}')
elif(select=="division"):
    div=float(a)/float(b)
    st.title(f'The division of {a} and {b} is {div:.2f}')
else:
    st.write("wrong input")

