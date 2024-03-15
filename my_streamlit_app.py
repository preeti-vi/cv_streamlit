import streamlit as st

st.title("My First app")
st.header("Header")
image = st.file_uploader("Open a file")
if image:
    st.image(image)
movie = st.selectbox("Choose the movie",["Kahani","Jo Jeeta..","Duniyadari"])
st.text("Good choice !!")
st.write("You have choose a movie : " + movie)
flag = st.checkbox("Do you want to watch it now ?")
if flag:
    st.text("Yes !")
else:
    st.text("No, later !")