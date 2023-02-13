import streamlit
streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('Omega 3 and blueberry Oatmeal')
streamlit.text('Kale,Spinach Rocket Smoothie')
streamlit.text('Hard-Boild Free_Range Egg')
streamlit.text('Avocado Toast')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
