import streamlit
streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣Omega 3 and blueberry Oatmeal')
streamlit.text('🥗Kale,Spinach Rocket Smoothie')
streamlit.text('Hard-Boild Free_Range Egg')
streamlit.text('Avocado Toast')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
# let put's pick list here so they can pick the fruit they want to include
streamlit.multiselect("pick some fruit",list(my_fruit_list.index),['Avocado','Strawberries'])
#display the table on the page
streamlit.dataframe(my_fruit_list)
fruits_selected=streamlit.multiselect("pick some fruit",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)
