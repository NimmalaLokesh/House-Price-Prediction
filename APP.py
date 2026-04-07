# import streamlit as st
# import pandas as pd
# import joblib 

# # st.set_page_config(page_icon="🏡",page_title="House_Price_Prediction",layout="wide")
# # st.title("HPP")
# # st.header("HPP")
# # st.subheader("HPP")
# # st.write("HPP")

# # st.text_input('Name:',placeholder="Type Your Name")
# # st.text_area("Address:",placeholder="Type Your Address",height=200)
# # st.number_input("Age:",min_value=18,max_value=75)

# # st.selectbox("SELECT:",options=["A","B","C","D"])

# # st.radio("SELECT:",options=["A","B","C","D"],horizontal=True)

# df = pd.read_csv("Cleaned_df.csv")

# st.set_page_config(page_icon='🏘',page_title='HOUSEPRICEPREDICTION',layout='wide')
# st.header("HOUSE PRICE PREDICTION")
# st.image("house_logo.png",width = 300)

# # location = st.selectbox("LOCATION :", options=df['location'].unique())
# # sqft = st.number_input("SQ.FT :", min_value = 300)
# # bath = st.selectbox("Number Of Bathrooms :",options = sorted(df['bath'].unique()))
# # bhk = st.selectbox("Number Of Bedrooms :", options = sorted(df['bhk'].unique()))

# with st.container(border=True):

#     col1,col2 = st.columns(2)
#     with col1:
#         location = st.selectbox("LOCATION :",options=df['location'].unique())
#         sqft = st.number_input("SQ.FT :",min_value=300)

#     with col2:
#         bath = st.selectbox("Number Of Bathrooms :",options = sorted(df['bath'].unique()))
#         bhk = st.selectbox("Number Of Bedrooms :",options = sorted(df['bhk'].unique()))


import streamlit as st
import pandas as pd
import joblib

with open("Rf_model.joblib","rb") as file:
    model=joblib.load(file)

df=pd.read_csv("cleaned_df.csv")

st.set_page_config(page_icon="🏠",page_title="House Price Prediction",layout="wide")
st.header("House Price Prediction")
st.image("house_logo.png",width=300)


with st.container(border=True):

    col1,col2=st.columns(2)
    with col1:
        location=st.selectbox("Location : ",options=df["location"].unique())
        sqft=st.number_input("SQ.FT :",min_value=300)

    with col2:
        bath=st.selectbox("Number of Bathrooms : ",options=sorted(df["bath"].unique()))
        bhk=st.selectbox("Number of BedRooms : ",options=sorted(df["bhk"].unique()))

def get_encoded_loc(location):
    for loc,encoded in zip(df["location"],df["encoded_loc"]):
        if location == loc:
            return encoded
        
encode=get_encoded_loc(location)

if st.button("PREDICT"):
    input_data=[[sqft,bath,bhk,encode]]
    pred=model.predict(input_data)
    pred=float(f'{pred[0]:.2f}')
    st.subheader(f"PREDICTED PRICE : Rs.  {pred*100000}")